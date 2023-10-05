#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

# Build the api documentation
SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"
cd "${SCRIPT_DIR}"

# build the api documentation
poetry run sphinx-apidoc --implicit-namespaces --separate --module-first --templatedir _templates -o reference ../src/{{ cookiecutter.__project_root_dir }}

# build the complete documentation
poetry run sphinx-build -a -T -E -j auto -n --color -W --keep-going -b html . _build/html

# Check links in the documentation
poetry run sphinx-build -b linkcheck . _build/linkcheck
