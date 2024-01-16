#!/bin/bash

# Create a group for permissions to the directory
sudo groupadd hf-users
sudo usermod -aG hf-users $USER

# Create shared directory and make it owned by the group
sudo mkdir --mode=u+rwx,g+rwxs,o-rwx /huggingface # Give the directory rwx for user and group, and make files the directory inherit these permissions
sudo chown $USER /huggingface/
sudo chgrp hf-users /huggingface/

# Add shared cache activation to .bashrc
cat <<EOF >> $HOME/.bashrc
export HF_HOME="/huggingface" # Download HF cache items to /huggingface
umask 002 # Give user and group rw/rwx by default
EOF
source $HOME/.bashrc

# Optional: join the group in this shell, or restart the shell
newgrp hf-users
