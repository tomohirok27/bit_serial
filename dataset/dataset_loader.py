"""" data loader """ ""

import os
import sys
import torch
import torchvision
import torchvision.transforms as transforms
import random


def dataset_loader(dataset="None",
                   train_batch=128,
                   test_batch=100,
                   num_worker=2):
    random.seed(1)
    return eval(dataset + '_loader')(train_batch, test_batch, num_worker)
    # if dataset == "cifer10":
    #     return cirfer10_loader()
    # if dataset == "cifer100":
    #     return cirfer100_loader()

    # else:
    #     print("no such dataset!!!")
    #     print("no such dataset!!!")
    #     sys.exit(1)


def cifar10_loader(train_batch=128, test_batch=100, num_workers=2):
    """ cifer10 loader """
    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010))
        # transforms.Normalize((0.424, 0.415, 0.384), (0.283, 0.278, 0.284))
    ])
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010))
        # transforms.Normalize((0.424, 0.415, 0.384), (0.283, 0.278, 0.284))
    ])

    dir_path = os.path.dirname(__file__) + '/data'
    # print(dir_path)

    train_dataset = torchvision.datasets.CIFAR10(root=dir_path,
                                                 train=True,
                                                 transform=train_transform,
                                                 download=True)
    test_dataset = torchvision.datasets.CIFAR10(root=dir_path,
                                                train=False,
                                                transform=test_transform,
                                                download=True)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=train_batch,
                                               shuffle=True,
                                               num_workers=num_workers)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=test_batch,
                                              shuffle=False,
                                              num_workers=num_workers)
    # breakpoint()

    return train_loader, test_loader


def cifar100_loader(train_batch=128, test_batch=128, num_workers=2):
    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        # transforms.Normalize((0.438, 0.418, 0.377), (0.300, 0.287, 0.294))
        transforms.Normalize((0.5071, 0.4867, 0.4408),
                             (0.2675, 0.2565, 0.2761))
    ])

    test_transform = transforms.Compose([
        transforms.ToTensor(),
        # transforms.Normalize((0.438, 0.418, 0.377), (0.300, 0.287, 0.294))
        transforms.Normalize((0.5071, 0.4867, 0.4408),
                             (0.2675, 0.2565, 0.2761))
    ])

    dir_path = os.path.dirname(__file__) + '/data'

    train_dataset = torchvision.datasets.CIFAR100(root=dir_path,
                                                  train=True,
                                                  transform=train_transform,
                                                  download=True)
    test_dataset = torchvision.datasets.CIFAR100(root=dir_path,
                                                 train=False,
                                                 transform=test_transform,
                                                 download=True)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=train_batch,
                                               shuffle=True,
                                               num_workers=num_workers)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=test_batch,
                                              shuffle=False,
                                              num_workers=num_workers)

    return train_loader, test_loader

def imagenet_loader(train_batch=128, test_batch=100, num_workers=2):
    """ ImageNet loader """
    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))
        # transforms.Normalize((0.424, 0.415, 0.384), (0.283, 0.278, 0.284))
    ])
    test_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))
        # transforms.Normalize((0.424, 0.415, 0.384), (0.283, 0.278, 0.284))
    ])

    # dir_path = os.path.dirname(__file__) + '/data'
    # print(dir_path)
    dir_path = '../../Shared/Datasets/ILSVRC'

    train_dataset = torchvision.datasets.ImageFolder(root=dir_path,
                                                transform=train_transform
                                                )
    test_dataset = torchvision.datasets.ImageFolder(root=dir_path,
                                                transform=test_transform
                                                )

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=train_batch,
                                               shuffle=True,
                                               num_workers=num_workers)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=test_batch,
                                              shuffle=False,
                                              num_workers=num_workers)
    # breakpoint()
    # for i, (images, labels) in enumerate(train_loader):
    #     print(labels.size())

    return train_loader, test_loader