import os
from dotenv import load_dotenv
import paramiko 

from wakeonlan import send_magic_packet

from dotenv import load_dotenv

load_dotenv()
WATTMONSTER_PWD = os.getenv('WATTMONSTER_PWD')

def is_up(hostname : str):
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        print(f"{hostname} is up!")
        return True
    else:
        print(f"{hostname} is down!")
        return False


def awake_the_monster(ip:str, mac: str):
    while not is_up(ip):
        send_magic_packet(mac)

def send_to_sleep(usr: str, ip:str):
    
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh_client.connect(ip, username=usr, password=WATTMONSTER_PWD)
        
        # Execute shutdown command
        stdin, stdout, stderr = ssh_client.exec_command('shutdown')
        
        # Wait for command to complete
        stdout.channel.recv_exit_status()
        
        print("Server shutdown command executed successfully.")
    
    except Exception as e:
        print(f"Error: {e}")