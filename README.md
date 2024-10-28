# uv trusted publishing examples

Trusted publishing allows uploading package from GitHub Action to PyPI without
manually setting a secret token. Instead, you specify on PyPI a GitHub Actions
workflow that is allowed to publish the package.

This repository contains a full, self-contained example for trusted publishing
with uv. The release workflow can be found in
[.github/workflows/release.yml](.github/workflows/release.yml). On PyPI, the
matching configuration is set under
`https://pypi.org/manage/project/<package-name>/settings/publishing/`:

![Screenshot from PyPI.
Manage current publishers.
Publisher: GitHub.
Details:
Repository: astral-sh/trusted-publishing-examples
Workflow: release.yml
Environment name: release](data/trusted-publishing-config-pypi.png)

You can find the published package at
https://pypi.org/project/trusted-publishing-examples/.

[.github/workflows/ci.yml](.github/workflows/ci.yml) is a minimal test and lint
workflow for a Python package, while
[.github/workflows/errors.yml](.github/workflows/errors.yml) is for testing uv
itself only.

## Documentation

- uv's side: https://docs.astral.sh/uv/guides/publish/
- PyPI's side: https://docs.pypi.org/trusted-publishers/
