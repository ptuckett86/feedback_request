import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-app-feedback",
    version="2.1.0",
    install_requires=[
        "djangorestframework==3.11.0",
        "drf-flex-fields==0.8.5",
        "Pillow==6.0.0",
        "Django>=3.0.7",
        "pytz==2019.1",
        "sqlparse==0.3.0",
        "six==1.15.0",
        "django_filter==2.3.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    license="",  # example license
    description="A Django app for users to leave feedback about your app.",
    long_description=README,
    url="",
    author="Paul Tuckett",
    author_email="",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: X.Y",  # replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
