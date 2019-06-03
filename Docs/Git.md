# Git
# Branches
## Create branch pointing to a particular commit
git checkout -b branch_name COMMIT_HASH

# Merging
## Merge commits from a branch in a new one
git checkout TARGET_BRANCH
git merge --squash BRANCH_CONTAINING_THE_CHANGES_TO_MERGE_INTO_TARGET
git commit

