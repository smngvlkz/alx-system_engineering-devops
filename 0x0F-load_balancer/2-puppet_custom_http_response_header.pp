# Ensures the package 'nginx' is installed
package { 'nginx':
  ensure => installed,
}

# Ensures that the Nginx service is running and enabled at boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# The custom header configuration directly in the Puppet manifest definded
class custom_nginx_header ($hostname) {
  $custom_header_content = @(END)
add_header X-Served-By ${hostname};
END

  # The custom header configuration file created
  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => $custom_header_content,
    notify  => Service['nginx'],
  }
}

# The custom_nginx_header class with hostname fact included
class { 'custom_nginx_header':
  hostname => $facts['hostname'],
}
