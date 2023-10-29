# client configuration using puppet
#include stdlib

file_line { 'Turn off password authentication':

  ensure  => present,

  path    => '/etc/ssh/ssh_config',

  line    => 'PasswordAuthentication no',

  replace => true,

}



file_line { 'Declare identity file':

  ensure  => present,

  path    => '/etc/ssh/ssh_config',

  line    => 'IdentityFile ~/.ssh/school',

  replace => true,

}


