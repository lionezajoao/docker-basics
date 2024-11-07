# Docker Basics

Esse projeto foi feito para documentar os estudos básicos de Docker, explicando o que é containerização e passando pelos comandos e conceitos básicos da ferramenta. Sinta-se livre para contribuir e compartilhar. :)

## Conteúdo do Repositório

- [Dependências Necessárias](#dependências-necessárias)
- [Dependências Opcionais](#dependências-opcionais)
- [Slides do conteúdo](presentation.pdf)
- [Comandos Docker](#comandos-docker)
    - [Flags](#flags)
    - [Build](#build)
    - [Run](#run)
    - [Docker Compose](#docker-compose)

## Dependências Necessárias

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Dependências Opcionais:

Apenas caso queria executar o [aplicativo de exemplo](app/) localmente

- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Pipenv](https://pypi.org/project/pipenv/)

## Comandos Docker

Essa sessão se refere aos tipos de build e execução diferentes que podemos usar com Docker

### Flags

- Flag **-d**: executa o container em segundo plano
- Flag **--name**: configura o container com um nome específico (sem isso será usado nome genérico)
- Flag **--env-file**: define o arquivo de variáveis de ambiente a ser incorporado pelo container
- Flag **--network**: define o tipo de configuração de rede docker que o container utilizará
- Flag **docker-example:dev**: define o qual imagem e tag necessária para rodar o container

### Build

Buildando imagem com tag **dev**:
```shell
docker build -t docker-example:dev -f dev.Dockerfile .
```

Buildando imagem com tag **prod**:
```
docker build -t docker-example:prod -f prod.Dockerfile .
```

### Run


Executando tag **dev**:
```
# Flag de network host
docker run -d --name docker-example-dev --env-file .env.dev --network="host" docker-example:dev
```


```
# Flag de network padrão (bridge)
docker run -d --name docker-example-dev --env-file .env.dev -p 8001:8001 docker-example:dev
```

Executando tag **prod**:

```
docker run -d --name docker-example-prod --env-file .env.prod --network="host" docker-example:prod
```

```
docker run -d --name docker-example-prod --env-file .env.prod -p 8002:8000 docker-example:prod
```

### Docker Compose

- Build e execução: ```docker-compose up -d --build```
- Parar execução: ```docker-compose down```

