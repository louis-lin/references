Introduction to Git
===================

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. For more detailed information, visit the `official Git website <https://git-scm.com/>`_.

Git Workflow Diagram
---------------------

Here's a visual representation of a simple Git workflow:

.. mermaid::

   graph LR
    A[Working Directory] -->|git add| B[Staging Area]
    B -->|git commit| C[Local Repository]
    C -->|git push| D[Remote Repository]
    D -->|git clone/pull| C
    C -->|git checkout| A
    
    C -->|git branch| E[New Branch]
    E -->|git merge| C
    E -->|git branch -d <branchName>| G[Delete]
    
    A -->|git stash| F[Stash]
    F -->|git stash pop| A

    style A fill:#E0F7FA,stroke:#006064
    style B fill:#E8F5E9,stroke:#1B5E20
    style C fill:#FFF3E0,stroke:#E65100
    style D fill:#EDE7F6,stroke:#4527A0
    style E fill:#FCE4EC,stroke:#880E4F
    style F fill:#FFEBEE,stroke:#B71C1C

    linkStyle 0,1,2,3,4,5,6,7,8 stroke:#333,stroke-width:3px;

Understanding Git
--------------------------------------

Think of Git as a magical library system for your project:

1. **Repository**: Your project's main library.
2. **Working Directory**: Your personal reading desk where you can make changes to books.
3. **Staging Area**: A review desk where you prepare changes before "publishing".
4. **Commit**: A published edition of your books, cataloged in the library's history.
5. **Branch**: A separate reading room where you can experiment with changes without affecting the main library.
6. **Merge**: Combining the changes from one reading room back into the main library.
7. **Remote**: A duplicate of your library stored in another location (like GitHub).

Basic Git Workflow
------------------

1. :ref:`Initialize <git-init>` a new library or :ref:`clone <git-clone>` an existing one.
2. Make changes to your books at your reading desk (Working Directory).
3. :ref:`Add <git-add>` changed books to the review desk (Staging Area).
4. :ref:`Commit <git-commit>` your changes, creating a new edition in the library catalog.
5. :ref:`Push <git-push>` your changes to share them with other libraries.
6. :ref:`Pull <git-pull>` changes from other libraries to update your local copy.
7. Create a new :ref:`branch <git-branch>` (reading room) for experiments or new features.
8. :ref:`Merge <git-merge>` branches when work is complete.


Commit History
--------------

Git's commit history can be visualized as a series of snapshots of your library over time:

.. mermaid::

   gitGraph
      commit
      commit
      branch feature
      checkout feature
      commit
      commit
      checkout main
      merge feature
      commit

In this graph:
- Each circle represents a commit (a published edition of your library).

- The main line represents the main branch of development.

- The branch line shows a separate line of development (a different reading room).

- The merge point shows where the changes from the branch are incorporated back into the main library.
