#!/bin/bash

echo "MUHAMMAD RAFLY - 19081010018"
echo " "
echo "Uang Anda : "
read uang
echo "Harga barang yang dibeli"
read harga

if [ $uang == $harga ]
then
	echo "Uang Anda pas"
elif [ $uang -gt $harga ]
then
	let kembali=$uang-$harga
	echo "Uang Anda kembali $kembali"
elif [ $uang -lt $harga ]
then
	let kurang=$harga-$uang
	echo "Uang Anda kurang $kurang"
fi

