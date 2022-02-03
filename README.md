# discord_updater
Updating of Discord channel's messages from the given URLs based on the simple schedule.

## dependencies
 pip3 install discord

## usage
 python3 message_updater.py config.json
 
## config file description

{ <br />
 "tokenID": "TOKEN_ID", <br />
 "channelID": CHANNEL_ID, <br />
 "URL_1" : "URL_FOR MESSAGE_1", <br />
 "URL_2":"URL_FOR_MESSAGE_2" - this value is optional <br />
 "refresh": seconds between publishing <br />
} <br /> 
