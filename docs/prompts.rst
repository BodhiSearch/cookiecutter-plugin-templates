Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

github_username
    Your GitHub username.

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.
    
project_package
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name. Note: your PyPi project and Travis links will use project_package, so change those in the README afterwards.

project_short_description
    A 1-sentence description of what your Python package does.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.
    
create_doc_files
    Whether to create documentation files
    
open_source_license
    Choose a `license <https://choosealicense.com/>`_. Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License 2.0, 5. GNU General Public License v3, 6. Not open source]
