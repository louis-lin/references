Troubleshooting Common Git Issues
=================================

Branch Naming Issues
--------------------

Default Branch Names
^^^^^^^^^^^^^^^^^^^^

Check your current branch name:

.. code-block:: bash

   git branch

Rename a branch:

.. code-block:: bash

   git branch -m old-name new-name

Push Errors
-----------

If you encounter "src refspec main does not match any":

1. Ensure you've made at least one commit:

   .. code-block:: bash

      git add .
      git commit -m "Initial commit"

2. Check your remote setup:

   .. code-block:: bash

      git remote -v

3. Add or update your remote:

   .. code-block:: bash

      git remote add origin https://github.com/yourusername/your-repo-name.git
   
   or

   .. code-block:: bash

      git remote set-url origin https://github.com/yourusername/your-repo-name.git

4. Push to the correct branch:

   .. code-block:: bash

      git push -u origin your-branch-name

Offline Documentation Compilation
---------------------------------
.. _offline-compilation:

For Windows (using make.bat):

.. code-block:: bash

   .\make.bat html

For Unix-based systems (using Makefile):

.. code-block:: bash

   make html

If you encounter issues with make.bat, ensure you're running it from the correct directory and that you have Sphinx installed and accessible from your command line.
