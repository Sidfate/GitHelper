# !/usr/bin/env python
# encoding: utf-8
import subprocess
import sys
import codecs


class ConfigHelper:

    def __init__(self):
        self.fd = codecs.open('push.conf', 'r+', 'utf-8')

    def add(self, name, root_dir, from_branch, to_branch):
        name_text = "[%s]" % name
        print(name_text)
        for line in self.fd.readlines():
            if line.strip() == name_text:
                self.update()
                return
        text = """
[%s]
root_dir=%s
from=%s
to=%s
        """ % (name, root_dir, from_branch, to_branch)
        self.fd.write(text)

    def update(self):
        print('update')
        pass

    def __del__(self):
        self.fd.close()


if __name__ == '__main__':
    helper = ConfigHelper()
    helper.add('test', "D:\sidfate\git\FuckingTime", "master", "master")
