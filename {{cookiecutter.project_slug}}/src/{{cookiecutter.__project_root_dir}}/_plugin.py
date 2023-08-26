from typing import Any, Dict, List, Optional

from bodhilib.plugin import Service, service_provider

from ._llm import {{ cookiecutter.__llm_class }}


@service_provider
def bodhilib_list_services() -> List[Service]:
    return [
        Service(
            service_name="{{ cookiecutter.__service_name }}",
            service_type="{{ cookiecutter.__service_type }}",
            publisher="{{ cookiecutter.org_name.lower() }}",
            service_builder={{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder,
            version="{{ cookiecutter.version }}",
        )
    ]


def {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder(
    *,
    service_name: Optional[str] = None,
    service_type: Optional[str] = "llm",
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    **kwargs: Dict[str, Any],
) -> {{ cookiecutter.__llm_class }}:
    return {{cookiecutter.__llm_class}}(model=model, api_key=api_key, **kwargs)
