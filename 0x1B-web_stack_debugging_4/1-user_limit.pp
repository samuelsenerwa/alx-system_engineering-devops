#!/usr/bin/ruby

# changing the OS configuration to allow login

user { 'holberton':
  ensure  => present,
  shell   => 'bin/bash'
}

# Excuting the the set limit for the user login

exec { 'set-file-limit':
  command => 'ulimit -n 4096',
  user    => 'holberton',
  path    => 'usr/bin',
}
