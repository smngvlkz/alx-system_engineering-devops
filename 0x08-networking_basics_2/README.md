0x08. Networking basics #1 - Devops, Network and SysAdmin


## Description
This project contains a collection of Bash scripts designed to perform various network configurations and diagnostics on an Ubuntu 20.04 LTS server. The scripts include functionality to modify the system's IP resolution for specific hosts, display all active IPv4 addresses, and set up a listener on a specified port.

## Getting Started

### Dependencies
- Ubuntu 20.04 LTS
- Bash shell
- `netcat` for port listening script

### Installing
- Clone the repository or download the scripts directly.
- Ensure scripts are executable with `chmod +x script_name`.

### Executing Programs
- Run the scripts with appropriate permissions, using `sudo` if required.

**0-change_your_home_IP**
Configures localhost to resolve to 127.0.0.2 and facebook.com to resolve to 8.8.8.8.

sudo ./0-change_your_home_IP


**1-show_attached_IPs**
Displays all active IPv4 IPs on the machine.

./1-show_attached_IPs


**100-port_listening_on_localhost**
Sets up a listener on port 98 on localhost.

sudo ./100-port_listening_on_localhost


## Help
Any advise for common problems or issues.

command to run if program contains helper info


## Contibuting

This project is a learning exercise by ALX Africa.

