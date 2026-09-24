#!/bin/bash
#
#
function divide {
	local a=$1
	local b=$2
        if [ $b -eq 0]
        then
	   echo "Cannot divide by 0"
	   return
        fi
