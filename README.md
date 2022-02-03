# discord_updater
Updating of Discord channel's messages from the given URLs based on schedule.

dependencies:
 pip3 install discord

usage:
 python3 message_updater.py config.json
 
config file description
 "tokenID": "TOKEN_ID",
 "channelID": CHANNEL_ID,
 "URL_1" : "URL_FOR MESSAGE_1",
 "URL_2":"URL_FOR_MESSAGE_2" - this value is optional
 "refresh": seconds between publishing
