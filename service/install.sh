#!/bin/bash
cp discord_updater.service /lib/systemd/system/
sudo systemctl daemon-reload 

sudo systemctl enable discord_updater.service 
sudo systemctl start discord_updater.service 

sudo systemctl status discord_updater.service 
