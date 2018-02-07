GitHelper
=========

A git tool to push for multi projects.

If you are a full-stack or manage multiple projects, it's too fussy to
type git command to push the code particularly the changes in the
project are frequent. So GitHelper can help you to manage projects' git
with the simple command.

Enjoy it :).

Installing
----------

To install an already packaged version directly from PyPi:

::

    $ pip install git-helper

Usage
-----

ghelp
~~~~~

type the ``ghelp`` in shell you can see all the usage of this command.

::

    $ ghelp
    usage: ghelp [command] [namespace]

    positional arguments:
      namespace             execute namespace's action

    optional arguments:
      -h, --help            show this help message and exit
      -l [LIST [LIST ...]], --list [LIST [LIST ...]]
                            list namespace info
      -d [DELETE [DELETE ...]], --delete [DELETE [DELETE ...]]
                            delete namespace
      -a [ADD [ADD ...]], --add [ADD [ADD ...]]
                            add namespace
      -u [UPDATE [UPDATE ...]], --update [UPDATE [UPDATE ...]]
                            update namespace info
      -v, --version         show program's version number and exit

ghelp -a,-add
~~~~~~~~~~~~~

``ghelp -a`` creates a new namespace.That will receive three params:

- namespace: generally the project name
- from\_branch: the local raw branch
- to\_branch: the remote target branch

The created namespace will be saved into one local file(push.json) which
is formatted with json.

.. code:: shell

    $ ghelp -a
    Input the namespace name:gstore
    Input root directory of namespace:D:\work\GStore
    Input the local raw branch:lumen
    Input the origin target branch:release-2.0.0
    Create a new namespace(gstore).

ghelp namespace [message]
~~~~~~~~~~~~~~~~~~~~~~~~~

``ghelp [namespace]`` is the most important command. This command
execute the full operation, include commit and push the local branch and
merge the local branch into another target branch which generally is the
remote one. By the way, the argv ``message`` is the commit message, and
also optional.

::

    $ ghelp gstore 111
    Active code page: 65001

    lumen


    Your branch is up-to-date with 'origin/lumen'.
    Already on 'lumen'



    [git commit -m "111"] end with a error return code 1
    On branch lumen
    Your branch is up-to-date with 'origin/lumen'.

    nothing to commit, working tree clean

    Everything up-to-date

    Your branch is up-to-date with 'origin/release-2.0.0'.
    Switched to branch 'release-2.0.0'

    Already up-to-date.

    git merge -m "Merge lumen into release-2.0.0" lumen
    Merge made by the 'recursive' strategy.
     _mall/tests/Http/Home/AppTest.php | 2 +-
     1 file changed, 1 insertion(+), 1 deletion(-)

    To code.aliyun.com:ecarx-srv/GStore.git
       32a9b2b3..d4bc675a  release-2.0.0 -> release-2.0.0

    Your branch is up-to-date with 'origin/lumen'.
    Switched to branch 'lumen'

    Finished!

ghelp -l,--list [namespace]
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``ghelp -l`` lists the namespace info.If namespace is not given, show
all namespace's info.

show one namespace:

::

    $ ghelp -l gstore
    [gstore]
    root_dir=D:\work\GStore
    from_branch=lumen
    to_branch=release-1.0.0

show all namespace:

::

    $ ghelp -l
    [gstore]
    root_dir=D:\work\GStore
    from_branch=lumen
    to_branch=release-1.0.0

    [test]
    root_dir=D:/test
    from_branch=dev
    to_branch=master

ghelp -d,--delete [namespace]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``ghelp -d`` deletes the namespace.If namespace is not given, it will
clear all namespace.

delete one:

::

    $ ghelp -d gstore
    Namespace(gstore) has been deleted

clear all:

::

    $ ghelp -d
    Are you sure to clean all the namespace(Y/N):y
    Clean all the namespace has been canceled.

ghelp -u,--update namespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``ghelp -u`` updates the namespace info.

::

    $ ghelp -u gstore
    Input namespace's root directory(D:\work\GStore):
    Input the local raw branch(lumen):
    Input the origin target branch(release-2.0.0):release-1.0.0
    Update the namespace(gstore).

Development
-----------

Requirements
~~~~~~~~~~~~

-  python >= 3.5

Building
~~~~~~~~

GitHelper uses Python'setuptools to manage dependencies and build.

To install its dependencies:

::

    $ python setup.py install

Example setups
--------------

License
-------

MIT.
