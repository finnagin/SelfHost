FROM ubuntu:20.04

# suppress debconf error messages:
ARG DEBIAN_FRONTEND=noninteractive

# add user "rt" and give sudo privilege:
RUN useradd rt -m -s /bin/bash

# install git and sudo
RUN apt-get update
RUN apt-get update  # running this twice seems to work around a weird 404 error
RUN apt-get install -y apt-utils
RUN apt-get install -y git sudo curl rsync

# give sudo privilege to user rt:
RUN usermod -aG sudo rt
RUN echo "rt ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/rt
RUN touch /home/rt/.sudo_as_admin_successful
RUN chown rt.rt /home/rt/.sudo_as_admin_successful

# configure ssh for user rt
RUN mkdir /home/rt/.ssh
RUN echo "StrictHostKeyChecking no" > /home/rt/.ssh/config
RUN echo "UserKnownHostsFile /dev/null" >> /home/rt/.ssh/config
RUN chown -R rt.rt /home/rt/.ssh
RUN chmod -R 700 /home/rt/.ssh

# install apache2
RUN apt-get update && apt-get install -yq apache2

# clone repo
RUN mkdir -p /mnt/data/orangeboard/production
RUN chown -R rt.rt /mnt/data/orangeboard/production
RUN su rt && cd /mnt/data/orangeboard/production && git clone https://github.com/finnagin/SelfHost.git && cd SelfHost
RUN chown -R rt.rt /mnt/data/orangeboard/production/SelfHost

# install python and packages
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.7 python3.7-dev python3.7-venv
RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.7 /usr/bin/python3
RUN su rt && cd /mnt/data/orangeboard/production/SelfHost && python3.7 -m pip install -r requirements.txt
