Branching and Merging
=====================

Branching
---------

Branching allows you to diverge from the main line of development and work on different features or experiments without affecting the main codebase.

Create a new branch:

.. code-block:: bash

   git branch <branch-name>

Switch to a branch:

.. code-block:: bash

   git checkout <branch-name>

Create and switch to a new branch in one command:

.. code-block:: bash

   git checkout -b <new-branch-name>

List all branches:

.. code-block:: bash

   git branch

Delete a branch:

.. code-block:: bash

   git branch -d <branch-name>

Merging
-------

Merging integrates changes from one branch into another.

To merge a branch into your current branch:

.. code-block:: bash

   git merge <branch-name>

If there are conflicts, Git will mark the conflicting areas in the affected files. You'll need to resolve these manually, then:

.. code-block:: bash

   git add <resolved-file>
   git commit -m "Merge branch 'branch-name'"

Fast-forward Merges
^^^^^^^^^^^^^^^^^^^

When the branch being merged is directly ahead of the current branch, Git performs a "fast-forward" merge. To force a merge commit even for fast-forward merges:

.. code-block:: bash

   git merge --no-ff <branch-name>

Merge Strategies
^^^^^^^^^^^^^^^^

Git uses different merge strategies depending on the situation. The most common are:

- Fast-forward (default when possible)
- Recursive (default when fast-forward is not possible)
- Octopus (for merging more than two branches)

You can specify a strategy with:

.. code-block:: bash

   git merge -s <strategy> <branch-name>

