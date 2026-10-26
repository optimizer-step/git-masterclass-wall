# Optimizer Step | Git & GitHub Masterclass Contributors Wall

Your first open-source-style pull request. Fork this repository, create your own branch, copy `contributors/_TEMPLATE.md` to `contributors/YOUR_USERNAME.md`, edit the three fields, and make a pull request.

## Steps
1. Fork in GitHub. Clone **your fork** locally: `git clone https://github.com/YOUR_USERNAME/git-masterclass-wall.git`.
2. `git switch -c add-YOUR_USERNAME`
3. Make `contributors/YOUR_USERNAME.md` from `_TEMPLATE.md`; use only safe public details (a nickname is fine; city is optional).
4. `python -m unittest discover -s tests -v`
5. `git add contributors/YOUR_USERNAME.md && git commit -m "Add YOUR_USERNAME to contributors wall"`
6. `git push -u origin add-YOUR_USERNAME`
7. Open a PR from your fork to the original project; watch the CI checks.

Please do not include email addresses, phone numbers, passwords, or tokens.

## For the host
This folder is the public contributor-wall repository. Configure repo rules before the stream. Keep collaborator permissions restricted. Do not enable automatic PR merging from unknown contributors.

## Repository and lab locations

The public contributor wall is https://github.com/optimizer-step/git-masterclass-wall.
Run contributor-wall commits and pushes from `class-repo/`, the folder containing this README.

The `labs/` folder contains separate disposable practice repositories for conflict,
recovery, fake-secret, and bisect exercises. It is ignored by this repository so
their histories remain local. Run lab commands only inside the appropriate lab;
do not push a lab to the contributor-wall repository.
