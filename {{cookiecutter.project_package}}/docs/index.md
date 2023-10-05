Welcome to {{ cookiecutter.project_name }}'s documentation!
{{ '=' * (cookiecutter.project_name|string|length + 28) }}

```{toctree}
:maxdepth: 2
:hidden:

installation
reference/{{ cookiecutter.project_package }}
```

{{ cookiecutter.project_name }} is a plugin for [bodhilib](https://github.com/bodhisearch/bodhilib) library. It adds the capability to {{ cookiecutter.project_short_description }}

# Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
