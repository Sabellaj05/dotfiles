
-- space key as leader
vim.g.mapleader = " "
vim.g.maplocalleader = " " 

-- Basic clipboard interaction
vim.keymap.set({'n', 'x'}, '<leader>y', '"+y') -- copy
vim.keymap.set({'n', 'x'}, '<leader>p', '"+p') -- paste

-- Clear search `/`
vim.keymap.set('n', '<leader>h', ':nohlsearch<CR>')



