# Git Cheat sheet
We will be using git as version control this semester in order to keep track of people's changes in an orderly fashion. Below are some commands that you will find useful for this lab and for the rest of the semester. Commands will be on the left and the description will be on the right.

## Basic Commands
git init - initialize a git repository. You must do this at the top level directory of every new project you create. You don't need to do this if you clone someone else's repository.

git clone `<url>` - Clone a repository from github. 

git remote add origin `<url>` - Sets the url origin of your git repository for when you push to github.

git remote set-url origin `<url>` - Sets the url origin of your git repository for when you push to github if a different origin had been set previously.

git status - Lets you see what files have been changed.

git diff - Lets you see what lines were modified/added/deleted

git add [`<files>` | -u | . | -A] - Add files for staging to be committed. `<files>` adds specific files, -u adds files previously committed, . adds everything in your current directory, -A adds everything

git commit -m "`<Message>`" - Commit your files with a message

git push origin `<branch_name>` - Push your files to the branch. 

## Branches
git checkout -b `<new_branch_name>` - Create a new branch and switch to it

git checkout `<branch_name>` - Switch branches

git branch - Check what branch you currently are on
