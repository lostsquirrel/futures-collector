SHELL=/bin/bash
VERSION=0.2.3

VERSION_TAG=$(VERSION)
REGISTRY=registry.cn-hangzhou.aliyuncs.com
IMAGE=$(REGISTRY)/lisong/kline
VERSIONED_IMAGE=$(IMAGE):$(VERSION_TAG)

export VERSION
export VERSIONED_IMAGE

push:
	docker push $(VERSIONED_IMAGE)

pull:
	docker pull $(VERSIONED_IMAGE)

build:
	docker build --no-cache -t $(VERSIONED_IMAGE) .

restart:
	docker-compose restart

clean:
	docker-compose down
	docker-compose rm --force

code:
	cd futures-collector && git pull

update:
	git pull
up:
	docker-compose up -d

.PHONY: build clean  push up
