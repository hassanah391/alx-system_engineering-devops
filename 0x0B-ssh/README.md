# SSH Configuration and Management

Part of ALX Software Engineering Program focused on SSH configuration, key management and secure server access.

## Files and Descriptions

| File | Description |
|------|-------------|
| `0-use_a_private_key` | Bash script using SSH to connect to server using `~/.ssh/school` private key with user `ubuntu` |
| `1-create_ssh_key_pair` | Bash script that creates 4096 bit RSA key pair with name "school" |
| `2-ssh_config` | SSH client configuration file showing connection debugging output | 
| `100-puppet_ssh_config.pp` | Puppet manifest to configure SSH client without password authentication |

## Usage Examples

### Connect to Server
```bash
./0-use_a_private_key
```
### Create New Key Pair
```bash
./1-create_ssh_key_pair 
```

### Apply Puppet Config

```
sudo puppet apply 100-puppet_ssh_config.pp
```

## SSH Configuration Details
- Private key: ~/.ssh/school
- Password authentication: disabled
- User: ubuntu
- Host: server IP
