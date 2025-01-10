# Puppet Manifests Repository

This repository contains Puppet manifests for various tasks.

## Manifests

### 0-create_a_file.pp

This manifest creates a file at `/tmp/school` with the following properties:
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

### 1-install_a_package.pp

This manifest installs the Flask package using `pip3` with the following properties:
- Package name: `Flask`
- Version: `2.1.0`

### 2-execute_a_command.pp

This manifest kills a process named `killmenow` using the `exec` resource with the following properties:
- Command: `/usr/bin/pkill -f /killmenow`

## Usage

To apply a manifest, use the following command:

```sh
puppet apply <manifest_file.pp>
```

## Environment
Operating System: Ubuntu 20.04 LTS

Puppet-lint version: 2.1.1
