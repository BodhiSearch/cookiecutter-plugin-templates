#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    target = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(target):
        os.remove(target)

def remove_dir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)

if __name__ == '__main__':

    if '{{ cookiecutter.create_doc_files }}' != 'y':
        remove_dir('docs')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
