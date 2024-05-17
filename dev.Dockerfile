FROM python:3.11

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install

COPY . .

EXPOSE 8001

CMD ["pipenv", "run", "dev"]