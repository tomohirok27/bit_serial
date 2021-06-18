#!/bin/bash

W8='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2249_resnet18_cifar100_ser8_9_h8_200909_1644.npy'
W7='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2246_resnet18_cifar100_ser8_9_h7_200909_1656.npy'
W6='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2243_resnet18_cifar100_ser8_9_h6_200909_1707.npy'
W5='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2241_resnet18_cifar100_ser8_9_h5_200909_1718.npy'
W4='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2238_resnet18_cifar100_ser8_9_h4_200909_1730.npy'
W3='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2235_resnet18_cifar100_ser8_9_h3_200909_1752.npy'
W2='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2233_resnet18_cifar100_ser8_9_h2_200909_1533.npy'
W1='/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2230_resnet18_cifar100_ser8_9_h1_200904_1710.npy'

for i in `seq 8`
do
    num="W${i}"
    eval weight='$'${num}
    echo $weight
    python3 threshold.py -p entropy -dn 0 -sn $i -tt 0.99 -pc False -pe False 
done