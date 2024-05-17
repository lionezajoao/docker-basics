# Docker

## Executando Dev

docker build -t docker-example:dev -f dev.Dockerfile .

docker run -d --name docker-example-dev --env-file .env.dev --network="host" docker-example:dev

docker run -d --name docker-example-dev --env-file .env.dev -p 8001:8001 docker-example:dev

## Executando Prod

docker build -t docker-example:prod -f prod.Dockerfile .

docker run -d --name docker-example-prod --env-file .env.prod --network="host" docker-example:prod

docker run -d --name docker-example-prod --env-file .env.prod -p 8002:8000 docker-example:prod

## Executando docker-compose

docker-compose up -d --build

docker-compose down

