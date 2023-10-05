from {{ cookiecutter.project_package }} import {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder, bodhilib_list_services


def test_bohilib_list_services():
    services = bodhilib_list_services()
    assert len(services) == 1
    service = services[0]
    assert service.service_name == "{{ cookiecutter.__service_module }}"
    assert service.service_type == "{{ cookiecutter.__service_type }}"
    assert service.version == "{{ cookiecutter.version }}"

def test_{{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder():
    service = {{ cookiecutter.__project_underscore}}_{{ cookiecutter.__service_type}}_service_builder(model="deep thought", api_key="424242")
    service.model = "deep thought"
    service.api_key = "424242"
