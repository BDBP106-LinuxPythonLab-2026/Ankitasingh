#!/bin/bash
#
#checking if a file exists or not [-e]
#if [ -e ques ] ; then
     #echo "Exist"
#else 
     #echo "Do not exist"
#fi

#if [ -s 'ques' ]

#then	
	#echo "file exist and has data"
#else
	#echo "file does not exit and does not have any data"
#fi

if [ -f 'ques' ]
then 
	echo "it is a regular file"
fi
