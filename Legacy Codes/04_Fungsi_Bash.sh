#!/bin/bash

luas() {
	x=$1
	y=$2
	let z=$x*$y
	echo $z
}

echo "Masukkan Panjang : "
read panjang
echo "Masukkan Lebar : "
read lebar

printf "\n"
echo "Luas Persegi : "
luas $panjang $lebar
