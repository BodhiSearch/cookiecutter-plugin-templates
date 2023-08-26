#!/usr/bin/env python
import os
import sys
from pathlib import Path

docs_dir = Path(os.path.dirname(__file__))
src_dir = docs_dir / ".." / "src"
sys.path.insert(0, str(src_dir.resolve()))

# -- General configuration ---------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx_copybutton",
]

templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'

# General information about the project.
project = '{{ cookiecutter.project_name }}'
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.org_name }}"
author = "{{ cookiecutter.org_name }}"

# TODO: fetch version from pyproject.toml and set version and release
# version = {{ cookiecutter.project_slug }}.__version__
# The full version, including alpha/beta/rc tags.
# release = {{ cookiecutter.project_slug }}.__version__

language = "en"

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

# -- Options for HTML output -------------------------------------------
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
}
autodoc_typehints = "description"
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]
myst_url_schemes = ("http", "https", "mailto")
