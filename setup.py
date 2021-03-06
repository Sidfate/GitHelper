from setuptools import setup, find_packages

with open('README.rst') as f_readme:
    readme = f_readme.read()

setup(
    name='git-helper',
    version='1.0.7',
    keywords=('git'),
    description='a git tool to push for multi projects',
    long_description=readme,
    license='MIT License',
    install_requires=[],

    author='sidfate',
    author_email='sidfate@163.com',
    url='https://github.com/Sidfate/GitHelper',

    packages=find_packages(),
    platforms='any',
    entry_points={
        'console_scripts': [     #如果你想要以Linux命令的形式使用
            'ghelp = GitHelper.command:command_execute'
        ]
      },
)