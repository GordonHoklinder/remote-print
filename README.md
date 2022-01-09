# About


This project aims to create an extremly simple way how to print on a 3D printer in a private network. It was tested on Prusa Mini, but as the gcodes used are not specific to this printer, it should work without a problem for most of the printers.

For a printer which is in a network where it's possible to set up a public server, Octoprint (see https://www.octoprint.org) may be a better solution.
However if this is not the case, Octoprint cannot be used and this project provides an alternative in such case.


# How to use it

## Setting up server

It's required to host this Django project on a public server.

First clone this repository `git clone https://www.github.com/GordonHoklinder/remote-print/`.

Then set up the server. If you've never done this, I found this guide useful: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04 .

You should be able to get to see the web app after accessing the server's ip address.

## Setting up raspberry

Generate ssh key on your raspberry pi (see https://docs.gitlab.com/ee/ssh/#generate-an-ssh-key-pair) and add your public key to the allowed ssh keys on your server.

Make sure you can access the server by running `ssh username@ip.address.of.the.server`.

Clone this repository on your raspberry `git clone https://www.github.com/GordonHoklinder/remote-print/`.

Next, create the file `server_address` using your favourite text editor `vim remote-print/raspberry/server_address` and write there the ssh target (i.e. `username@ip.address.of.the.server`).

Connect the 3D printer and give the permisions to read and write to the USB port by `sudo chmod 666 /dev/ttyACM0`.

Install the dependencies by `pip install -r remote-print/raspberry/requirements.txt` (recommended to install to a virual environment) and run the program `cd remote-print/raspberry/` and `python3 main_controller.py`.

## Wrap up

You're ready to print!

Try to submit a .gcode file on the server and your printer should automatically start the print.

## Troubleshooting

### Different type of printer

It's possible to use Remote Print with any type of 3D printer, not just Prusa Mini. For the majorito of printers, it shouln't be a problem, but it may be that your printer does not support the `M20` calibration gcode. If this is the case, the only thing you need to do is to replace the gcode in `remote-print/printing/gcode_sender` with the one corresponding to your printer.

### Custom location of the server app
If you did not clone this repository on the server into your home folder, you may be getting errors on your raspberry. To solve this, change the `SERVER_GCODE_LOCATION` in the file `remote-print/raspberry/file_loader.py` appropriately.

### Different USB port
If the printer is connected to a different port than `ttyACM0` the app will refuse to run. This can be fixed by editing the `USB_PORT` property in the file `remote-print/printing/gcode_sender`.

# Final notes

This project was created as a seminary project for the course Programming 1 in the Bachelor's programme Computer Science at Charles University.

You can learn more about the structure of the project in the programmer's documentation.

The code in this repository can be used as described in LICENSE.

If you've found any issues or there are any features missing, do not hasitate to raise an issue or create a pull request.






