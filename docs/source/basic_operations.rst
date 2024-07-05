Basic Git Operations
====================

This section covers the fundamental Git commands you'll use in your day-to-day work.

.. _git-init:

git init
--------

Initializes a new Git repository.

.. code-block:: bash

   git init

.. _git-add:

git add
-------

Adds changes in the working directory to the staging area.

.. code-block:: bash

   git add <file>

To add all changes:

.. code-block:: bash

   git add .

.. _git-commit:

git commit
----------

Records the changes in the repository.

.. code-block:: bash

   git commit -m "Your commit message"

.. _git-status:

git status
----------

Shows the working tree status.

.. code-block:: bash

   git status

.. _git-log:

git log
-------

Shows commit logs.

.. code-block:: bash

   git log

.. _git-diff:

git diff
--------

Shows changes between commits, commit and working tree, etc.

.. code-block:: bash

   git diff

.. _git-stash:

git stash
---------

Stashes the changes in a dirty working directory away.

Save changes to a stash:

.. code-block:: bash

   git stash

Apply stashed changes:

.. code-block:: bash

   git stash apply

.. _git-stash-pop:

Pop stashed changes:

.. code-block:: bash

   git stash pop