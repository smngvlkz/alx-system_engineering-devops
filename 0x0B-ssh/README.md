0x0B. SSH - DevOps, SSH, Network, SysAdmin, Security

This project covers SSH configuration and key management.

## Files

- `0-use_a_private_key`: Bash script that uses ssh to connect to a server using a private key.
- `1-create_ssh_key_pair`: Bash script that creates an RSA key pair.
- `2-ssh_config`: SSH client configuration file.
- `100-puppet_ssh_config.pp`: Puppet manifest to configure the SSH client.

## Tasks

### 0. Use a private key
Connects to a server using ssh with a private key.

### 1. Create an SSH key pair
Creates an RSA key pair with specific requirements.

### 2. Client configuration file
Configures the SSH client to use a specific private key and refuse password authentication.

### 3. Let me in!
Added a provided public key to the server for the ubuntu user.

### 4. Client configuration file (w/ Puppet)
Uses Puppet to configure the SSH client to use a specific private key and refuse password authentication.

## Requirements

- All Bash scripts are interpreted on Ubuntu 20.04 LTS
- All files end with a new line
- All Bash scripts must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does
