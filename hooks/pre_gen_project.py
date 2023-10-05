import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9\.]+$"

module_name = "{{ cookiecutter.project_package }}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name. "
        "Please use '_' instead" % module_name
    )

    # Exit to cancel project
    sys.exit(1)

service_class = r"^[A-Z]{1}[a-zA-Z0-9]+$"
service_class = "{{ cookiecutter.service_class }}"
if not re.match(service_class, service_class):
    print(
        "ERROR: The service_class (%s) is not valid. "
        + "Should be in camel-case and only contain alphanumeric characters."
        % service_class
    )

    # Exit to cancel project
    sys.exit(1)
