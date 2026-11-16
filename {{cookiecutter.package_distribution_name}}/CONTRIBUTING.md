# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development
Clone the repository and enter its directory. Create and activate a Python 3.11+ virtual environment.
```bash
python -m pip install -e .
```

## Run the tests
```bash
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```
Expected output: `Hello, Hee!`

## Send a change
Start from `main` and create a branch, then edit and commit your change:
```bash
git switch main
git switch -c add-usage
git add README.md
git commit -m "Add usage example"
git push -u origin add-usage
```
Open a pull request from `add-usage` into `main` on GitHub.
