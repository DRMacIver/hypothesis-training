# -*- mode: ruby -*-
# vi: set ft=ruby :

# This is a trivial Vagrantfile designed to simplify development of Hypothesis on Windows,
# where the normal make based build system doesn't work, or anywhere else where you would
# prefer a clean environment for Hypothesis development. It doesn't do anything more than spin
# up a suitable local VM for use with vagrant ssh. You should then use the Makefile from within
# that VM.

PROVISION = <<PROVISION
sudo apt-get install -y git python3

sudo python3 /vagrant/tools/get-pip.py

sudo pip install -r /vagrant/requirements.txt

PROVISION

Vagrant.configure(2) do |config|

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end

  config.vm.box = "bento/ubuntu-14.04"

  config.vm.provision "shell", inline: PROVISION, privileged: false
end
