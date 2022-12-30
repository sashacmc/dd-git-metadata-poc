import os
from setuptools import setup


def get_long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    return long_description


setup(
    name="ddgitmetadata",
    version="1.0.0",
    description="Datadog Git Metadata embedding library",
    url="https://github.com/DataDog/TODO",
    package_urls={
        "Changelog": "https://TODO",
        "Documentation": "https://TODO",
    },
    project_urls={
        "Bug Tracker": "https://github.com/DataDog/TODO",
        "Source Code": "https://github.com/DataDog/TODO",
        "Changelog": "https://TODO",
        "Documentation": "https://TODO",
    },
    author="Datadog, Inc.",
    author_email="dev@datadoghq.com",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="BSD",
    packages=["ddgitmetadata"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe=True,
)
