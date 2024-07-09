# Ensures the package is up to date
exec { 'update_packages':
  command => '/usr/bin/apt-get update',
}

# Installs Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update_packages'],
}

# Creates a custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => "add_header X-Served-By ${::hostname};",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensures Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_header.conf'],
}
