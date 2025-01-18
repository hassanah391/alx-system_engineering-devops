# Puppet manifest to install and configure Nginx with specified requirements

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Configure the Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure the 'Hello World!' page exists
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

# Create the template for the Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF")
server {
    listen 80;

    server_name _;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://google.com;
    }
}
| EOF
}

