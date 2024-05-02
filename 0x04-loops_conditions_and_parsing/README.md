# 0x04. Loops, Conditions and Parsing

This project contains a collection of Bash scripts that perform various tasks. These tasks range from parsing Apache log files to generating FizzBuzz sequences.

## Project Structure

The project is structured as follows:

- `0-RSA_public_key.pub`: Contains the RSA public key.
- `1-for_best_school`: A script that displays "Best School" 10 times using a `for` loop.
- `2-while_best_school`: A script that displays "Best School" 10 times using a `while` loop.
- `3-until_best_school`: A script that displays "Best School" 10 times using an `until` loop.
- `4-if_9_say_hi`: A script that displays "Best School" 10 times, but for the 9th iteration, displays "Best School" and then "Hi" on a new line.
- `5-4_bad_luck_8_is_your_chance`: A script that displays "Best School" 10 times, but for the 4th iteration, displays "4" and then "bad luck from China", and for the 8th iteration, displays "8" and then "good luck".
- `6-superstitious_numbers`: A script that displays numbers from 1 to 20 and displays "bad luck from China" for the 4th loop iteration, "bad luck from Japan" for the 9th loop iteration, and "bad luck from Italy" for the 17th loop iteration.
- `7-clock`: A script that displays the time for 12 hours and 59 minutes.
- `8-for_ls`: A script that displays the content of the current directory in a list format, where only the part of the name after the first dash is displayed.
- `9-to_file_or_not_to_file`: A script that gives information about the `school` file.
- `10-fizzbuzz`: A script that displays numbers from 1 to 100, replacing multiples of 3 and 5 with "Fizz" and "Buzz".
- `100-read_and_cut`: A script that displays the username, user id, and home directory path for each user in `/etc/passwd`.
- `101-tell_the_story_of_passwd`: A script that displays the content of the file `/etc/passwd` in a specific format.
- `102-lets_parse_apache_logs`: A script that displays the visitor IP along with the HTTP status code from the Apache log file.
- `103-dig_the-data`: A script that groups visitors by IP and HTTP status code, and displays this data.

## Usage

Each script can be run from the command line as follows:

```bash
./script_name
