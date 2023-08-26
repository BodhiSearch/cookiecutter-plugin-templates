"""{{ cookiecutter.project_name }} LLM service package."""
from ._llm import {{ cookiecutter.__llm_class }} as {{ cookiecutter.__llm_class }}
from ._plugin import {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder as {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder
from ._plugin import bodhilib_list_services as bodhilib_list_services

__version__ = "{{ cookiecutter.version }}"
