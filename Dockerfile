ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION}

LABEL maintainer=swernst@gmail.com

WORKDIR /support

COPY pyproject.toml .
COPY README.md .

RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root

COPY locusts /support/locusts

RUN poetry config virtualenvs.create false \
 && poetry install

WORKDIR /scripts

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

ENTRYPOINT ["locusts", "run"]
