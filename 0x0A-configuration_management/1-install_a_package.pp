# using Puppet, install flask from pip3

file { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
