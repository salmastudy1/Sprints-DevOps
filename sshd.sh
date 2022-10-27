#!/usr/bin/env bash

echo "Enter an Integer to be SSH Port"
read portInt

if! [[ "$port"=~ ^[0-9]+$ ]]; 
then 
  echo "Enter an Integer"
else

  if [[ ${INT_FROM_USER} -lt 1024  && ${INT_FROM_USER} != 22 || ${INT_FROM_USER} -gt 65535 ]]
  then 
	  echo "Enter an Integer between 1024 and 65535 or 22"
  else
	  sed -i -e "/Port /c\Port ${portInt}" /etc/ssh/sshd_config
	  echo "The Port number is changed to $portInt"
  fi
fi  

sed -i -e "/PermitRootLogin /c\PermitRootLogin no" /etc/ssh/sshd_config
echo "Disabled root login"
service sshd restart
echo "Restarted ssh service"
