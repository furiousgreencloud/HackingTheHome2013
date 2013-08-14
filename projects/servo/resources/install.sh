sudo cp /boot/kernel.img /boot/kernel-bac.img
sudo cp -A /lib/modules /lib/modules-bac
sudo cp tmp/kernel.img /boot/
sudo cp -R tmp/modules/lib/* /lib/
