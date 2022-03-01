import setuptools
from os import path

kwargs = {
    "version": "{{ cookiecutter.package_version }}",
}

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
all_reqs = []
requirements_file = path.join(here, "requirements.txt")
if path.isfile(requirements_file):
    with open(requirements_file, encoding="utf-8") as f:
        all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.package_description }}",
    long_description=open("README.rst").read(),
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Healthcare Industry",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={
        "chemocompile_plugin": [
            "{{ cookiecutter.package_name }}={{ cookiecutter.package_slug }}:register_plugin"
        ],
    },
    **kwargs
)
