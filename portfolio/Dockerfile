FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 8020

CMD ["poetry", "run", "uvicorn", "src.application.server:app_portfolio", "--host", "0.0.0.0", "--port", "8020"]
