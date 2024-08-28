# 1-user_limit.pp

# Ensure the holberton user exists
user { 'holberton':
  ensure     => present,
  managehome => true,
}

# Increase hard file limit for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf || echo "holberton hard nofile 50000" >> /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  unless  => 'grep -q "holberton hard nofile 50000" /etc/security/limits.conf',
}

# Increase soft file limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf || echo "holberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  unless  => 'grep -q "holberton soft nofile 50000" /etc/security/limits.conf',
}
