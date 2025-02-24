# webui
# http://localhost:8080


up:
	mkdir -p ollama open-webui
	docker compose up -d --build --force-recreate
down:
	docker compose down

destroy:
	docker compose down -v

stop:
	docker compose stop
start:
	docker compose start

run-ollama3:
	docker compose exec -it ollama ollama run llama3

run-ollama3-3:
	docker compose exec -it ollama ollama run llama3.3


prune:
	docker system prune -a -f