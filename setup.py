from setuptools import setup, find_packages

setup(
    name='git_helper',
    version='1.0.0',
    keywords=('git'),
    description='a git tool to push for multi projects',
    license='MIT License',
    install_requires=[],

    author='sidfate',
    author_email='sidfate@163.com',
    url='https://sidfate.com',

    packages=find_packages(),
    platforms='any',
    entry_points={
        'console_scripts': [     #如果你想要以Linux命令的形式使用
            'ghelp = GitHelper.main:main'
        ]
      },
)