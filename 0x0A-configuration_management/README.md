0x0A. Configuration management - DevOps, SysAdmin, Scripting, CI/CD

# Configuration Management

This project contains Puppet manifests for various system configuration tasks.

## Files

- `0-create_a_file.pp`: Creates a file in /tmp with specific requirements.
- `1-install_a_package.pp`: Installs Flask version 2.1.0 using pip3.
- `2-execute_a_command.pp`: Kills a process named killmenow.

## Requirements

- All files are interpreted on Ubuntu 20.04 LTS
- All files end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Puppet manifests pass puppet-lint version 2.1.1 without errors
- Puppet manifests run without error
- Puppet manifests first line is a comment explaining the manifest
- Puppet manifest files end with the extension .pp

## Tasks

### 0. Create a file

Creates a file in /tmp with the following requirements:
- File path is /tmp/school
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains "I love Puppet"

### 1. Install a package

Installs Flask from pip3 with the following requirements:
- Install Flask
- Version must be 2.1.0

### 2. Execute a command

Creates a manifest that kills a process named killmenow:
- Must use the exec Puppet resource
- Must use pkill

## Note

This project is designed to work with Puppet 5.5 preinstalled on Ubuntu 20.04 VM. Do not attempt to upgrade versions.

## Installation

To install the required versions of puppet and puppet-lint:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
$ gem install puppet-lint
```
