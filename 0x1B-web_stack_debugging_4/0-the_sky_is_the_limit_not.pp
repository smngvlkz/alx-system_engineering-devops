# Increase the number of worker processes for Nginx to handle high traffic

exec { 'fix--for-nginx':
  command => 'sudo sed -i "s/worker_processes 1/worker_processes 4/" /etc/nginx/nginx.conf && sudo service nginx restart',
}
