#!/bin/bash

# setup some shell values and stuff I like

. conf.sh

setup_vim ()
{
    # install vim, remove vi, sym-link vi -> vim, setup default .vimrc

    # actually install vim
    $manager -y install vim
    if [[ $? -gt 0 ]];
    then
        echo "[X] Problem installing vim.. manually install!"
        exit 1
    fi

    # remove vi, ugh
    if [[ -e "/usr/bin/vi" ]];
    then
        rm -f "/usr/bin/vi"
    fi
    # add sym-link from vi -> vim
    ln -s "/usr/bin/vim" "/usr/bin/vi"

    # setup .vimrc to use spaces b/c why would you use tabs?? lol
    if [[ ! -e ~/.vimrc ]];
    then
        touch ~/.vimrc
    fi
    # probs a better way but i'm just whippin this up
    echo "syntax on" >> ~/.vimrc
    echo "set tabstop=4" >> ~/.vimrc
    echo "set shiftwidth=4" >> ~/.vimrc
    echo "set expandtab" >> ~/.vimrc

}

setup_shellrc ()
{
    # maybe add more stuff eventually.. setup vim-shell navigation

    # use vim-shell navigation, not emacs
    echo "set -o vi" >> ~/$shellrc

}

if [[ $UID -gt 0 ]];
then
    echo "[X] Must run script as root!"
    exit 1
fi

setup_vim
setup_shellrc
