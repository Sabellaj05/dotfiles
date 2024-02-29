
-- TODO: Arreglar los colores a unos mas decentes

require("catppuccin").setup({
    flavour = "mocha", -- latte, frappe, macchiato, mocha
    background = { -- :h background
        light = "latte",
        dark = "mocha",
    },
    transparent_background = false, -- disables setting the background color.
    show_end_of_buffer = false, -- shows the '~' characters after the end of buffers
    term_colors = false, -- sets terminal colors (e.g. `g:terminal_color_0`)
    dim_inactive = {
        enabled = false, -- dims the background color of inactive window
        shade = "dark",
        percentage = 0.15, -- percentage of the shade to apply to the inactive window
    },
    no_italic = false, -- Force no italic
    no_bold = false, -- Force no bold
    no_underline = false, -- Force no underline
        styles = { -- Handles the styles of general hi groups (see `:h highlight-args`):
        comments = { "italic" }, -- Change the style of comments
        conditionals = { "italic" },
    },
    color_overrides = {
        mocha = {
          --base = "#1e1e2e",
		  --mantle = "#181825",
		  --crust = "#11111b",
          text = '#94e2d5',    -- play with it
          --red = "#8839ef",
          red = "#f38ba8",
          --red = "#f07c82",
          blue = "#04a5e5",
          --blue = "#89b4fa",
          --blue = "#70a1ff",
          green = "#a6e3a1",
          --green = "#7bed9f",
          yellow = "#8839ef", -- {}
          --yellow = "#d20f39", -- {}
          --yellow = "#ffeaa7",

          sky = "#5ef1ff",
          flamingo = '#e64553', --require
          pink = "#ffacfc",

          --peach = "#e64553",
          peach = "#ffbe76",
      } 
    },
    custom_highlights = {},
    integrations = {
        cmp = true,
        gitsigns = true,
        nvimtree = true,
      --  lualine = true,   
        treesitter = true,
        notify = false,
        mini = {
            enabled = true,
            indentscope_color = "",
        },
        -- For more plugins integrations please scroll down (https://github.com/catppuccin/nvim#integrations)
    },
})

vim.cmd.colorscheme "catppuccin"
-- local mocha = require("catppuccin.palettes").get_palette "mocha"
--
--
-- Mas parametros (meter mano)
--       loops = {},
--       functions = {},
--       keywords = {},
--       strings = {},
--       variables = {},
--       numbers = {},
--       booleans = {},
--       properties = {},
--       types = {},
--       operators = {},


