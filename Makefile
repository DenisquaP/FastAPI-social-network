linux_up:
	sudo docker compose up -d && cd app && alembic upgrade head && uvicorn main:app --reload
windows_up:
	docker-compose up -d && cd app && alembic upgrade head && uvicorn main:app --reload
linux_down:
	sudo docker compose down
windows_down:
	docker-compose down