
-- space key as leader
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Basic clipboard interaction
vim.keymap.set({'n', 'x'}, '<leader>y', '"+y') -- copy
vim.keymap.set({'n', 'x'}, '<leader>p', '"+p') -- paste

-- Clear search `/`
vim.keymap.set('n', '<leader>h', ':nohlsearch<CR>')

-- terminal h and v  -- wip
-- vim.keymap.set('n', '<leader>th', ':hsplit terminal')
-- vim.keymap.set('n', '<leader>tv', ':vsplit term://bash<CR>')

-- floaterm
-- vim.keymap.set('n', '<leader>ft', ':FloatermNew<CR>')
vim.keymap.set('n', '<leader>ft', ':FloatermNew<CR>')
vim.keymap.set('n', '<leader>ftr', ':FloatermNew --position=right<CR>')




