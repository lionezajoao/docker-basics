# Docker

## Executando Dev

docker build -t docker-example:dev -f dev.Dockerfile .
docker run -d --name docker-example-dev --env-file .env.dev --network="host" docker-example:dev
docker run -d --name docker-example-dev --env-file .env.dev -p 8001:8001 docker-example:dev

## Executando Prod

docker build -t docker-example:prod -f prod.Dockerfile .
docker run -d --name docker-example-prod --env-file .env.prod --network="host" docker-example:prod
docker run -d --name docker-example-prod --env-file .env.prod -p 8000:8000 docker-example:prod

## Executando docker-compose

docker-compose up -d --build
docker-compose down


- O que é container
- container x VM
- O que é Docker
- Entendendo Dockerfile
- Sintaxe
- Imagem docker
- docker build
- docker run
- docker logs
- interação com docker (docker exec -it)
- Entendendo docker-compose.yml
- Executando mais de um docker ao mesmo tempo
- docker network (breve)
- Docker Hub e docker push
