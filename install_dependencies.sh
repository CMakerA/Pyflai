#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

while [ "$#" -gt 0 ]; do
  case "$1" in
	# TODO: Check what to install params
    -i) name="$2"; shift 2;;

    --install=*) install="${1#*=}"; shift 1;;

    -*) echo "unknown option: $1" >&2; exit 1;;
    *) handle_argument "$1"; shift 1;;
  esac
done

echo "Should install " ${install+x}
if [[ ! -z ${install+x} ]] ; then
    echo "Should install " ${install+x}
else
    installed_git=false
    if hash git 2>/dev/null; then
        echo 'Git already installed.'
    else
        echo "I require git but it's not installed. Installing..."
        apt-get install git -y
        ${installed_git} = true
    fi
    installed_python3=false
    if hash python3 2>/dev/null; then
        echo 'Python3 already installed.'
    else
        echo "I require python3 but it's not installed. Installing..."
        apt-get install python3 -y
        ${installed_python3} = true
    fi

    installed_pip=false
    if python3 -c "import pip" &> /dev/null; then
        echo 'Pip already installed.'
    else
        echo 'Pip not installed, installing...'
        wget https://bootstrap.pypa.io/get-pip.py

        python3 get-pip.py

        rm get-pip.py

        ${installed_pip} = true
    fi
    installed_pygame=false
    if python3 -c "import pygame" &> /dev/null; then
        echo 'Pygame already installed.'
    else
        echo 'Pygame not installed, installing...'
        python3 -m pip install pygame
        ${installed_pygame} = true
    fi
    installed_webcolors=false
    if python3 -c "import webcolors" &> /dev/null; then
        echo 'webcolors already installed.'
    else
        echo 'webcolors not installed, installing...'
        python3 -m pip install webcolors
        ${installed_webcolors} = true
    fi
    installed_wheel=false
    if python3 -c "import wheel" &> /dev/null; then
        echo 'Wheel already installed.'
    else
        echo 'Wheel not installed, installing...'
        python3 -m pip install wheel
        ${installed_wheel} = true
    fi

    if python3 -c "import wheel" &> /dev/null; then
        if python3 -c "import pygame" &> /dev/null; then
            if python3 -c "import pip" &> /dev/null; then
                if python3 -c "import webcolors" &> /dev/null; then
                    if hash python3 2>/dev/null; then
                        if hash git 2>/dev/null; then
                            installed_counter=0
                            if ${installed_git} ; then
                                ${installed_counter}++
                            fi
                            if ${installed_pip} ; then
                                ${installed_counter}++
                            fi
                            if ${installed_pygame} ; then
                                ${installed_counter}++
                            fi
                            if ${installed_python3} ; then
                                ${installed_counter}++
                            fi
                            if ${installed_wheel} ; then
                                ${installed_counter}++
                            fi
                            if ${installed_webcolors} ; then
                                ${installed_webcolors}++
                            fi

                            if [[ ! "${installed_counter}" > 0 ]] ; then
                                echo 'All dependencies already installed.'
                            else
                                if [[ "${installed_counter}" = 1 ]] ; then
                                    echo ${installed_counter} ' dependency installed'
                                else
                                    echo ${installed_counter} ' dependencies installed'
                                fi
                            fi
                        else
                            echo 'Git is missing.'
                        fi
                    else
                        echo 'Python3 is missing.'
                    fi
                else
                    echo 'webcolors is missing.'
                fi
            else
                echo 'Pip is missing.'
            fi
        else
            echo 'Pygame is missing.'
        fi
    else
        echo 'Wheel is missing.'
    fi
fi
