PROJECT_NAME := OVH Package

SHELL            := /bin/bash
PACK             := ovh
ORG              := ovh
PROJECT          := github.com/${ORG}/ovhai-python-sdk
NODE_MODULE_NAME := @pulumi/${PACK}
TF_NAME          := ${PACK}
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

JAVA_GEN 		 := pulumi-java-gen
JAVA_GEN_VERSION := v0.8.0
TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-resource-${PACK}
VERSION         := $(shell pulumictl get version)

TESTPARALLELISM := 4

WORKING_DIR     := $(shell pwd)

OS := $(shell uname)
EMPTY_TO_AVOID_SED := ""

ensure::
	cd provider && go mod tidy
	cd sdk && go mod tidy
	cd examples && go mod tidy

prepare::
	@if test -z "${NAME}"; then echo "NAME not set"; exit 1; fi
	@if test -z "${REPOSITORY}"; then echo "REPOSITORY not set"; exit 1; fi

.PHONY: development provider build_sdks build_python cleanup

development:: install_plugins provider lint_provider build_sdks install_sdks cleanup # Build the provider & SDKs for a development environment

# Required for the codegen action that runs in pulumi/pulumi and pulumi/pulumi-terraform-bridge
build:: install_plugins provider build_sdks install_sdks
only_build:: build

tfgen:: install_plugins
	(cd provider && go build -o $(WORKING_DIR)/bin/${TFGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN})
	$(WORKING_DIR)/bin/${TFGEN} schema --out provider/cmd/${PROVIDER}
	(cd provider && VERSION=$(VERSION) go generate cmd/${PROVIDER}/main.go)

provider:: tfgen install_plugins # build the provider binary
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER})

build_sdks:: install_plugins provider build_python

build_python:: PYPI_VERSION := $(shell pulumictl get version --language python)
build_python:: install_plugins tfgen # build the python sdk
	$(WORKING_DIR)/bin/$(TFGEN) python --overlays provider/overlays/python --out sdk/python/
	cd sdk/python/ && \
        cp ../../README.md . && \
        python3 setup.py clean --all 2>/dev/null && \
        rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
        sed -i.bak -e 's/^VERSION = .*/VERSION = "$(PYPI_VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
        rm ./bin/setup.py.bak && \
        cd ./bin && python3 setup.py build sdist

$(WORKING_DIR)/bin/$(JAVA_GEN)::
	$(shell pulumictl download-binary -n pulumi-language-java -v $(JAVA_GEN_VERSION) -r pulumi/pulumi-java)

lint_provider:: provider # lint the provider code
	cd provider && golangci-lint run -c ../.golangci.yml

cleanup:: # cleans up the temporary directory
	rm -r $(WORKING_DIR)/bin
	rm -f provider/cmd/${PROVIDER}/schema.go

help::
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
 	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
 	expand -t20

clean::
	rm -rf sdk/{dotnet,nodejs,go,python}

install_plugins::
	[ -x $(shell which pulumi) ] || curl -fsSL https://get.pulumi.com | sh
	pulumi plugin install resource random 4.8.2

install_python_sdk::

install_sdks:: install_python_sdk

test::
	cd examples && go test -v -tags=all -parallel ${TESTPARALLELISM} -timeout 2h

