Branch Operations
=================

This section covers Git commands related to creating, managing, and merging branches.

`git pull` fetches and merges changes from a remote repository.


.. _git-branch:

git branch
----------

Lists, creates, or deletes branches.

List all branches:

.. code-block:: bash

   git branch

Create a new branch:

.. code-block:: bash

   git branch <branch-name>

Delete a branch:

.. code-block:: bash

   git branch -d <branch-name>

.. _git-checkout:

git checkout
------------

Switches branches or restores working tree files.

Switch to an existing branch:

.. code-block:: bash

   git checkout <branch-name>

Create and switch to a new branch:

.. code-block:: bash

   git checkout -b <new-branch-name>

.. _git-merge:

git merge
---------

Joins two or more development histories together.

To merge a branch into your current branch:

.. code-block:: bash

   git merge <branch-name>

.. _git-rebase:

git rebase
----------

Reapply commits on top of another base tip.

To rebase your current branch onto another branch:

.. code-block:: bash

   git rebase <base-branch>

Caution: Rebasing rewrites commit history. Avoid rebasing commits that have been pushed to a public repository.