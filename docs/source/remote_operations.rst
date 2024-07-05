Remote Operations
=================

This section covers Git commands used for interacting with remote repositories.

.. _git-remote:

git remote
----------

The `git remote` command lets you create, view, and delete connections to other repositories.

List remote connections:

.. code-block:: bash

   git remote -v

Add a new remote:

.. code-block:: bash

   git remote add <name> <url>

Remove a remote:

.. code-block:: bash

   git remote remove <name>

.. _git-fetch:

git fetch
---------

`git fetch` downloads objects and refs from another repository.

Fetch from a specific remote:

.. code-block:: bash

   git fetch <remote>

Fetch all remotes:

.. code-block:: bash

   git fetch --all

.. _git-pull:

git pull
--------

`git pull` fetches and merges changes from a remote repository.

Pull from a specific remote branch:

.. code-block:: bash

   git pull <remote> <branch>

.. _git-push:

git push
--------

`git push` updates remote refs along with associated objects.

Push to a specific remote:

.. code-block:: bash

   git push <remote> <branch>

Push all branches to a remote:

.. code-block:: bash

   git push --all <remote>

.. _git-clone:

git clone
---------

`git clone` creates a copy of an existing Git repository.

Clone a repository:

.. code-block:: bash

   git clone <repository-url>

Clone a specific branch:

.. code-block:: bash

   git clone -b <branch> <repository-url>

