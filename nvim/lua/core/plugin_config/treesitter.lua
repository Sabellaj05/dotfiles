require('nvim-treesitter.configs').setup {
    -- A list of parser names, or "all"
    ensure_installed = { "c",
                        "lua",
                        "rust",
                        "python",
                        "vim",
                        "bash",
                        "markdown", },
    
    -- Install parsers synchronously (only apllied to 'ensure installed')
    sync_install = false,
    auto_install = true,
    highligh = {
        enable = true,
    },
}
