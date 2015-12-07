#!/bin/bash
dir=${PWD##*/}
attach=""
for var in "$@"
do
	attach="$attach""-a ""$var "
done
mutt -s "${PWD##*/}" ${attach} -- jtihrkws@sharklasers.com </dev/null
