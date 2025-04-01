#!/usr/bin/bash

# This takes files in the logfiles folder with the .log extension
# and it turns them into a compressed tar file

for file in logfiles/*.log
do 
   tar -czvf $file.tar.gz $file 
done

