"""{{ cookiecutter.project_name }} LLM service package."""
from ._{{ cookiecutter.__service_module }} import {{ cookiecutter.service_class }} as {{ cookiecutter.service_class }}
from ._{{ cookiecutter.__service_module }} import {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder as {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder
from ._{{ cookiecutter.__service_module }} import bodhilib_list_services as bodhilib_list_services

from ._version import __version__ as __version__

__all__ = ["{{ cookiecutter.service_class }}", "{{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder", "bodhilib_list_services"]
