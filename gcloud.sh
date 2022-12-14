#!/bin/bash
cd ~/Downloads
file="google-cloud-cli-412.0.0-darwin-arm.tar.gz"
link="https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/"

curl -L "$link""$file" | tar xz 
CLOUDSDK_CORE_DISABLE_PROMPTS=1 ./google-cloud-sdk/install.sh

gcloud components update
gcloud components install gke-gcloud-auth-plugin


