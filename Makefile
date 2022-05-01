FLASK_HOST ?= 0.0.0.0
FLASK_PORT ?= 8081

all:
	make static

local:
	poetry run flask run -p ${FLASK_PORT} --host=${FLASK_HOST}

debug:
	FLASK_ENV=development make local

clean:
	-rm -rf templates/*.bak

##############

.PHONY: static
static:
	make build freeze

build:
	poetry run python app.py build

freeze:
	poetry run python app.py freeze

