remove-assets:
	pip3 uninstall -r requirements.txt -y

install-assets: remove-assets
	pip3 install -r requirements.txt

build-image: install-assets
	docker build -t toph-osint -f Dockerfile .

run-docker: build-image
	docker run --rm --tty --interactive toph-osint

run:
	python3 -m toph

test:
	pytest --cov=toph -vv toph/tests/

.PHONY: install-assets build-image run-docker run test