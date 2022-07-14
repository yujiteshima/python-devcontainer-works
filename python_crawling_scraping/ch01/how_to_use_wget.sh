#!/bin/bash
# wget http://gihyo.jp/assets/templates/gihyojp2007/image/gihyo_logo.png
# wget http://gihyo.jp
# wget http://gihyo.jp/ -O gihyo_top.html
wget -r --no-parent -w 1 -l 1 --restrict-file-names=nocontrol https://gihyo.jp/dp/