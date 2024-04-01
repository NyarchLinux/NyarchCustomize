DASH_TO_DOCK_UUID = "dash2dock-lite@icedman.github.com"
DASH_TO_DOCK_SCHEMA = "org.gnome.shell.extensions.dash2dock-lite"
ARCMENU_UUID = "arcmenu@arcmenu.com"
DASH_TO_PANEL_UUID = "dash-to-panel@jderose9.github.com"


LAYOUTS = [
	{
		"label": "Bottom panel",
		"icon": "bottom_panel",
		"enable_extensions":  [
			DASH_TO_PANEL_UUID,
			ARCMENU_UUID
		],
		"disable_extensions": [
			DASH_TO_DOCK_UUID
		],
		"extra_commands": [],
	},
	{
		"label": "Gnome",
		"icon": "gnome-layout",
		"enable_extensions":  [
		],
		"disable_extensions": [
			DASH_TO_PANEL_UUID,
			ARCMENU_UUID,
			DASH_TO_DOCK_UUID
		],
		"extra_commands": [],
	},
	{
		"label": "Top panel with menu",
		"icon": "top_bar_with_menu",
		"enable_extensions":  [
			ARCMENU_UUID
		],
		"disable_extensions": [
			DASH_TO_PANEL_UUID,
			DASH_TO_DOCK_UUID
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + DASH_TO_DOCK_UUID + "/schemas set " + DASH_TO_DOCK_SCHEMA + " dock-location 0"
		],
	},
	{
		"label": "Top panel with menu and dock",
		"icon": "top_bar_menu_dock",
		"enable_extensions":  [
			ARCMENU_UUID,
			DASH_TO_DOCK_UUID
		],
		"disable_extensions": [
			DASH_TO_PANEL_UUID,
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + DASH_TO_DOCK_UUID + "/schemas set " + DASH_TO_DOCK_SCHEMA + " dock-location 0"
		],
	},
	{
		"label": "Top panel with dock",
		"icon": "top_bar_dock",
		"enable_extensions":  [
			DASH_TO_DOCK_UUID
		],
		"disable_extensions": [
			DASH_TO_PANEL_UUID,
			ARCMENU_UUID
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + DASH_TO_DOCK_UUID + "/schemas set " + DASH_TO_DOCK_SCHEMA + " dock-location 0"
		],
	},
	{
		"label": "Top panel with left dock",
		"icon": "top_bar_dock",
		"enable_extensions":  [
			ARCMENU_UUID,
			DASH_TO_DOCK_UUID
		],
		"disable_extensions": [
			DASH_TO_PANEL_UUID,
		],
		"extra_commands": [
			"gsettings --schemadir ~/.local/share/gnome-shell/extensions/" + DASH_TO_DOCK_UUID + "/schemas set " + DASH_TO_DOCK_SCHEMA + " dock-location 1"
		],
	}
]

COLORS = {"#643f00": 0xffbc9769, "#005142": 0xffdafaef, "#722b65": 0xffdcabcc, "#00497e": 0xffd1e1f8, "#225104": 0xff7d916e, "#004397": 0xff4285f4, "#7c2c1b": 0xffb18c84, "#00504e": 0xff7ca7a5, "#403c8e": 0xffb7b4cf, "#3d4c00": 0xffb0b78e, "#64307c ": 0xff8e7596, "#005137 ": 0xff9bb8a8, "#4e4800": 0xfff0eab7}

