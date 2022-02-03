#/bin/bash
cd /home/opc/discord_updater
echo "STARTING " >>channel_updater.log
python3 channel_updater.py RNS.json >> channel_updater.log

