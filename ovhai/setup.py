import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()


def readme():
    try:
        with open('../README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "ovhai Package - Development Version"


setup(
    name="ovhai",
    version="0.1a1",
    description="A client library for accessing OVHcloud's AI Solutions",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='ovhai ovh AI',
    project_urls={
          'Repository': 'https://github.com/ovh/ovhai-python-sdk'
      },
    license='Apache-2.0',
    packages=find_packages(),
    python_requires=">=3.8, <4",
    install_requires=["httpx >= 0.20.0, < 0.28.0", "attrs >= 21.3.0", "python-dateutil >= 2.8.0, < 3"],
    package_data={"ovhai": ["py.typed"]},
    zip_safe=False
)
