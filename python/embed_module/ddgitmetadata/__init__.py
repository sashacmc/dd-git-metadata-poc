import os
import subprocess


def __query_git(args):
    try:
        p = subprocess.Popen(["git"] + args, stdout=subprocess.PIPE)
    except EnvironmentError:
        print("Couldn't run git")
        return
    ver = p.communicate()[0]
    return ver.strip().decode("utf-8")


def __get_commit_sha():
    return __query_git(["rev-parse", "HEAD"])


def __convert_url(url):
    # TODO: convert url to https://
    return url


def __get_repository_url():
    return __convert_url(__query_git(["config", "--get", "remote.origin.url"]))


def __add_project_urls(setup):
    source_code_link = __get_repository_url() + "#" + __get_commit_sha()

    def patch(**attrs):
        if "project_urls" not in attrs:
            attrs["project_urls"] = {}
        attrs["project_urls"]["source_code_link"] = source_code_link
        return setup(**attrs)

    return patch


import distutils.core

distutils.core.setup = __add_project_urls(distutils.core.setup)

import setuptools

setuptools.setup = __add_project_urls(setuptools.setup)
