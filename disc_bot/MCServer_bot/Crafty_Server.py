import os
from dotenv import load_dotenv
import paramiko 
import requests
from dotenv import load_dotenv

load_dotenv()
CRAFTY_IP = os.getenv('CRAFTY_IP')
CRAFTY_BEARER = os.getenv('CRAFTY_BEARER')

def get_ipv6(usr: str, ip:str):
    
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh_client.look_for_keys(True)

        # Connect to the server
        ssh_client.connect(ip, username=usr)
        
        # Execute shutdown command
        stdin, stdout, stderr = ssh_client.exec_command('ip -6 addr show ens18 | grep -oP \'(?<=inet6\s)[\da-f:]+\' | head -n 1 | awk \'{print $1}\' ')
        
        ip = stdout.read().decode("utf8")
        # Wait for command to complete
        stdout.channel.recv_exit_status()        
        
        # Because they are file objects, they need to be closed
        stdin.close()
        stdout.close()
        stderr.close()
        return ip
    
    except Exception as e:
        print(f"Error: {e}")

def whitelist(usr:str):
    
    endpoint = f'https://{CRAFTY_IP}:8443/api/v2/servers/1/stdin'
    data = f'whitelist add {usr}'
    headers = {"Authorization": f'Bearer {CRAFTY_BEARER}'}

    print(requests.post(endpoint, data=data, headers=headers,verify=False).json())