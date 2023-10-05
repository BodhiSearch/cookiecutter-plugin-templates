{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}


{% if is_open_source %}
![pypi](https://img.shields.io/pypi/v>/{{ cookiecutter.project_package }}.svg)

![[ci](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_package }}.svg)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_package }})

![[Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_package | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_package | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)

{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
\* Free software: {{ cookiecutter.open_source_license }}
\* Documentation: <https:/>/{{ cookiecutter.project_package | replace("\_", "-") }}.readthedocs.io.
{% endif %}

# Features

- TODO

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) forked and modified at [BodhiSearch/cookiecutter-plugin-template](https://github.com/BodhiSearch/cookiecutter-plugin-template).
