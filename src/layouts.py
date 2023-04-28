LAYOUTS = [
	{
		"label": "Bottom panel",
		"icon": "bottom_panel",
		"enable_extensions":  [
			"dash-to-panel@jderose9.github.com",
			"nyarcmenu@nyarchlinux.moe"
		],
		"disable_extensions": [
			"dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com"
		],
		"extra_commands": [],
	},
	{
		"label": "Gnome",
		"icon": "gnome-layout",
		"enable_extensions":  [
		],
		"disable_extensions": [
			"dash-to-panel@jderose9.github.com",
			"nyarcmenu@nyarchlinux.moe",
			"dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com"
		],
		"extra_commands": [],
	},
	{
		"label": "Top panel with menu",
		"icon": "top_bar_with_menu",
		"enable_extensions":  [
			"nyarcmenu@nyarchlinux.moe"
		],
		"disable_extensions": [
			"dash-to-panel@jderose9.github.com",
			"dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com"
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com/schemas set org.gnome.shell.extensions.dash-to-dock-pop dock-position BOTTOM"
		],
	},
	{
		"label": "Top panel with menu and dock",
		"icon": "top_bar_menu_dock",
		"enable_extensions":  [
			"nyarcmenu@nyarchlinux.moe",
			"dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com"
		],
		"disable_extensions": [
			"dash-to-panel@jderose9.github.com",
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com/schemas set org.gnome.shell.extensions.dash-to-dock-pop dock-position BOTTOM"
		],
	},
	{
		"label": "Top panel with dock",
		"icon": "top_bar_dock",
		"enable_extensions":  [
			"dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com"
		],
		"disable_extensions": [
			"dash-to-panel@jderose9.github.com",
			"nyarcmenu@nyarchlinux.moe"
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com/schemas set org.gnome.shell.extensions.dash-to-dock-pop dock-position BOTTOM"
		],
	},
	{
		"label": "Top panel with left dock",
		"icon": "top_bar_dock",
		"enable_extensions":  [
			"nyarcmenu@nyarchlinux.moe"
			"dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com"
		],
		"disable_extensions": [
			"dash-to-panel@jderose9.github.com",
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/dash-to-dock-cosmic-@halfmexicanhalfamazing@gmail.com/schemas set org.gnome.shell.extensions.dash-to-dock-pop dock-position LEFT"
		],
	}
]

COLORS = {"#643f00": 0xffbc9769, "#005142": 0xffdafaef, "#722b65": 0xffdcabcc, "#00497e": 0xffd1e1f8, "#225104": 0xff7d916e, "#004397": 0xff4285f4, "#7c2c1b": 0xffb18c84, "#00504e": 0xff7ca7a5, "#403c8e": 0xffb7b4cf, "#3d4c00": 0xffb0b78e, "#64307c ": 0xff8e7596, "#005137 ": 0xff9bb8a8, "#4e4800": 0xfff0eab7}
