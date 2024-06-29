# Puppet manifest to configure ssh client

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^#?\s*PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^#?\s*IdentityFile',
}
