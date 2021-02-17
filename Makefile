install-assets:
	pip install -r requirements.txt

build-image: install-assets
	docker build -t toph-osint -f Dockerfile .

run-docker: build-image
	docker run --rm --tty --interactive toph-osint

run:
	python3 toph

.PHONY: install-assets build-image run-docker run