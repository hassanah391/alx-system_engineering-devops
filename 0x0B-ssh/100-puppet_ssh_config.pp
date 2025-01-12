# A puppet config file to set up your client SSH configuration file
# so that you can connect to a server without typing a password.
#
# Requirements:
# - must be configured to use the private key ~/.ssh/school
# - must be configured to refuse to authenticate using a password

file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0600',
  content => @(SSHCONFIG)
Host alx_server
  HostName 100.26.246.61
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
SSHCONFIG

}
