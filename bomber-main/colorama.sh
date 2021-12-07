#!/bin/bash


array=(
"""
	</> kesalahan $1
	    argumen tidak terdaftar
	     syntax $1 eror
"""
)

function bold {

if (( $? == 0 )); then
   str=${1}
 else
     str=1
 fi

case $1 in
	      hitam)setterm --foreground black --bold on ;;
	      merah)setterm --foreground red --bold on ;;
	      hijau)setterm --foreground green --bold on ;;
	      kuning)setterm --foreground yellow --bold on ;;
	      biru)setterm --foreground blue --bold on ;;
	      pink)setterm --foreground magenta --bold on ;;
	      cyan)setterm --foreground cyan --bold on ;;
	      putih)setterm --foreground white --bold on ;;
	      *)echo "${array[*]}"; exit 4
    ;;
esac
 
  
}

function normal {

if (( $? == 0 )); then
   str=${1}
 else
     str=1
 fi

case $1 in
              hitam)setterm --foreground black --bold off ;;
              merah)setterm --foreground red --bold off ;;
              hijau)setterm --foreground green --bold off ;;
              kuning)setterm --foreground yellow --bold off ;;
              biru)setterm --foreground blue --bold off ;;
              pink)setterm --foreground magenta --bold off ;;
              cyan)setterm --foreground cyan --bold off ;;
              putih)setterm --foreground white --bold off ;;
              *)echo "${array[*]}"; exit 4
    ;;
esac	
}

function stop {
	setterm --foreground default
}

function blink {
	# comming soon
	shift
}
