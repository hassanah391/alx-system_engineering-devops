# Web Server Configuration Scripts

This repository contains a collection of scripts for configuring and managing web servers, primarily focused on Nginx installation and configuration on Ubuntu systems.

## Scripts Overview

- [`0-transfer_file`](0-transfer_file) - Transfers files to a server using SCP
- [`1-install_nginx_web_server`](1-install_nginx_web_server) - Basic Nginx installation and configuration
- [`2-setup_a_domain_name`](2-setup_a_domain_name) - Contains domain name configuration (digitalhassan.tech)
- [`3-redirection`](3-redirection) - Configures Nginx with a 301 redirect
- [`4-not_found_page_404`](4-not_found_page_404) - Sets up custom 404 error page
- [`7-puppet_install_nginx_web_server.pp`](7-puppet_install_nginx_web_server.pp) - Puppet manifest for Nginx configuration

## Features

- Nginx installation and configuration
- Custom domain setup
- 301 redirections
- Custom 404 error pages
- File transfer automation
- Infrastructure as Code using Puppet

## Requirements

- Ubuntu server
- Bash shell
- Puppet (for manifest execution)
- Root/sudo privileges

## Usage

Each script can be executed independently. Make sure to set execution permissions:

```bash
chmod +x script-name
./script-name
```
