#!/usr/bin/ruby
# Increasing the number of traffic Nginx can handle

exec { 'fix-for-nginx':
  command     => 'sed -i "s/15/4096/" /etc/default/nginx',
  path        => '/usr/local/bin:/bin',
  refreshonly => true,
}

# Restarting Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/sbin:/usr/sbin:/bin:/usr/bin',
}
