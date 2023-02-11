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
