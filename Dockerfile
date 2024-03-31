FROM python:3.9-buster as builder

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /src

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.9-slim-buster as runtime

ENV VIRTUAL_ENV=/src/.venv \
    PATH="/src/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /src

COPY ./ ./

ENV PYTHONPATH /src

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
