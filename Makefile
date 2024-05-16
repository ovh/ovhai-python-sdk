PROJECT_NAME := OVH Package

SHELL            := /bin/bash
PACK             := ovh
ORG              := ovh
PROJECT          := github.com/${ORG}/ovhai-python-sdk
TF_NAME          := ${PACK}
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version
VERSION         := $(shell ovhai get version)

WORKING_DIR     := $(shell pwd)

OS := $(shell uname)
EMPTY_TO_AVOID_SED := ""

PHONY: build_python
development:: build_sdks install_sdks # Build the provider & SDKs for a development environment

build:: build_sdks install_sdks
build_sdks: build_python

build_python:: PYPI_VERSION := $(shell ovhai get version --language python)
build_python:: install_plugins tfgen # build the python sdk
	$(WORKING_DIR)/bin/$(TFGEN) python --overlays provider/overlays/python --out sdk/python/
	cd sdk/python/ && \
        cp ../../README.md . && \
        python3 setup.py clean --all 2>/dev/null && \
        rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
        sed -i.bak -e 's/^VERSION = .*/VERSION = "$(PYPI_VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
        rm ./bin/setup.py.bak && \
        cd ./bin && python3 setup.py build sdist

install_python_sdk::

