PROJECT_NAME := OVH Package

SHELL            := /bin/bash
PACK             := ovh
ORG              := ovh
PROJECT          := github.com/${ORG}/ovhai-python-sdk
NODE_MODULE_NAME := @ovhai/${PACK}
TF_NAME          := ${PACK}
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

VERSION         := $(shell ovhai get version)

TESTPARALLELISM := 4

WORKING_DIR     := $(shell pwd)

OS := $(shell uname)
EMPTY_TO_AVOID_SED := ""

prepare::
	@if test -z "${NAME}"; then echo "NAME not set"; exit 1; fi
	@if test -z "${REPOSITORY}"; then echo "REPOSITORY not set"; exit 1; fi

.PHONY: development build_sdks build_python cleanup

development:: build_sdks install_sdks cleanup # Build SDK for a development environment

build:: build_sdks install_sdks
only_build:: build

build_sdks:: build_python

build_python:: PYPI_VERSION := $(shell ovhai get version --language python)
build_python:: # build the python sdk
	cd sdk/python/ && \
        cp ../../README.md . && \
        python3 setup.py clean --all 2>/dev/null && \
        rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
        sed -i.bak -e 's/^VERSION = .*/VERSION = "$(PYPI_VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
        rm ./bin/setup.py.bak && \
        cd ./bin && python3 setup.py build sdist

cleanup:: # cleans up the temporary directory
	rm -r $(WORKING_DIR)/bin

help::
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
 	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
 	expand -t20

clean::
	rm -rf sdk/{python}

install_python_sdk::

install_sdks:: install_python_sdk

