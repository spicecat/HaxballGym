# Local packages

Place local dependencies here to use them via Poetry path dependencies.

## Add `ursinaxball`

You have three options to bring your custom `ursinaxball` here:

- Simple move/copy (quickest):
  ```bash
  mv /home/ahteh/Developer/Ursinaxball /home/ahteh/Developer/HaxballGym/packages/ursinaxball
  ```
  Ensure it contains a valid Python package (with `pyproject.toml` or `setup.cfg/setup.py` and a top-level `ursinaxball` module).

- Git submodule (keep separate repo, easy updates):
  ```bash
  cd /home/ahteh/Developer/HaxballGym
  git submodule add ../Ursinaxball packages/ursinaxball
  git submodule update --init --recursive
  ```

- Git subtree (vendor the code, preserves history inside this repo):
  ```bash
  cd /home/ahteh/Developer/HaxballGym
  git remote add ursinaxball ../Ursinaxball
  git subtree add --prefix packages/ursinaxball ursinaxball master --squash
  ```

After adding it, reinstall deps so Poetry picks up the path dependency:

```bash
poetry install
```

Verify the local package is being used:

```bash
python -c "import ursinaxball, sys; print(ursinaxball.__file__)"
```
Should point inside `packages/ursinaxball`.
