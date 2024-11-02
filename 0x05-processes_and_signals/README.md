# Processes and Signals
This repository contains code examples that demonstrate essential concepts of system engineering and DevOps related to processes and signals, including:
- `ps`
- `pgrep`
- `kill`
- `pkill`
- `SIGINT` (Ctrl-C)
- `SIGTERM` (`kill`)
- `SIGQUIT` (Ctrl-\\)

## File Descriptions

### Process Management
* `0-what-is-my-pid` - Displays the current Bash script's PID
* `1-list_your_processes` - Lists all currently running processes
* `2-show_your_bash_pid` - Displays PIDs of Bash processes using `ps`
* `3-show_your_bash_pid_made_easy` - Displays PIDs of Bash processes using `pgrep`

### Signal Handling
* `4-to_infinity_and_beyond` - Creates an infinite loop with `sleep 2` (can be terminated with Ctrl-C)
* `5-dont_stop_me_now` - Script to terminate process 4 from a different terminal
* `6-stop_me_if_you_can` - Script to terminate process 4 using `pkill`
* `7-highlander` - Enhanced version of process 4 that catches Ctrl-C (SIGINT) and displays a message
* `8-beheaded_process` - Script to successfully terminate process 7 using `pkill`

### Advanced Examples
* `100-process_and_pid_file` - Infinite loop with Ctrl-C termination capability
* `101-manage_my_process` - Infinite loop with multiple signal handling and clean exit
* `102-zombie.c` - Creates 5 zombie processes for demonstration

## Environment
- **Language**: Bash scripts
- **Operating System**: Ubuntu 20.04 LTS
- **Execution**:
  ```bash
  chmod +x [filename]
  ./[filename]
  ```
- **Code Style**: Following [Shellcheck](https://github.com/koalaman/shellcheck) guidelines

## Author
Hassan Ahmed
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hassan-ahmed-77578b206/)