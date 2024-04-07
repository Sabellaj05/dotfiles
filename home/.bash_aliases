#>>>>> Terminal >>>>>

## ls stuff
alias lsx='exa -la --icons -h'
alias ls='exa -l --icons -h --group-directories-first'
alias lxs='exa --icons'
alias lxd='exa -a --icons --group-directories-first'

## clipboard thingy
alias xcp='xclip -sel c'

## cd's
alias ..='cd ..'
alias ...='cd ../..'

#>>>> Software >>>>

## zathura remove terminal
alias ztr='nohup zathura'
## fulL HACKER
alias neo='cmatrix -C blue'

## git
alias gst='git status'
alias glo='git log --oneline'

## neovim
alias vim='nvim'

## jupyter 
alias jpn='jupyter notebook --no-browser'
alias jpl='jupyter lab --no-browser'

## Cursor from the command line
alias cursor='/opt/cursor.appimage'

#>>>> OS >>>>
## Windows C Drive
alias win-c='cd /media/don/9EEE3C3BEE3C0DD1/Users/manum/'

## Windows D Drive
alias win-d='cd /media/don/Discardo/'

## Linux version
alias linuxv='lsb_release -a'
alias linuxinfo='uname -m && cat /etc/*release'
alias linuxkernel='uname -srmv'
