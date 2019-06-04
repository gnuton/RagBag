# Git
## Commits
```bash
// status of the files
git status

// diff
git changes

// commit history
git log

// revert a single commit
git revert COMMIT_HASH

// pick a commit from a different branch
git cherry-pick COMMIT_HASH_IN_ANOTHER_BRANCH
```
### Cleaning 
```bash
// clean modified files
git checkout .
// remove files not tracked
git clean -df
```

# Branches
## Show
```bash
// list local branches
git branch

// git remote branches
git branch -a
```

## Create 
```
// track a remote branch
git checkout -b BRANCH origin/BRANCH

// create an orphan branch

// fork a branch
git checkout BRANCH_I_WANNA_FORK
git branch NEW_BRANCH

// create a branch pointing to a commit
git checkout -b branch_name COMMIT_HASH
```
## Delete
```bash
// delete local branch
git branch -d BRANCH_TO_DELETE

// delete local branch even if we lose some commits
git branch -D BRANCH_TO_DELETE

// delete remote branch
git push --delete origin BRANCH_TO_DELETE
```
## Merging
```
git checkout TARGET_BRANCH
git merge --squash BRANCH_CONTAINING_THE_CHANGES_TO_MERGE_INTO_TARGET
git commit
```
# Tags
```
// create tag
git tag

// push tags to remote
git push --tag

//delete local tag
git delete LOCAL_TAG_NAME

//delete remote tag
git push origin -- delete TAG_TO_DELETE_REMOTELY
```
