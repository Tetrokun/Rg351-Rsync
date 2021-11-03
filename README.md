# Rg351-Rsync

Script to sync Handheld emulator rg351's saves with folder on fileserver.

Edit worm.json to fit your needs. You must be able to auth using sshkeys (Passwordless)

This is mostly intended to be run from Chronos (https://github.com/simse/chronos), if you choose to run it from Chronos too, be sure to put the .json file in the working dir for the script

There is no reason you shouldn't be able to run this ad hoc either


But what does it do?
  Script sets up an SSH connection to a file server, using the paramaters defined in worm.py
  It then tries to Rsync The remote client directory into the Server directory.
  Once the Clint >> Server transfer is complete, we try and push new server Data to the Client, ensuring they match.


This shouldn't be desctructive, Use at your own risk. 
