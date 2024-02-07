import os
import discord
from WattMonster import awake_the_monster, send_to_sleep, is_up

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WATTMONSTER_MAC = os.getenv('WATTMONSTER_MAC')
WATTMONSTER_IP = os.getenv('WATTMONSTER_IP')


intents=discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

commands = {
    "!help": "Displays this message", 
    "!info": "I dont know yet....maybe some stats for the future", 
    "!startle <name>": "Wakes up a pc/server. Currenty available:\n   WattMonster",
    "!sleep <name>": "Sends a PC to sleep. Currently available:\n   WattMonster",
    "!crafty": "Returns info about the MC server!",
    "!crafty <action>": "Special things to do ^^, for example:\n   coords"
    }

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    match message.content:
        case "!help":
            msg = f"These are the available commands:\n"
            for key, desc in commands.items():
                msg = msg + f'- {key} : {desc} \n'
            await message.channel.send(msg)

        case "!info":
            await message.channel.send("Not yet implemented")

        case "!startle WattMonster":
            await message.channel.send("BOOO!")
            awake_the_monster(WATTMONSTER_IP, WATTMONSTER_MAC)
            await message.channel.send("The monster has awakened!")

        case "!sleep WattMonster":
            await message.channel.send("Enough power for today! Go to SLEEP!")
            send_to_sleep('root', WATTMONSTER_IP)
            await message.channel.send("The monster has fallen asleep")
        
        case "!crafty":
            await message.channel.send(
                "To join the server, you have to join my VPN. Cant buy a domain atm. =/\nTo accept my routes run: \n```tailscale up --accept-routes```\nIf there are error messages, please read them (and then ask me).\nOn this server, there shall only be communism!\n\nJoin link: https://login.tailscale.com/admin/invite/EMGA7dZt6E4\nIP-Adress: 10.6.6.5\n")
            
        case "!crafty coords":
            important_coords = {
                "our base" : "800 800 (i hope)",
                "Unterwassertempel" : "1990 2100",
                "Mossy Höhle" : "2455 2294"
            }
            msg = "The stuff we found until now:\n"    
            for key, desc in important_coords.items():
                msg = msg + f'- {key} : {desc}\n'
        
            await message.channel.send(msg)

        case "!crafty status":
            if is_up(WATTMONSTER_IP):
                await message.channel.send("Crafty is ONLINE!")
            else:
                await message.channel.send("sorry, seems stuff is offline...might have to startle the WattMonster...")

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()