#!/bin/bash

EXPECTED_ARGS=1
E_BADARGS=65
SFOLDER="/home/iis/Desktop/sweb-1/"

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: $0 buildstart v start v build v debug v builddebug"
  exit $E_BADARGS
else
  arg=$1 
fi

if [ $arg == "buildstart" ]
then 
  mkdir -p /tmp/sweb; cd /tmp/sweb; 
  cmake ${SFOLDER}
  make
  make qemu
elif [ $arg == "build" ]
then
  mkdir -p /tmp/sweb; cd /tmp/sweb; 
  cmake ${SFOLDER}
  make
else
  if [ $arg == "start" ]
  then
    cd /tmp/sweb
    make qemu
  elif [ $arg == "builddebug" ]
  then
    mkdir -p /tmp/sweb; cd /tmp/sweb; 
    cmake ${SFOLDER}
    make
    make qemugdb
  else
    if [ $arg == "debug" ]
    then
      cd /tmp/sweb
      make qemugdb
    elif [ $arg == "clean" ]
    then
      rm -rf /tmp/sweb/
    else
      echo "Unknown Argument"
      exit $E_BADARGS    
      fi
  fi
fi



