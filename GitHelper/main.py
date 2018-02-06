# !/usr/bin/env python
# encoding: utf-8
from GitHelper.config_helper import ConfigHelper
from GitHelper.git_helper import GitHelper
import argparse
import sys


class Core:
    config_template = """\
[%s]    
root_dir=%s
from_branch=%s
to_branch=%s
"""

    def __init__(self):
        self.config = ConfigHelper()
        self.parser = self.init_parser()
        self.args = self.parser.parse_args()

    def execute(self):
        if self.args.namespace is not None and len(self.args.namespace) > 0:
            config = self.get_config(self.args.namespace[0])
            config['comment'] = self.args.namespace[1] if len(self.args.namespace) > 1 else 'update'
            git_helper = GitHelper(config['root_dir'])
            git_helper.push_remote(**config)
            self.end('Finished!')

    def update_handler(self):
        if self.args.update is None:
            return
        arg_len = len(self.args.update)
        if arg_len is 0:
            raise Exception('The namespace you want to update is not given.')
        elif arg_len >= 1:
            namespace = self.args.update[0]
            config = self.get_config(namespace)
            root_dir = input("Input namespace's root directory(%s):" % config['root_dir'])
            from_branch = input("Input the local raw branch(%s):" % config['from_branch'])
            to_branch = input("Input the origin target branch(%s):" % config['to_branch'])
            root_dir = root_dir if root_dir != '' else config['root_dir']
            from_branch = from_branch if from_branch != '' else config['from_branch']
            to_branch = to_branch if to_branch != '' else config['to_branch']
            self.save_config(namespace=namespace, root_dir=root_dir, from_branch=from_branch, to_branch=to_branch)
            self.end('Update the namespace(%s).' % namespace)

    def list_handler(self):
        if self.args.list is None:
            return
        arg_len = len(self.args.list)
        if arg_len is 0:
            all_config = self.get_config()
            self.end('\n'.join(self.config_format(all_config[i]) for i in all_config))
        elif arg_len >= 1:
            namespace = self.args.list[0]
            config = self.get_config(namespace)
            self.end(self.config_format(config))

    def delete_handler(self):
        if self.args.delete is None:
            return
        arg_len = len(self.args.delete)
        if arg_len is 0:
            is_clear = input("Are you sure to clean all the namespace(Y/N):")
            if is_clear == 'Y':
                self.config.delete()
            else:
                self.end('Clean all the namespace has been canceled.')
        elif arg_len >= 1:
            namespace = self.args.delete[0]
            config = self.get_config(namespace)
            self.delete_config(namespace)
            self.end('Namespace(%s) has been deleted' % namespace)

    def add_handler(self):
        if self.args.add is None:
            return

        namespace = input("Input the namespace name:")
        root_dir = input("Input namespace's root directory:")
        from_branch = input("Input the local raw branch:")
        to_branch = input("Input the origin target branch:")
        self.save_config(namespace=namespace, root_dir=root_dir, from_branch=from_branch, to_branch=to_branch)
        self.end('Create a new namespace(%s).' % namespace)

    def config_format(self, config):
        return self.config_template % (
            config['namespace'],
            config['root_dir'],
            config['from_branch'],
            config['to_branch']
        )

    def get_config(self, namespace=None):
        config = self.config.get(namespace)
        if config is None:
            raise Exception('Namespace(%s) is non-existent' % namespace)
        return config

    def save_config(self, **kwargs):
        self.config.save(**kwargs)

    def delete_config(self, namespace=None):
        self.config.delete(namespace)

    def parse(self):
        try:
            self.execute()
            self.list_handler()
            self.delete_handler()
            self.add_handler()
            self.update_handler()
            self.parser.print_help()
        except Exception as err:
            print('Progress exited with an Error: '+str(err))

    @staticmethod
    def end(text):
        print(text)
        sys.exit()

    @staticmethod
    def init_parser():
        parser = argparse.ArgumentParser(prog='ghelp', usage='%(prog)s [command] [namespace]')
        parser.add_argument('namespace', nargs='*', help='execute namespace\'s action')
        parser.add_argument('-l', '--list', nargs='*', help='list namespace info')
        parser.add_argument('-d', '--delete', nargs='*', help='delete namespace')
        parser.add_argument('-a', '--add', nargs='*', help='add namespace')
        parser.add_argument('-u', '--update', nargs='*', help='update namespace info')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')
        return parser

