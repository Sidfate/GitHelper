# !/usr/bin/env python
# encoding: utf-8
import subprocess
import sys


class GitHelper:
    file_path = ''
    cmd_log = []
    current_branch = ''

    """docstring for GitHelper"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.call('chcp 65001')
        self.branch()

    def status(self):
        out = self.call(['git', 'status'])
        print(out)

    """提交修改"""
    def commit(self, comment):
        self.call('git add -A')
        self.call('git commit -m "'+comment+'"')
        pass

    """push"""
    def push(self):
        self.call(['git', 'push'])

    """pull"""
    def pull(self):
        self.call(['git', 'pull'])

    """切换分支"""
    def checkout(self, branch):
        self.call('git checkout '+branch)

    """获取当前分支"""
    def branch(self):
        current_branch = self.call('git symbolic-ref --short -q HEAD')
        self.current_branch = str(current_branch.strip())
        return self.current_branch

    """合并分支"""
    def merge(self, branch):
        self.call('git merge --no-commit '+branch)

    """调用命令"""
    def call(self, command):
        try:
            out = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, cwd=self.file_path)
            log = {
                'command': command,
                'output': str(out.decode()),
                'path': self.file_path
            }
            self.cmd_log.append(log)
            print(out.decode())
            return out
        except subprocess.CalledProcessError as e:
            self.error(command, e)

    """错误处理"""
    def error(self, command, e):
        message = '[' + command + '] end with a error return code '+str(e.returncode)+"\n"+str(e.output.decode())
        self.exit(message)

    """成功处理"""
    def success(self):
        self.exit("Commands Complete！")

    """退出程序"""
    def exit(self, message):
        try:
            sys.exit(0)
        except:
            print(message)

    """输出日志"""
    def history(self):
        for log in self.cmd_log:
            command = log['command']
            if isinstance(command, list):
                command = ' '.join(command)
            print('[' + command + ']\n'+log['output'])

    """跨分支发布"""
    def push_remote(self, **kwargs):
        self.call(['cd', kwargs['root_dir']])
        self.checkout(kwargs['from_branch'])
        self.pull()
        self.commit(kwargs['comment'])
        self.push()
        self.checkout(kwargs['to_branch'])
        self.pull()
        self.merge(kwargs['from_branch'])
        self.push()
        self.checkout(kwargs['from_branch'])
        pass


