#>>>>> Terminal >>>>>

## ls stuff
alias lsx='exa -la --icons -h'
alias ls='exa -l --icons -h --group-directories-first'
alias lxs='exa --icons'
alias lxd='exa -a --icons --group-directories-first'

## Clipboard thingy
alias xcp='xclip -sel c'

## cd's
alias ..='cd ..'
alias ...='cd ../..'

#>>>> Software >>>>

## zathura remove terminal
alias ztr='nohup zathura'
## FULL HACKER
alias neo='cmatrix -C blue'

## Git
alias gst='git status'
alias glo='git log --oneline'

## Neovim
alias vim='nvim'

## Jupyter 

alias jpn='jupyter notebook --no-browser'
alias jpl='jupyter lab --no-browser'



#>>>> OS >>>>
## C Drive
alias c-docs='cd /media/don/9EEE3C3BEE3C0DD1/Users/manum/Documents'

## Linux version
alias linuxv='lsb_release -a'
alias linuxinfo='uname -m && cat /etc/*release'
alias linuxkernel='uname -srmv'
