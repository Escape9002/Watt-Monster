import os
from dotenv import load_dotenv
load_dotenv()

INTERFACE = os.environ.get('INTERFACE')
HOSTNAME = os.environ.get('HOSTNAME')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
HOSTNAME_MGMT = os.environ.get('HOSTNAME_MGMT')

def check_ping():
    response = os.system("ping -c 1 " + HOSTNAME)
    if response == 0:
        pingstatus = "Server online!"
    else:
        pingstatus = "Server offline -_-"
    
    return pingstatus

from wakeonlan import send_magic_packet
def turn_on():
    send_magic_packet(INTERFACE, ip_address=HOSTNAME_MGMT)



from proxmoxer import ProxmoxAPI
def turn_off():
    proxmox = ProxmoxAPI(HOSTNAME, user=USERNAME, password=PASSWORD, verify_ssl=False)
    proxmox.post('/api2/json/nodes/node1/status', 'shutdown')