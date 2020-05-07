# docker.openvpn.server

An add-on for kodi to create a openvpn server that runs in raspeberry pi devices.

User a docker image which git is: nvdias0/rpi-docker-openvpn
The docker repository is in: nvdias/rpi-openvpn

## Installation

a) download docker.openvpn.server respository as a zip file.

b) Install as a kodi add-on (add-ons / install from zip file)

c) On first run define the server name in the kodi interface (should be the ddns name or wan ip address of the server)

d) Run openvpn-add-server in your pi's ssh console to define the server keys and openvpn cfg

e) Run openvpn-add-user in your pi's ssh console to create users

f) Restart the add-on

g) Open port 1194 UDP in your router

i) Give the files generated with openvpn-add-user to your users.


