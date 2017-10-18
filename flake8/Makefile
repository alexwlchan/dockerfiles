export ROOT = $(shell git rev-parse --show-toplevel)
export FLAKE8 = $(ROOT)/flake8
export FLAKE8_IMAGE = greengloves/flake8
export FLAKE8_VERSION = $(shell cat $(FLAKE8)/requirements.in | tr '=' ' ' | awk '{print $$2}')


$(FLAKE8)/requirements.txt: $(FLAKE8)/requirements.in
	docker run --volume $(FLAKE8):/src micktwomey/pip-tools

$(ROOT)/.docker/flake8: $(FLAKE8)/Dockerfile $(FLAKE8)/requirements.txt
	docker build --tag $(FLAKE8_IMAGE) $(FLAKE8)
	mkdir -p $(ROOT)/.docker && touch $(ROOT)/.docker/flake8

flake8-build: $(ROOT)/.docker/flake8

flake8-version:
	@echo $(FLAKE8_VERSION)

flake8-publish: flake8-build
	docker push $(FLAKE8_IMAGE):latest
	docker tag $(FLAKE8_IMAGE):latest $(FLAKE8_IMAGE):$(FLAKE8_VERSION)
	docker push $(FLAKE8_IMAGE):$(FLAKE8_VERSION)


.PHONY: flake8-build flake8-publish flake8-version
