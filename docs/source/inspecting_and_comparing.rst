Inspecting and Comparing
========================

Status
------

Check the status of your working directory:

.. code-block:: bash

   git status

For a more concise status:

.. code-block:: bash

   git status -s

Diff
----

View changes between working directory and staging area:

.. code-block:: bash

   git diff

View staged changes:

.. code-block:: bash

   git diff --staged

Compare two branches:

.. code-block:: bash

   git diff <branch1>..<branch2>

Log
---

View commit history:

.. code-block:: bash

   git log

View a compact log:

.. code-block:: bash

   git log --oneline

View log with branching graph:

.. code-block:: bash

   git log --graph --oneline --all

View log for a specific file:

.. code-block:: bash

   git log -- <file>

Limit log output:

.. code-block:: bash

   git log -n 5  # Show only the last 5 commits

Show
----

View details of a specific commit:

.. code-block:: bash

   git show <commit-hash>

