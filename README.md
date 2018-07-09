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