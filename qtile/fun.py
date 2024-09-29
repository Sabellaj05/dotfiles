@lazy.funcion
def spawn_terminal_pwd(qtile):
    # current window
    try:
        # get current working dir
        cwd = os.getcwd()
        # spawn terminal in such dir
        qtile.cmd_spawn(f'{terminal} --working-directory {cwd}')

    except Exception as e:

        print(f"Error: {e}. Spawning terminal in pwd")
        qtile.cmd_spawn(terminal)

    # Spawn new terminal on pwd
     Key([mod, "n"], "t",             spawn_terminal_pwd(), desc="Spawn new terminal in same directory"),
