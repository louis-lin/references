Remote Operations
=================

Working with Remotes
--------------------

List remote repositories:

.. code-block:: bash

   git remote -v

Add a new remote:

.. code-block:: bash

   git remote add <name> <url>

Remove a remote:

.. code-block:: bash

   git remote remove <name>

Change a remote's URL:

.. code-block:: bash

   git remote set-url <name> <new-url>

Fetching
--------

Fetch downloads new data from a remote repository but doesn't integrate it into your working files:

.. code-block:: bash

   git fetch <remote>

Fetch all remotes:

.. code-block:: bash

   git fetch --all

Pulling
-------

Pull fetches and merges changes from a remote repository:

.. code-block:: bash

   git pull <remote> <branch>

If you want to fetch first and then merge manually:

.. code-block:: bash

   git fetch <remote>
   git merge <remote>/<branch>

Pushing
-------

Push uploads your local branch commits to a remote repository:

.. code-block:: bash

   git push <remote> <branch>

Force push (use with caution):

.. code-block:: bash

   git push -f <remote> <branch>

Set up branch tracking:

.. code-block:: bash

   git push -u <remote> <branch>

