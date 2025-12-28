# Release Procedure

1. **Pre-Release Checks**
   - Ensure all tests pass locally: `pytest`
   - Ensure mypy is green: `mypy src`
   - Ensure CI is passing on `main`.

2. **Version Bump**
   - Update `__version__` in `src/dbl_ingress/__init__.py`.
   - Update `version` in `pyproject.toml`.
   - Update `CHANGELOG.md` with release date and version.

3. **Commit & Tag**
   - Create a PR with the version bump.
   - Merge PR.
   - Tag the commit on `main`: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
   - Push tag: `git push origin vX.Y.Z`

4. **Build & Publish**
   - Clean artifacts: `rm -rf dist/ build/`
   - Build: `python -m build`
   - Publish to PyPI (if applicable) or internal registry: `twine upload dist/*`
