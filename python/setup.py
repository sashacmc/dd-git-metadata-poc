#!/usr/bin/env python

# patch setup method
import ddtrace.gitmetadata

from setuptools import setup

setup(
    name="gitmetadatapoc",
    version="1.0",
    description="Python Test",
    author="First Last",
    author_email="example@mail.net",
    packages=["git_metadata_poc"],
    project_urls={
        "Bug Tracker": "https://bug.tracker.link",
        "Documentation": "https://some.documentation.link/",
        "Source Code": "https://github.com/sashacmc/dd-git-metadata-poc",
    },
    zip_safe=True,
)
