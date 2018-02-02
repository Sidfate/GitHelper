# !/usr/bin/env python
# encoding: utf-8
from config_helper import ConfigHelper
from git_helper import GitHelper
import argparse
import sys


class Core:
    config_template = """
name=%s    
root_dir=%s
from_branch=%s
to_branch=%s
"""

    def __init__(self):
        self.config = ConfigHelper()

        parser = argparse.ArgumentParser(prog='ghelp', usage='%(prog)s [--version] [-c namespace] [namespace]')
        parser.add_argument('namespace', nargs='*', help='execute namespace\'s action')
        parser.add_argument('-c', '--config', nargs='*', help='config handler')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')

        self.parser = parser
        self.args = self.parser.parse_args()
        print(self.args)

    def execute(self):
        if self.args.namespace is not None:
            config = self.get_config(self.args.namespace[0])
            config['comment'] = self.args.namespace[1]
            git_helper = GitHelper(config['root_dir'])
            git_helper.push_remote(**config)
            self.end('Finished!')

    def config_handler(self):
        if self.args.config is None:
            return
        arg_len = len(self.args.config)
        if arg_len is 0:
            all_config = self.get_config()
            self.end('\n'.join(self.config_format(all_config[i]) for i in all_config))
        elif arg_len > 1:
            print('config 参数大于1')

        namespace = self.args.config[0]
        config = self.get_config(namespace)
        if config is None:
            root_dir = input("Input namespace's root directory:")
            from_branch = input("Input the local raw branch:")
            to_branch = input("Input the origin target branch:")
            self.add_config(namespace=namespace, root_dir=root_dir, from_branch=from_branch, to_branch=to_branch)
            self.end('\ncreate config success.')
        self.end(self.config_format(config))

    def config_format(self, config):
        return self.config_template % (
            config['namespace'],
            config['root_dir'],
            config['from_branch'],
            config['to_branch']
        )

    def get_config(self, namespace=None):
        return self.config.get(namespace)

    def add_config(self, **kwargs):
        self.config.save(**kwargs)

    def parse(self):
        self.execute()
        self.config_handler()
        pass

    @staticmethod
    def end(text):
        print(text)
        sys.exit()


if __name__ == '__main__':

    core = Core()
    core.parse()
