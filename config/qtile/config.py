import os, subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook


mod = "mod1"

@hook.subscribe.startup_once
def autostart():
    autostart_path = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([autostart_path])
    top_bar.show(False)
    top_bar2.show(False)

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
	# Go next monitor
	Key([mod], 'i', lazy.next_screen(), desc='Next monitor'),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
	# Resize layout
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("xfce4-terminal"), desc="Launch terminal"),
    Key([], "Print", lazy.spawn("import -window root "+os.path.expanduser("~/images/screenshot.jpg")), desc="Spawn screenshot"),
    Key([mod, "control"], "Return", lazy.spawn("i3lock -c 000000"), desc="i3lock lockscreen"),
    # Toggle between different layouts as defined below
    Key([mod], "t", lazy.window.toggle_fullscreen(), desc="Toogle fullscreen"),
    Key([mod], "f", lazy.next_layout(), desc="Next layout"),
	Key([mod], "b", lazy.hide_show_bar("top")),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
	Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    #volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
	]

groups = [Group(i) for i in "1234567890"]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
		]
    )

groups.append(Group("web", matches=[Match(wm_class=["firefox"])]))
keys.extend([Key([mod], "w", lazy.group["web"].toscreen(), desc="web firefox"),
		(Key([mod, "shift"], "w", lazy.window.togroup("web", switch_group=True), desc="web firefox"))])
groups.append(Group("tg", matches=[Match(wm_class=["telegram-desktop"])]))
keys.extend([Key([mod], "t", lazy.group["tg"].toscreen(), desc="web telegram"),
		(Key([mod, "shift"], "t", lazy.window.togroup("tg", switch_group=True), desc="web telegram"))])
groups.append(Group("mail", matches=[Match(wm_class=["thunderbird"])]))
keys.extend([Key([mod], "m", lazy.group["mail"].toscreen(), desc="web mail"),
		(Key([mod, "shift"], "m", lazy.window.togroup("mail", switch_group=True), desc="web mail"))])

layouts = [
	layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1),
	layout.Max(),
]

widget_defaults = dict(
    font="monospace",
    fontsize=12,
    padding=4,
)
extension_defaults = widget_defaults.copy()

bottom_bar2 = bar.Bar(
	[
		widget.GroupBox(highlight_method='line'),
		widget.CurrentScreen(padding=0),
		widget.TextBox("|", foreground="#d75f5f"),
		widget.CurrentLayout(),
		widget.Prompt(),
		widget.TextBox("|", foreground="#d75f5f"),
		widget.WindowName(),
		widget.Chord(
			chords_colors={
				"launch": ("#ff0000", "#ffffff"),
			},
			name_transform=lambda name: name.upper(),
		),
	],
	24,
)

bottom_bar = bar.Bar(
	[
		widget.GroupBox(highlight_method='line'),
		widget.CurrentScreen(padding=0),
		widget.TextBox("|", foreground="#d75f5f"),
		widget.CurrentLayout(),
		widget.Prompt(),
		widget.TextBox("|", foreground="#d75f5f"),
		widget.WindowName(),
		widget.Chord(
			chords_colors={
				"launch": ("#ff0000", "#ffffff"),
			},
			name_transform=lambda name: name.upper(),
		),
		widget.Systray(padding=0),
		widget.TextBox("|", foreground="#d75f5f", padding=0),
		widget.DF(visible_on_warn=False),
		widget.TextBox("|", foreground="#d75f5f", padding=0),
		widget.Memory(measure_mem="G", padding=0),
		widget.TextBox("|", foreground="#d75f5f", padding=0),
		widget.CPU(padding=0),
		widget.TextBox("|", foreground="#d75f5f", padding=0),
		widget.Clock(format="%Y-%m-%d %a %I:%M%p", padding=0),
		widget.TextBox("|", foreground="#d75f5f", padding=0),
		widget.Volume(padding=0),
		widget.TextBox("|", foreground="#d75f5f", padding=0),
		widget.QuickExit(default_text="[X]", countdown_format="[{}]", padding=0),
	],
	24,
)
top_bar = bar.Bar(
	[
		widget.TaskList(padding=0),
	],
	20,
)
top_bar2 = bar.Bar(
	[
		widget.TaskList(padding=0),
	],
	20,
)
screens = [
    Screen(
		bottom=bottom_bar,
		top=top_bar,
        #background image
        wallpaper="/home/alexander/images/fon.jpeg",
		wallpaper_mode="stretch",
    ),
	Screen(
		bottom=bottom_bar2,
		top=top_bar2,
        wallpaper="/home/alexander/images/fon2.jpeg",
		wallpaper_mode="stretch",
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
follow_mouse_focus = False
bring_front_click = False
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

auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"
