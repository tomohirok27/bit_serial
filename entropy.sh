#!/bin/bash

W8='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h8_200909_1644.pth'
W7='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h7_200909_1656.pth'
W6='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h6_200909_1707.pth'
W5='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h5_200909_1718.pth'
W4='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h4_200909_1730.pth'
W3='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h3_200909_1752.pth'
W2='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h2_200909_1533.pth'
W1='/work/j-suzuki/weight/different_fn/resnet18_cifar100_ser8_9_h1_200904_1710.pth'

for i in `seq 8`
do
    num="W${i}"
    eval weight='$'${num}
    echo $weight
    python3 entropy.py -m resnet18 -d cifar100 -df True -w $weight -hb $i -p entropy 
done