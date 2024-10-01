import os
import smtplib

from email.message import EmailMessage
from fedora_messaging import config


class SaveMessage:
    """
    A fedora-messaging consumer that saves the message to a file.

    A single configuration key is used from fedora-messaging's
    "consumer_config" key, "path", which is where the consumer will save
    the messages::

        [consumer_config]
        path = "/tmp/fedora-messaging/messages.txt"
    """

    def __init__(self):
        """Perform some one-time initialization for the consumer."""
        self.path = config.conf["consumer_config"]["path"]

        # Ensure the path exists before the consumer starts
        if not os.path.exists(os.path.dirname(self.path)):
            os.mkdir(os.path.dirname(self.path))

    def __call__(self, message):
        """
        Invoked when a message is received by the consumer.

        Args:
            message (fedora_messaging.api.Message): The message from AMQP.
        """

        # openqa.job.done or ci.fedora-update.test.complete
        queue = message.topic.removeprefix("org.fedoraproject.prod.")

        if "test" in message.body:
            # ci.fedora-update
            which_test = message.body["test"]["type"]
            ts = message.body["generated_at"]           # ISO9601
            result = message.body["test"]["result"]
        elif "TEST" in message.body:
            # openqa.job
            which_test = message.body["TEST"]
            ts = message._headers["sent-at"]
            result = message.body["result"]
        else:
            raise "FIXME I don't know what this is"

        if "podman" not in which_test:
            return
        print(">>>>>>> it is podman! + ", result)

        outfile = os.path.join(os.path.dirname(self.path), ts) + "." + queue + "." + result
        with open(outfile, "a") as fd:
            fd.write(str(message))

        # FIXME: if result != passed, notify Ed, include run.log run.url
        if result != "passed":
            email = EmailMessage()
            email['From'] = 'OpenQA Podman <openqapodman@redhat.com>'
            # ESM: if this is running on your laptop, just 'yourusername' is fine
            email['To'] = 'REPLACEME'

            # e.g. 'podman_client failed'
            subj = which_test.split(' ')[0] + ' ' + result
            try:
                subj += ": " + message.body["artifact"]["builds"][0]["nvr"]
            except:
                True
            email['Subject'] = subj

            if "run" in message.body:
                url = message.body["run"]["url"]
            else:
                url = "https://openqa.fedoraproject.org/tests/" + message.body["id"]

            email.set_content(queue + "\n\n" + url + "\n\n" + str(message))

            s = smtplib.SMTP('localhost')
            s.send_message(email)
            s.quit()
