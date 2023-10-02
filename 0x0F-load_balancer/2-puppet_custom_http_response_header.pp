# use puppet to automate the task of creating a custom HTTP header response

exec {'apt-update':
  command  => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => 'installed',
}

file {'/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => "location / {\n  add_header X-Served-By ${facts['networking']['hostname']};\n}\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service {'nginx':
  ensure => running,
  enable => true,
}

exec {'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
