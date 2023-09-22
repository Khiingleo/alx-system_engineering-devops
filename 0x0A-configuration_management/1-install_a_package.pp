# using Puppet, install flask from pip3

file { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
