
@lazy.funcion
def spawn_terminal_pwd(qtile):
    # current window
    cur_window = qtile.current_window

    if cur_window is None:
        qtile.cmd_spawn(terminal)
        return
    try:
        # get pid 
        win_pid = cur_window.window.get_pid()
        # get current working dir
        cwd = os.readlink(f'/proc/{win_pid}/cwd')
        # spawn terminal in such dir
        qtile.cmd_spawn(f'{terminal} --working-directory {cwd}')

    except Exception as e:

        print(f"Error: {e}. Spawning terminal in pwd")
        qtile.cmd_spawn(terminal)

    # Spawn new terminal on pwd
     Key([mod, "n"], "t",             spawn_terminal_pwd(), desc="Spawn new terminal in same directory"),
