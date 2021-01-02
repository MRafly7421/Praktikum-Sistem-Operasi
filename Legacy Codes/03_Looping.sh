#!/bin/bash

echo "Masukkan Nilai maks : "
read nilai

echo "Output : "
for ((i=nilai; i>=1; i=i-2))
do
	echo $i
done
