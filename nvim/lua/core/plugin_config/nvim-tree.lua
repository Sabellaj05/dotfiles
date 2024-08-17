vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

require("nvim-tree").setup({
  view = {
    width = 30,
    side = 'right',
  --hide_root_folder = true,
    number = true,
    relativenumber = true,

  }
})

vim.keymap.set('n', '<c-n>', ':NvimTreeFindFileToggle<CR>')
vim.keymap.set('n', '<c-n>', ':NvimTreeFindFileToggle<CR>')
