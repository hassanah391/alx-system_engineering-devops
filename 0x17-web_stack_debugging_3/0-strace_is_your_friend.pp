# Problem: Apache returns 500
# Solution: use this script to fix typo in config

exec { 'fix config typo':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  onlyif  => "grep '.phpp' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Exec['fix config typo'],
}
