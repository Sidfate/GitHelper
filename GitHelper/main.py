# !/usr/bin/env python
# encoding: utf-8
from config_helper import ConfigHelper
import argparse


class CommandHelper:
    def __init__(self):
        self.config = ConfigHelper()

        pass

    def config_handler(self):
        print(111)

    def get_config(self):
        print(self.config.get())

    def init_argv(self):
        pass


if __name__ == '__main__':

    command = CommandHelper()

    parser = argparse.ArgumentParser()
    parser.add_argument('config', help='the config')
    # parser.add_argument('--val', required=True, help='path to dataset')
    # parser.add_argument('--total', type=int, help='number of dataset', default=100)
    # parser.add_argument('--lr', type=float, default=0.01, help='learning rate')
    args = parser.parse_args()

    print(args.config)
    pass