#!/usr/bin/env python
import os
import sys
from pathlib import Path
import toml

DOCS_DIR = Path(os.path.dirname(__file__))
PROJ_DIR = DOCS_DIR / ".."
SRC_DIR = PROJ_DIR / "src"
sys.path.insert(0, str(SRC_DIR.resolve()))

with open(PROJ_DIR / "pyproject.toml") as f:
    pyproj_file = toml.load(f)

# -- Project information -----------------------------------------------------
project = "{{ cookiecutter.project_name }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.org_name }}"
author = "{{ cookiecutter.org_name }}"
release = pyproj_file["tool"]["poetry"]["version"]

# -- General configuration ---------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "en"

source_suffix = [".rst", ".md", ".ipynb", ".myst"]
master_doc = "index"
pygments_style = "sphinx"
todo_include_todos = False

# -- Options for HTML output -------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "bodhilib": ("https://bodhilib.readthedocs.io/en/stable/", None),
}
autodoc_default_options = {
    "typehints": "description",
    "mock_imports": ["pydantic"],
    "members": True,
}
autoclass_content = "both"
html_theme_options = {
    "collapse_navigation": False,
}
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]
myst_url_schemes = ("http", "https", "mailto")
