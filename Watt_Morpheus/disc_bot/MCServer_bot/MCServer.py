import os
import discord
from WattMonster import awake_the_monster, send_to_sleep, is_up
from Crafty_Server import get_ipv6, whitelist

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WATTMONSTER_MAC = os.getenv('WATTMONSTER_MAC')
WATTMONSTER_IP = os.getenv('WATTMONSTER_IP')
CRAFTY_IP = os.getenv('CRAFTY_IP')


intents=discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

commands = {
    "!help": "Displays this message", 
    "!info": "I dont know yet....maybe some stats for the future", 
    "!startle <name>": "Wakes up a pc/server. Currenty available:\n   WattMonster",
    "!sleep <name>": "Sends a PC to sleep. Currently available:\n   WattMonster",
    "!crafty": "Returns info about the MC server!",
    "!crafty <action>": "Special things to do ^^, for example:\n- - coords\n- - whitelist"
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
            return

        case "!info":
            await message.channel.send("Not yet implemented, maybe try '''!help''' instead")
            return

        case "!startle WattMonster":
            await message.channel.send("BOOO!")
            awake_the_monster(WATTMONSTER_IP, WATTMONSTER_MAC)
            await message.channel.send("The monster has awakened!")
            return

        case "!sleep WattMonster":
            await message.channel.send("Enough power for today! Go to SLEEP!")
            send_to_sleep('root', WATTMONSTER_IP)
            await message.channel.send("The monster has fallen asleep")
            return
        
        case "!crafty":
            ip = get_ipv6("crafty", CRAFTY_IP)
            
            await message.channel.send(
                f'I hope this works...I am not sure yet.\n Whitelist is enabled, make sure that you are whitelisted!\n\n To join enter this IP: {ip}\n')
            return
        
        case "!crafty coords":
            important_coords = {
                "our base" : "550 790 ",
                "Unterwassertempel" : "1990 2100",
                "Unterwassertempel (der 2te)" :  "-1200 1000 2",
                "Mossy Höhle" : "2455 2294",
                "end" : "-1150 1020 ",
                " lush cave" : "-37 25 871"
            }
            msg = "The stuff we found until now:\n"    
            for key, desc in important_coords.items():
                msg = msg + f'- {key} : {desc}\n'
        
            await message.channel.send(msg)
            return

        case "!crafty status":
            if is_up(WATTMONSTER_IP):
                await message.channel.send("Crafty is ONLINE!")
            else:
                await message.channel.send("sorry, seems stuff is offline...might have to startle the WattMonster...")
            return

    if message.content.startswith('!crafty whitelist'):
        player_names = message.content.replace('!crafty whitelist', '').strip()
        whitelist(player_names)
        
        await message.channel.send(f'Whitelisted player {player_names}')

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
