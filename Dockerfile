FROM python:3.10-slim

WORKDIR /app

# system deps for building some packages
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* README.md /app/

# install poetry
RUN pip install --no-cache-dir poetry

# install dependencies in the image
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi --without dev

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "todo_app.main:app", "--host", "0.0.0.0", "--port", "8000"]