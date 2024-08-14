# Fix for Wordpress 500 internal server error
# This will correct a typo in wp-settings.php file

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
