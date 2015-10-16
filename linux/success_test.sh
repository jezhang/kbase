#!/bin/bash
# file name:success_test.sh
CMD='ls'
status
$CMD
if [ $? -eq 0 ];
then
	echo "$CMD executed successfully"
else
	echo "$CMD terminated unsuccessfully"
fi