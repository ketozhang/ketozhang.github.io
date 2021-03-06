FLASK_HOST ?= 0.0.0.0
FLASK_PORT ?= 8080

local:
	poetry run flask run -p ${FLASK_PORT} --host=${FLASK_HOST}

debug:
	FLASK_ENV=development make local

.PHONY: static
static:
	make build freeze

build:
	poetry run python app.py build

freeze:
	poetry run python app.py freeze

