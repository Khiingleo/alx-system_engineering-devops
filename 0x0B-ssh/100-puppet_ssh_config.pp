# use puppet to set up client SSH congiguration file to connect without 
# password
include stdlib


file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  replace => true,
}

file_line { 'Declare identify file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentifyFile ~/.ssh/school',
  match   => '^IdentifyFile',
  replace => true,
}