run-web:
	poetry run python -m web

run-bot:
	poetry run python -m bot

run:
	make -j 2 run-bot run-web

setup:
	cd web && yarn && yarn build-tailwind
	poetry install
