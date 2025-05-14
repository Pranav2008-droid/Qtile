from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import widget
from customScripts import colors
import keybindings,customWidgets


keys = keybindings.keys
theme = colors.colors

mod = "mod4"
terminal = "alacritty"
marg = 4


# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Uncomment only one of the following lines
group_labels = ["", "", "󰗃", "", "PHY", "ETC6", "ETC7", "ETC8", "ETC9"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#group_labels = ["DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX", "MISC"]
group_class = ["alacritty","firefox","surf","brave"]+["None"]*5
# The default layout for each of the 10 workspaces
group_layouts = ["Columns"]*9

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            matches=[Match(wm_class=group_class[i])]
        ))
 
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
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )
    
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=0,margin=marg),
    layout.Max(margin=marg, border_width=0),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2,border_widgth=0),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(margin=marg, border_width=0,border_color="None"),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(margin=marg, border_width=0),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=17,
    padding=3,
    foreground=theme["fg"]
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                widget.GroupBox(highlight_method="line",highlight_color=['00000000', '00000000'],this_screen_border=theme["white"],urgent_border=theme["white"]),
                widget.Sep(),
                widget.Prompt(),
                widget.WindowName(),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                #widget.StatusNotifier(),
                widget.Systray(),
                widget.Sep(),
                widget.Backlight(backlight_name = "intel_backlight",format="󰃠 :{percent}%"),
                widget.Sep(),
                widget.Redshift(),
                widget.Sep(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Sep(),
                customWidgets.BatteryWidget(update_interval=10),
                widget.Sep(),
                customWidgets.shutdown_widget,
            ],
            32,
             border_width=[0]*4,  # Draw top and bottom borders
            border_color=[theme["accent"]]*4,  # Borders are magenta
            margin = [marg,marg,0,marg],
            background="#000000"+"00",
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

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
