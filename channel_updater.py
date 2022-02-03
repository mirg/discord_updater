import discord
import asyncio
import sys
import json
from datetime import datetime


print(f"[Channel updater] started.")

client = discord.Client()
bg_task=None

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

if len(sys.argv)!=2:
    print("Missing argument!");
    exit(-1);
try:
    print(f"Loading config file from {sys.argv[1]}...")
    config=read_json(sys.argv[1])
except Exception as inst:
     print("Cannot read or parse config file!");
     print(inst)
     exit(-2);

try:     
    tokenID = config["tokenID"]
    channelID = config["channelID"]

    URL_DAILY = config["URL_1"]
    URL_WEEKLY = config["URL_2"]
    refresh = config["refresh"]
except KeyError as e:    
     print(f"Invalid config file, missing key {e}!");
     exit(-3);


async def my_background_task():
    await client.wait_until_ready()
    messages = await client.get_channel(channelID).history(limit=20).flatten()
    if len(messages)==0 : 
            print("Empty channel, creating message...");
            await client.get_channel(channelID).send(content="Content")
            messages = await client.get_channel(channelID).history(limit=20).flatten()

    if len(URL_WEEKLY)>0:
        if len(messages)==1 : 
            print("Empty channel, creating message...");
            await client.get_channel(channelID).send(content="Content")
            messages = await client.get_channel(channelID).history(limit=20).flatten()
            
    if messages[0].author.id!=client.user.id:
            print("Not my message?, creating my own...");
            await client.get_channel(channelID).send(content="Content")
            messages = await client.get_channel(channelID).history(limit=20).flatten()

    if len(URL_WEEKLY)>0:
        if messages[1].author.id!=client.user.id:
            print("Not my message?, creating my own...");
            await client.get_channel(channelID).send(content="Content")
            messages = await client.get_channel(channelID).history(limit=20).flatten()
            
    now = datetime.now()
    sleepTime=refresh-(now.minute*60+now.second)+60;
    print(f"Publishing to channel: {client.get_channel(channelID).name}")
    print(f"Synchronizing {sleepTime}s...");
    while not client.is_closed():
        times=datetime.today().strftime('%Y-%m-%d-%H:%M:%S');
        if len(URL_WEEKLY)>0:
            await messages[0].edit(content=URL_WEEKLY+"?tst="+times)
            await messages[1].edit(content=URL_DAILY+"?tst="+times)
        else:    
            await messages[0].edit(content=URL_DAILY+"?tst="+times)
        
        print(f"Message(s) updated at {times}");
        await asyncio.sleep(sleepTime)
        if (sleepTime!=refresh):
            sleepTime=refresh;
        

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    bg_task = client.loop.create_task(my_background_task())    

@client.event
async def on_disconnect():
    print('Disconnected...');
    if bg_task:
        bg_task.cancel();
       
        
@client.event
async def on_message(message):
    if message.author == client.user:
        #ignore self messages
        return
    if (message.channel.id==channelID):    
        if message.content.startswith('$hello'):
            await message.channel.send('Hello '+message.author.name+"!")
        

client.run(tokenID)
