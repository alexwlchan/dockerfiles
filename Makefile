include flake8/Makefile
include twine/Makefile

update-requirements: $(FLAKE8)/requirements.txt $(TWINE)/requirements.txt

check-requirements: update-requirements
	git diff --exit-code
