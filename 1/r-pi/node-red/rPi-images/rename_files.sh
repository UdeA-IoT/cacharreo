#!/bin/bash
i=0
for f in 2023*; do
	i=$(($i+1))
	# echo ${i}
	cp "$f" "rPi_capture-${i}"
done
rm 2023*

