# Cosmic Data Stories

Cosmic Data Stories are online interactive resources for teaching the public data science skills. They are built on research-grade visualization tools like [glue](https://glueviz.org) and [WorldWide Telescope](https://worldwidetelescope.org/home).

This repository is a monorepo for the Cosmic Data Stories project. It contains the code for the Cosmic Data Stories website, as well as the code for the individual stories.

### Current available stories

| Story Name | Description | Version |
|------------|-------------|---------|
| Hubble's Law | Explore the expansion of the universe using Hubble's Law | 0.1.0   |

## Installation

To install a data story, clone or download this repository and navigate to the story directory. **Note**: it is recommended to install the stories in a virtual environment to avoid conflicts with other packages.

```bash
# Example install for Hubble's Law
cd cosmicds/packages/cds-hubble
pip install uv
uv pip install .
```

## Developer Setup

Developer setup is done using [`uv`](https://docs.astral.sh/uv/), a Python package and project manager. To get started, follow these steps:

1. Follow the [`uv` installation instructions](https://docs.astral.sh/uv/getting-started/installation/) to install `uv`.
2. If you use `conda` or have an active `conda` environment, it is recommended you disable it as `uv` will create its own environment. You can do this by running:
   ```bash
   conda deactivate
   ```
   `conda`'s auto-activation feature can also be disabled by running:
   ```bash
    conda config --set auto_activate_base false
    ```
   which will ensure that the `conda` base environment is not automatically activated when initiating a new terminal session.
3. Move to the top-level directory of the repository and run the following command to create a new `uv` environment:
   ```bash
   cd cosmicds
   uv sync --all-packages
   ```
   A new environment should now be defined in the `.venv` directory.

   Note for Linux developers: `uv` uses Clang as its compiler [by default](https://github.com/astral-sh/uv/issues/8036).
   As pywwt's `toasty` dependency requires C compilation, this can be a problem, as many Linux distributions don't include Clang by default.
   Thus, you can either install Clang, or use your system's default compiler (probably `gcc`) in the command, eg:
   ```bash
   CC=<compiler> uv sync --all-packages
   ```

   Note about `ipywwt`: If you run into an issue with the `npm run build` subprocess command failing when building `ipywwt`, you may
   need to install `webpack` and `webpack-cli` globally on the Node.js that you're using:
   ```bash
   npm i -g webpack webpack-cli
   ```
5. Activate the environment:
   ```bash
   source .venv/bin/activate
   ```
   This environment can be referenced in your editor of choice by setting the interpreter to `.venv/bin/python`.


All data stories should now be accessible by the command line. To start a story, run the following command:
```bash
<environment variables> solara run <story>.pages

# Example for Hubble's Law
SOLARA_SESSION_SECRET_KEY="..." \
SOLARA_OAUTH_CLIENT_ID="..." \
SOLARA_OAUTH_CLIENT_SECRET="..." \
SOLARA_OAUTH_API_BASE_URL="..." \
SOLARA_OAUTH_SCOPE="..." \
SOLARA_SESSION_HTTPS_ONLY=false \
CDS_API_KEY="..." 
solara run cds_hubble.pages
```
