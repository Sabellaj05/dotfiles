# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import os
import subprocess

# esto sirve para aplicar la funcion al hacer un qtile restart
#@hook.subscribe.startup

# Esta solo la primera vez que qtile starts
#@hook.subscribe.startup_once

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/scripts/autostart.sh')
    subprocess.Popen([home])     ## No es lo mas comun pero asi funca bien

@lazy.function
def minimize_all(qtile):
    '''
    Function para minimizar todas las ventanas
    del grupo en el cual estamos Ex '3'.
    Agregar keybind dentro del grupos `Keys` line: 62
    Current line of keybind: 85
    - Por alguna razon no viene una funcion ya hecha para esto
    '''
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Minimize all windows
    Key([mod], "m", minimize_all(), desc="Toggle minimization on all window"),
    #Rofi launcher
    Key([mod, "shift"], "r", lazy.spawn("rofi -show drun")),

    # Flameshot
    Key([], "Print", lazy.spawn("flameshot gui --clipboard --path /home/don/Pictures/Screenshots")),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

#group_label: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
   # main
    layout.Columns(
        border_focus_stack=["#74c7ec", "#fab387"],
        border_focus=["#74c7ec"],
        border_width= 3
        ),

    layout.MonadTall(border_focus_stack=["#74c7ec", "#fab387"],
        border_focus=["#74c7ec"],
        border_width= 3),

    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
     layout.Bsp(border_focus_stack=["#74c7ec", "#fab387"],
        border_focus=["#74c7ec"],
        border_width= 3),
    # layout.Matrix(),
     
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# pegarle una ojeada a esto tal vez sea clave para el tema de los iconos
widget_defaults = dict(
    #font="sans",
    font="JetBrains Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Image(
                    filename='~/.config/qtile/Assets/launch_icon.png',
                    scale="False"
                    ),
                #widget.Prompt(),         #mod+r el old rofi
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#74c7ec", "#89dceb"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # Pomodoro parameters: 
                # https://docs.qtile.org/en/latest/manual/ref/widgets.html#pomodoro
                widget.Pomodoro(color_active="#a6e3a1",
                                color_inactive="#f38ba8",
                                length_long_break=15,
                                length_pomodori=25,
                                length_short_break=5,
                                num_pomodori=4,
                                prefix_inactive="Pomodoro",
                                prefix_long_break="LB ",
                                prefix_paused="Pause",
                                font='JetBrains Mono',
                                ), ## twekear 

                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                #widget.StatusNotifier(),
                widget.Systray(),
                #widget.CPUGraph(),
                widget.CPU(),
               #wigget.Sep(padding=4, linewdith=5),
                widget.Memory(fmt="RAM{}", measure_mem="M"),
               #widget.Sep(),
                #widget.Net(format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}", interface="enp3s0"),
                widget.NetGraph(type='line', line_width=1),
                #widget.Clock(format="%d-%m-%Y %a %I:%M %p"),
                widget.Clock(format="%d-%m-%Y %I:%M"),
               # widget.QuickExit(), para apagar
            ],
            #24,
            26,
            #background=[ "#1e1e2e66","#585b7066"],
            #background=["#585b7066" ,"#1e1e2e66"],  Nice
            #background = "#31324466",
            background ="#24273a",
            #color="#74c7ec",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "Qtile"
