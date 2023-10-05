# Installation

## Requirements

The {{ cookiecutter.project_name }} requires Python 3.8 or above. You can download the latest version of Python [here](https://www.python.org/downloads/).


## Installing {{ cookiecutter.project_name }}

To install {{ cookiecutter.project_name }}, execute the following command in your terminal:

```shell
$ pip install {{ cookiecutter.project_package }}
```

This command will download the latest stable version of {{ cookiecutter.project_name }} along with its dependencies and install it on your system.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

We recommend using [poetry](https://python-poetry.org/) for managing your Python projects and their dependencies. Since the [bodhilib](https://github.com/bodhisearch/bodhilib) plugins are loaded at runtime dynamically from `sys.path`, sharing dependencies between projects can cause unforeseen issues. Also, bodhilib checks all the installed libraries when discovering plugins at boot time. Having a large number of packages installed might cause longer boot time.

To install using poetry, execute the following command in your terminal:

```shell
poetry add bodhilib
```

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [Github Repo](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_package}}).

You can either clone the public repository:

```shell
$ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_package }}
```

Or download the [tarball](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_package}}/tarball/master):

```shell
$ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_package }}/tarball/master
```

Once you have a copy of the source, you can install it with:

```shell
$ pip install poetry
$ poetry install
```

## Verifying the Installation

You can verify the installation by executing the following in your Python environment:

```python
import {{ cookiecutter.project_package }}
```

If the commands execute without an error, congratulations! You've successfully installed bodhilib along with its plugin package.
