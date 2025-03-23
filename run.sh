#!/bin/bash
APPID="moe.nyarchlinux.customize"
git add *
git commit -m "temp"
flatpak-builder --install --user --force-clean flatpak-app "$APPID".json
git reset --soft HEAD~1
flatpak run $APPID