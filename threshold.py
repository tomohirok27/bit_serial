import sys
import argparse
from tqdm import tqdm
import torch
import torch.nn as nn
import numpy as np
import os
import pandas as pd
import utils





def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--prominent', type=str, default='entropy')
    parser.add_argument('-dn', '--data_npy', type=int, default=0)
    parser.add_argument('-sn', '--sort_npy', type=int, default=0)
    parser.add_argument('-pc', '--plt_cum', type=str, default=True)
    parser.add_argument('-pe', '--plt_entropy', type=str, default=True)
    parser.add_argument('-tt', '--train_th', type=float, default=0.99)

    return parser.parse_args()

def npy_loader():
    if args.prominent == 'entropy':
        if args.data_npy:
            if args.data_npy == 1:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2230_resnet18_cifar100_ser8_9_h1_200904_1710.npy'
            elif args.data_npy == 2:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2233_resnet18_cifar100_ser8_9_h2_200909_1533.npy'
            elif args.data_npy == 3:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2235_resnet18_cifar100_ser8_9_h3_200909_1752.npy'
            elif args.data_npy == 4:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2238_resnet18_cifar100_ser8_9_h4_200909_1730.npy'
            elif args.data_npy == 5:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2241_resnet18_cifar100_ser8_9_h5_200909_1718.npy'
            elif args.data_npy == 6:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2243_resnet18_cifar100_ser8_9_h6_200909_1707.npy'
            elif args.data_npy == 7:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2246_resnet18_cifar100_ser8_9_h7_200909_1656.npy'
            elif args.data_npy == 8:
                data_file = '/artic/t-kaneko/work/bit_serial/numpy/data/201207/201207_2249_resnet18_cifar100_ser8_9_h8_200909_1644.npy'
            filename = utils.numpy_save(sort, data_file, 'sort')
            all_value = np.load('%s.npy' % filename)
            sort = np.zeros_like(all_value)
            sort = all_value[:, np.argsort(all_value[0])]
        if args.sort_npy:
            if args.sort_npy == 1:
                filename = '201208_0001_201207_2230_resnet18_cifar100_ser8_9_h1_200904_1710'
            elif args.sort_npy == 2:
                filename = '201208_0001_201207_2233_resnet18_cifar100_ser8_9_h2_200909_1533'
            elif args.sort_npy == 3:
                filename = '201208_0001_201207_2235_resnet18_cifar100_ser8_9_h3_200909_1752'
            elif args.sort_npy == 4:
                filename = '201208_0001_201207_2238_resnet18_cifar100_ser8_9_h4_200909_1730'
            elif args.sort_npy == 5:
                filename = '201208_0001_201207_2241_resnet18_cifar100_ser8_9_h5_200909_1718'
            elif args.sort_npy == 6:
                filename = '201208_0001_201207_2243_resnet18_cifar100_ser8_9_h6_200909_1707'
            elif args.sort_npy == 7:
                filename = '201208_0001_201207_2246_resnet18_cifar100_ser8_9_h7_200909_1656'
            elif args.sort_npy == 8:
                filename = '201208_0001_201207_2249_resnet18_cifar100_ser8_9_h8_200909_1644'
            sort = np.load('/artic/t-kaneko/work/bit_serial/numpy/sort/201208/%s.npy' % filename)

    return filename, sort


if __name__ == '__main__':
    args = parse_args()

    filename, sort = npy_loader()
    cum =  np.zeros_like(sort)
    # cum[0] = sort[0]
    cum[1] = np.cumsum(sort[1])
    cum[2] = np.cumsum(sort[2])
    correct_rate = np.empty(0)
    for i, (x, y) in enumerate(zip(cum[1], cum[2])):
        r = x / (x + y)
        correct_rate = np.append(correct_rate, r)
        if r > args.train_th:
            key = i
            ratio = r
    if args.plt_cum:
        utils.plt_cum(cum[1], cum[2], correct_rate, 'frequency', filename, key, ratio, sort[0][key], args.train_th)
    
    if args.plt_entropy:
        utils.plt_number_entropy(sort, 'entropy', filename)
    # breakpoint()

    if args.data_npy == 1 or args.sort_npy == 1:
        print('1bit: %s' % sort[0][key])
    else:
        print('%sbit: %s' % (args.data_npy or args.sort_npy, sort[0][(np.where(sort[2]==1)[0][0])]))