# wwPDB Python Code Development Best Practices

## Description

This document intends to document the coding standards and best practices that
should be employed when developing in Python for wwPDB projects.

In addition, there is a document describing some of the major differences in
Python 3 and the update process [here](2to3.md).

Major foci of this document:

* [Using Git](#using-git)
* [Python Coding Standards](#python-coding-standards)
* [Unit Testing](#unit-testing)
* [Continuous Integration](#continuous-integration)

### Using Git

Using git provides many benefits over SVN. First and foremost, git is designed for
decentralized collaboration. This is a major benefit for teams of people in different
locations working together on a shared project. Other major benefits of git:

* Github website enables
  * Contributions from anyone in the open-source community via pull requests
  * Integrated bug tracking
  * Using free [continuous integration software](#continuous-integration)
* Lightweight branches
  * All new feature development should be done in branches
  
Most important things to keep in mind when developing using git:

* Create branches for all development
* Commit frequently
* Use descriptive commit messages

More detailed best practices documents can be found [here](https://sethrobertson.github.io/GitBestPractices/)
and [here](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices).

### Python Coding Standards

Python code should be written following [PEP008](https://www.python.org/dev/peps/pep-0008/). A good IDE like
[PyCharm](https://www.jetbrains.com/pycharm/) will highlight issues automatically.

Most important:

* Use four spaces per indentation level - not tabs
* Use proper [casing for names](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions)
* Be consistent in use of single or double quotes for string declarations
* Document classes, methods, and functions using appropriate [docstrings](https://www.python.org/dev/peps/pep-0257/)
* Keep lines to a reasonable length (79-100 characters per line - exact length TBD)
* A foolish consistency is the hobgoblin of little minds

If you don't use PyCharm, you can check your code for PEP0008 compliance using [pylint](https://www.pylint.org/).

Additional considerations:

Python 3.5 has built-in support for [optional typing](https://docs.python.org/3/library/typing.html).
Using type annotations is recommended for new code development.

#### Project folder layout

Each git repository should contain one logical unit of related code. This usually means one module
per repository. Within that repository, some or all of the following files should be present:

```
README.rst
LICENSE
setup.py
requirements.txt
modname/__init__.py
modname/core.py
modname/helpers.py
docs/conf.py
docs/index.md
tests/test_modname.py
```

See more details on project layout [here](http://docs.python-guide.org/en/latest/writing/structure/).


### Unit Testing

