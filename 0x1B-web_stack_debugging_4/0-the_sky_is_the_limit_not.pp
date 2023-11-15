# puppet file that changes the limit that nginx can handle

exec { 'fix-for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['restart-nginx'],
}

exec {'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
