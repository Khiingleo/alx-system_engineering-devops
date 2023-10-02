# automate the task of creating a custom HTTP header response, but with Puppet.

$host = $::hostname

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec {'install nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  require  => Exec['update'],
}

package {'nginx':
  ensure  => 'installed',
}

service {'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file {'/etc/nginx/sites-available/default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'listen 80 default_server',
  line   => "\n\tadd_header X-Served-By \"${host}\";",
}

exec {'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
