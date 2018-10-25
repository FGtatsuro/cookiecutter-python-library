from setuptools import setup, find_packages
from pathlib import Path


# FYI: https://packaging.python.org/guides/making-a-pypi-friendly-readme/
with open(Path(__file__).parent.resolve()/'README.md') as f:
    readme = f.read()

# Ref: 
#    https://packaging.python.org/guides/distributing-packages-using-setuptools/
#    https://setuptools.readthedocs.io/en/latest/setuptools.html
# FYI: 
#    https://github.com/pypa/sampleproject/blob/master/setup.py
#    https://github.com/Pylons/pyramid-cookiecutter-starter/blob/latest/%7B%7Bcookiecutter.repo_name%7D%7D/setup.py
setup(
    name='{{cookiecutter.project_name}}',
    version='0.1.0',
    description='{{cookiecutter.project_description}}',

    # FYI: https://packaging.python.org/guides/making-a-pypi-friendly-readme/
    long_description=readme,
    long_description_content_type='text/markdown',

    url='https://github.com/{{cookiecutter.author}}/{{cookiecutter.project_name}}',
    author='{{cookiecutter.author}}',

    # Ref: https://pypi.org/classifiers
    classifiers=[
    ],
    keywords='',

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
    ],
    python_requires='>=3',
)
