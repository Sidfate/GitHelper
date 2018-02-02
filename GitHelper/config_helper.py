# !/usr/bin/env python
# encoding: utf-8
import os
import codecs
import json


class ConfigHelper:
    filename = "push.json"

    def __init__(self):

        if not os.path.isfile(self.filename):
            tmp = codecs.open('push.json', 'x', 'utf-8')
            tmp.write(json.dumps({}))
            tmp.close()
        tmp = open(self.filename, 'r')
        self.config = json.loads(tmp.read())
        tmp.close()

    def save(self, namespace, root_dir, from_branch, to_branch):
        self.config[namespace] = {
            'namespace': namespace,
            'root_dir': root_dir,
            'from_branch': from_branch,
            'to_branch': to_branch
        }
        self.rewrite()

    def delete(self, namespace):
        if namespace in self.config:
            self.config.pop(namespace)
            self.rewrite()

    def get(self, namespace=None):
        return self.config if (namespace is None) else (self.config[namespace] if (namespace in self.config) else None)

    def rewrite(self):
        tmp = open(self.filename, 'w')
        tmp.write(json.dumps(self.config))
        tmp.close()


# if __name__ == '__main__':
#     helper = ConfigHelper()
#     helper.save('test2', "D:\sidfate\git\FuckingTime", "master", "master")
