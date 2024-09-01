#!/bin/bash

APPDIR=/opt
APPIMAGE_URL="https://downloader.cursor.sh/linux/appImage/x64"

wget -O $APPDIR/cursor.appimage $APPIMAGE_URL
chmod +x $APPDIR/cursor.appimage
