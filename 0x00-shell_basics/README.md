# Shell Basics Project

This project contains a collection of Bash scripts that perform various tasks. These tasks range from navigating directories to manipulating files and directories.

## Project Structure

The project is structured as follows:

- `0-current_working_directory`: A script that prints the absolute path name of the current working directory.
- `1-listit`: A script that displays the contents list of your current directory.
- `2-bring_me_home`: A script that changes the working directory to the user’s home directory.
- `3-listfiles`: A script that displays current directory contents in a long format.
- `4-listmorefiles`: A script that displays current directory contents, including hidden files (starting with .).
- `5-listfilesdigitonly`: A script that displays current directory contents with user and group IDs displayed numerically.
- `6-firstdirectory`: A script that creates a directory named `holberton` in the `/tmp/` directory.
- `7-movethatfile`: A script that moves the file `betty` from `/tmp/` to `/tmp/holberton`.
- `8-firstdelete`: A script that deletes the file `betty` in `/tmp/holberton`.
- `9-firstdirdeletion`: A script that deletes the directory `holberton` that is in the `/tmp` directory.
- `10-back`: A script that changes the working directory to the previous one.
- `11-lists`: A script that lists all files (even ones with names beginning with a period character) in the current directory and the parent of the working directory and the `/boot` directory, in long format.
- `12-file_type`: A script that prints the type of the file named `iamafile`.
- `13-symbolic_link`: A script that creates a symbolic link to `/bin/ls`, named `__ls__`.
- `14-copy_html`: A script that copies all the HTML files from the current working directory to the parent of the working directory.
- `100-lets_move`: A script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
- `101-clean_emacs`: A script that deletes all files in the current working directory that end with the character `~`.
- `102-tree`: A script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/holberton` in the current directory.
- `103-commas`: A script that lists all the files and directories of the current directory, separated by commas (`,`).

## Usage

Each script can be run from the command line as follows:

```bash
./script_name
```
