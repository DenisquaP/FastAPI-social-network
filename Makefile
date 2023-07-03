linux_up:
	pip install -r requirements.txt && sudo docker compose up -d && cd app && alembic upgrade head && uvicorn main:app --reload
windows_up:
	pip install -r requirements.txt && docker-compose up -d && cd app && alembic upgrade head && uvicorn main:app --reload
linux_down:
	sudo docker compose down
windows_down:
	docker-compose down