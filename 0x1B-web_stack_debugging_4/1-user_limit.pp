#!/usr/bin/ruby

# changing the OS configuration to allow login

user { 'holberton':
  ensure  => present,
  shell   => 'bin/bash',
}

# Excuting the the set limit for the user login

exec { 'increase-sof-file-limit-for-holberton-user':
       command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  user    => 'holberton',
  path    => 'usr/local/bin/:/bin/',
}
