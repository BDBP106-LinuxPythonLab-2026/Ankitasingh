#!/bin/bash
#
#
echo "Enter a Number"
read n
i=1
until [ $i -gt 15 ]
do
	result=$((n*i))
	echo "$n x $i = $result"
	i=$[i+1]
done

