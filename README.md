# About

This project aims to create an extremly simple way how to print on a 3D Prusa Mini printer in a private network.

For a printer which is in a network where it's possible to set up a public server, Octoprint (see https://www.octoprint.org) may be a better solution.
However if this is not the case, Octoprint cannot be used and this project provides an alternative in such case.

You can learn more about the structure of the project in the programmer's documentation.

# How to use it

## Setting up server

It's required to host this Django project on a public server.

First clone this repository `git clone https://www.github.com/GordonHoklinder/remote-print/`.

Then set up the server. If you've never done this, I found this guide useful: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04 .

You should be able to get to see the web app after accessing the server's ip address.

<!-- TODO: signing in -->

## Setting up raspberry

Generate ssh key on your raspberry pi (see https://docs.gitlab.com/ee/ssh/#generate-an-ssh-key-pair) and add your public key to the allowed ssh keys on your server.

Make sure you can access the server by running `ssh username@ip.address.of.the.server`.

Clone this repository on your raspberry `git clone https://www.github.com/GordonHoklinder/remote-print/`.

Next, create the file `server_address` using your favourite text editor `vim remote-print/raspberry/server_address` and write there the ssh target (i.e. `username@ip.address.of.the.server`).








