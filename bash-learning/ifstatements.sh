#!/usr/bin/bash

mynum=300

if [ $mynum -eq 200 ] #! reverses the check # -ne is not equal -eq is equal to  -gt is greater than 
then
    echo "The condition is true"
else
    echo "the variable does not equal 200"
fi
#backwards if just basically says im done (instead of curly brackets {})
