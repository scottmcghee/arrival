#!/bin/bash

#you could expand this script to be a bit more interactive
#e.g. prompts to the user to supply values for the config
#but... I'm lazy

#set up virtualenv
virtualenv ds

#activate the virtualenv in this subshell
. ds/bin/activate

#install the required modules
pip install -r requirements.txt

#open the workflow to prompt the user to install the folder action
open DownloadStation.workflow