# Django SKELETON

Django new project template. Created after having manually rebuilt to the same base state too many times. No more looking up urls import, load static template definition, boilerplate HTML, etc. The opinionated minimum to start writing the interesting stuff. Deployment is a hacky search-and-replace done in a way to offer a semblance of code auditing.

With [ripgrep](https://github.com/BurntSushi/ripgrep) and [black](https://github.com/psf/black) on PATH, build a new 'foobar' project (in a new virtual environment) by:

```bash
git clone https://github.com/dbready/django_skeleton.git foobar
cd foobar
# install latest Django release + minimum dependency
pip install django dj-database-url
pip freeze > requirements.txt
# start fresh project locally
django-admin startproject foobar
 # standardize code formatting
black foobar
# commit the new project configuration
git add -A
git commit -m "Commit fresh Django startproject"
# replace fresh foobar with a copy of skeleton
# (copy so as to not pollute the git diff)
rm -rf foobar
cp -r skeleton foobar
mv foobar/skeleton foobar/foobar
# case-sensitive search and replace placeholder project name
rg --null --files-with-matches "SKELETON" | xargs -0 sed -i 's/SKELETON/FOOBAR/g'
rg --null --files-with-matches "skeleton" | xargs -0 sed -i 's/skeleton/foobar/g'
```

Git will now report all diffs between the freshly run `startproject` and the skeleton. If everything in the `foobar` project is acceptable, finalize the initialization as if you had rolled-up your sleeves:

```bash
rm -rf skeleton
rm -rf .git
git init
```
