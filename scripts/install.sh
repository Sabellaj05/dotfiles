#!/bin/bash

# WIP, not tested yet also stolen

copy(){
  cp -rp "$1" "$2"
  echo "Copied $1 to $2"
}

# get .bashrc from my repos ( revisar )
curl -O https://raw.githubusercontent.com/Sabellaj05/dotfiles/home/.bashrc

# copy home files
for f in .*; do
  # if file and not .git/
  [[ -f $f && $f != '.git' ]] && {
    # if file exist
    if [[ -f ~/$f ]]; then
      read -rp "Overwrite ~/$f with $f? [y/N]: "
      [[ ${REPLY,,} =~ y(es)? ]] && copy "$f" ~/
    else
      copy "$f" ~/
    fi
  }
done

# copy .config files
for f in .config/*; do
  # if file/directory exist
  if [[ -e ~/$f ]]; then
    read -rp "Overwrite ~/$f with $f? [y/N]: "
    [[ ${REPLY,,} =~ y(es)? ]] && copy "$f" ~/.config/
  else
    copy "$f" ~/.config/
  fi
done
