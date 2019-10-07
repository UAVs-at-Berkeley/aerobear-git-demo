# Git Cheat sheet
We will be using git as version control this semester in order to keep track of people's changes in an orderly fashion. Below are some commands that you will find useful for this lab and for the rest of the semester. Commands will be on the left and the description will be on the right.

## Basic Commands
`git init` - initialize a git repository. You must do this at the top level directory of every new project you create. You don't need to do this if you clone someone else's repository.

`git clone <url>` - Clone a repository from github. 

`git remote add origin <url>` - Sets the url origin of your git repository for when you push to github.

`git remote set-url origin <url>` - Sets the url origin of your git repository for when you push to github if a different origin had been set previously.

`git status` - Lets you see what files have been changed.

`git diff` - Lets you see what lines were modified/added/deleted

`git add [<files> | -u | . | -A]` - Add files for staging to be committed. `<files>` adds specific files, -u adds files previously committed, . adds everything in your current directory, -A adds everything

`git commit -m "<Message>"` - Commit your files with a message

`git push origin <branch_name>` - Push your files to the branch. 

## Branches
`git checkout -b <new_branch_name>` - Create a new branch and switch to it

`git checkout <branch_name>` - Switch branches

`git branch` - Check what branch you currently are on

## Side note: Continuous Integration

### What is CI?
> Continuous Integration (CI) is a development practice where developers integrate code into a shared repository frequently, preferably several times a day. Each integration can then be verified by an automated build and automated tests. While automated testing is not strictly part of CI it is typically implied.

From [CodeShip](https://codeship.com/continuous-integration-essentials)


When you make a pull request in this repository, GitLab CI notices the new branch and fetches it. CI then runs our test, checking whether or not you've uploaded a valid JSON file under `data` folder.

On the master branch once the PR is merged, if all tests pass, then GitLab CI uploads the data to our flask app running [here](https://aerobear.berkeley.edu/git-demo/). You can see your merged commit having an effect by adding your name to the marquee on the top of the page.