#!/bin/bash
# Install the files to the correct location in your HOME dir.
# Also replace the variables correctly with the user email.

set -e

cwd="$(dirname -- ${BASH_SOURCE[0]})"
email="$1"

if [[ -z "$email" ]]; then
    echo "Requires user email as first argument" 1>&2
    exit 1
fi

# Install application script/config
mkdir -p ~/.config/fedora-messaging
cp $cwd/podman.py ~/.config/fedora-messaging
sed -i "s/REPLACEME/$email/" ~/.config/fedora-messaging/podman.py
cp $cwd/podman.toml ~/.config/fedora-messaging
sed -i "s/REPLACEME/$email/" ~/.config/fedora-messaging/podman.toml

# Install unit file
mkdir -p ~/.config/systemd/user
cp $cwd/podman-openqa.service ~/.config/systemd/user

systemctl --user daemon-reload
systemctl --user enable podman-openqa.service
# restart in case a previous version was already running
systemctl --user restart podman-openqa.service
