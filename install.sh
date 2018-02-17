#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

prompt_confirm() {
  while true; do
    read -r -n 1 -p "${1:-Continue?} [y/n]: " REPLY
    case $REPLY in
      [yY]) echo ; return 0 ;;
      [nN]) echo ; return 1 ;;
      *) printf " \033[31m %s \n\033[0m" "invalid input"
    esac
  done
}

if hash python3 2>/dev/null; then
    python3 -m pip install Pyflai
else
    prompt_confirm "Python3 is required for using Pyflai, do you want us to install it for you?" || apt-get install python3 -y
fi