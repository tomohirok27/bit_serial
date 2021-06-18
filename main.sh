#!/bin/bash

python3 main.py   --lr 0.0001 -e 60 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 1 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 60 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 2 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 20 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 3 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 20 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 4 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 20 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 5 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 20 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 6 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 20 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 7 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True
python3 main.py   --lr 0.0001 -e 20 -d cifar100 -m vgg16 --weights /artic/t-kaneko/work/bit_serial/weights/vgg16_cifar100_ser_8/vgg16_cifar100_ser_8_210113/vgg16_cifar100_ser_8_210113_1853.pth --csv True --writer True -sw True --high_bits 8 -cfn out_2101132117_vgg16_cifar100_ser_8h.csv -df True


# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 1
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 2
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 3
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 4
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 5
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 6
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 7
# python3 main.py  --lr 0.001 -m resnet18 --weights weights/resnet18_cifar100_ser_8/resnet18_cifar100_ser_8_201206/resnet18_cifar100_ser_8_201206_1623.pth --csv True --writer True -sw True -df True --high_bits 8





# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 7
# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 6
# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 5
# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 4
# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 3
# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 2
# python3 main.py  --lr 0.001 -m vgg11 --weights weights/vgg11_cifar100_ser_8/vgg11_cifar100_ser_8_201117/vgg11_cifar100_ser_8_201117_2340.pth --csv True --writer True -sw True -df True --high_bits 1

