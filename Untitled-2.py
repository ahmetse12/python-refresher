

git add .

git commit -m "Initial commit"

git checkout -b new-feature

git add .
git commit -m "Add new feature"

git checkout main
git merge new-feature

git push origin main

