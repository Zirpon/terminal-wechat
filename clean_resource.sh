#!/bin/sh

ls -l ./resource/*.gif | awk -F' ' '{cmd="rm -f "$9;print $9;if($5 == 0)system(cmd);}'
echo "resouce gif Left:"
ls -l ./resource/*.gif | awk -F' ' '{if($5 == 0)print $9;}'
