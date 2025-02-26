# webui
# http://localhost:8080


up:
	mkdir -p ollama open-webui
	docker compose up -d --build --force-recreate
down:
	docker compose down

destroy:
	docker compose down -v

rebuild:
	docker compose stop ollama
	docker compose rm -f ollama
	docker compose build ollama
	docker compose up -d ollama

stop:
	docker compose stop
start:
	docker compose start


run-deepseek:
	docker compose exec -it ollama ollama run deepseek-r1:8b
run-llama:
	docker compose exec -it ollama ollama run llama3.2:3b

run-ollama3:
	docker compose exec -it ollama ollama run llama3


# pull-models:
# 	docker compose exec -it ollama ollama pull nomic-embed-text
# 	docker compose exec -it ollama ollama pull llama3.2:3b


# run-deepseek-r1-32b:
# 	docker compose exec -it ollama ollama run deepseek-r1:32b


# # Run a model
# docker compose exec -it ollama ollama run llama3.3
# # Pull a model
# docker compose exec -it ollama ollama pull llama3.3
# # Remove a model
# docker compose exec -it ollama ollama rm llama3.3
# # Copy a model
# docker compose exec -it ollama ollama cp llama3.3 my-model

prune:
	docker system prune -a -f