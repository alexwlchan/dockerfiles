export ROOT = $(shell git rev-parse --show-toplevel)
export TWINE = $(ROOT)/twine
export TWINE_IMAGE = greengloves/twine
export TWINE_VERSION = $(shell cat $(TWINE)/requirements.in | tr '=' ' ' | awk '{print $$2}')


$(TWINE)/requirements.txt: $(TWINE)/requirements.in
	docker run --volume $(TWINE):/src micktwomey/pip-tools

$(ROOT)/.docker/twine: $(TWINE)/Dockerfile $(TWINE)/requirements.txt
	docker build --tag $(TWINE_IMAGE) $(TWINE)
	mkdir -p $(ROOT)/.docker && touch $(ROOT)/.docker/twine

twine-build: $(ROOT)/.docker/twine

twine-publish: twine-build
	docker push $(TWINE_IMAGE):latest
	docker tag $(TWINE_IMAGE):latest $(TWINE_IMAGE):$(TWINE_VERSION)
	docker push $(TWINE_IMAGE):$(TWINE_VERSION)


.PHONY: twine-build twine-publish
