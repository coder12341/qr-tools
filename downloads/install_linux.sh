#!/bin/bash

clear
echo " ██████╗ ██████╗        ██████╗ ██████╗ ██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗  "
echo "██╔═══██╗██╔══██╗      ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗ "
echo "██║   ██║██████╔╝█████╗██║     ██║   ██║██║  ██║█████╗      ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝ "
echo "██║▄▄ ██║██╔══██╗╚════╝██║     ██║   ██║██║  ██║██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗ "
echo "╚██████╔╝██║  ██║      ╚██████╗╚██████╔╝██████╔╝███████╗    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║ "
echo " ╚══▀▀═╝ ╚═╝  ╚═╝       ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ "
echo "                                                                                                                                          "


function install() {
  if (( $EUID != 0 )); then
      printf "\nThe installation is for the current user only! If you want to install for all users run as root!\n"
      echo "The installation will begin in 10 seconds. Press Ctrl+C to abort!"
      sleep 10
      echo "Installing..."
      {
      cd ~/.local/share/ && mkdir qr-tools && cd qr-tools
      wget https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_linux_x64 -O qr-generator 
      chmod +x qr-generator
      } &> /dev/null
      echo 'export PATH=~/.local/share/qr-tools:$PATH' >> ~/.bashrc
      exit
  fi
    
  echo "The installation will begin in 10 seconds. Press Ctrl+C to abort!"
  sleep 10
  echo "Installing..."
  {
  cd /bin && wget https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_linux_x64 -O qr-generator
  chmod +x qr-generator
  
  } &> /dev/null
  exit
}

function uninstall() {
  echo "Removing..."
  if (( $EUID != 0 )); then
    cd ~/.local/share && rm -r qr-tools
    export PATH=${PATH%:~/.local/share/qr-tools}
    exit
  fi
 cd /bin && rm qr-generator
 exit
  
}


printf "(0)Install\n(1)Uninstall\n:"
read mode

if (( "$mode" == "0" )); then
  install
elif (( "$mode" == "1" )); then
  uninstall
else
  echo "Aborting..."
  exit
fi
