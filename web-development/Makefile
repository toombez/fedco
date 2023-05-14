setup-venv:
	python -m venv venv
	venv\Scripts\activate
	make install

install:
	pip install -r requirements.txt

run-web:
	cd web && python -m flask run
