#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

# Build the api documentation
SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"
cd "${SCRIPT_DIR}"

# build the api documentation
poetry run sphinx-apidoc --implicit-namespaces --separate --module-first -o api/reference ../src/{{ cookiecutter.__project_root_dir }}

# build the complete documentation
poetry run sphinx-build -a -E -j auto -n --color -W --keep-going -b html api api/_build/

# Check links in the documentation
poetry run sphinx-build -b linkcheck api api/_build/linkcheck/
