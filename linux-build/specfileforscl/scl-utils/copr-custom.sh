#!/bin/sh -x
if [ -f /etc/fedora-release ]; then
OS="Fedora"
VER=$(rpm -E %fedora)
elif [ -f /etc/centos-release ]; then
OS=$(source /etc/os-release; echo ${NAME})
VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/centos-release)
VER=${VERFULL:0:1} # return 8
elif [ -f /etc/almalinux-release ]; then
OS=$(source /etc/os-release; echo ${NAME})
VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/almalinux-release)
VER=${VERFULL:0:1} # return 8
elif [ -f /etc/rocky-release ]; then
OS=$(source /etc/os-release; echo ${NAME})
VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/rocky-release)
VER=${VERFULL:0:1} # return 8
else
OS=$(source /etc/os-release; echo ${NAME})
VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/redhat-release)
VER=${VERFULL:0:1} # return 8
fi
#for change git comment this start
if [ "$OS" = "Fedora" ] ; then
wget https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/scl-utils/scl-utils-Fedora.spec -O scl-utils.spec
else
wget https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/scl-utils/scl-utils-el-$VER.spec -O scl-utils.spec
fi
#for change git comment this stop here
#for change git uncomment this start
#if [[ "$OS" = "Fedora" ]] ; then
#wget https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/linux-build/specfileforscl/scl-utils/scl-utils-Fedora.spec -O scl-utils.spec
#else
#wget https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/linux-build/specfileforscl/scl-utils/scl-utils-el-$VER.spec -O scl-utils.spec
#fi
#for change git uncomment this stop here
