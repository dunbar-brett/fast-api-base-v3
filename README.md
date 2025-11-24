# Base Template API (FastAPI)

Base Template API:
- FastAPI basic todo app
- Tests using pytest

## Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/)
- Docker
- Docker Compose
- Pyenv or another virtual environment for Python recommended

## Setup Instructions

1. **Install Dependencies**
    ```bash
    make install
    ```

2. **Build DB Container, Create Tables, and Seed DB**
    ```bash
    make build-db
    ```

3. **Run API locally**
    ```bash
    make run
    ```


Server is running in `http://localhost:8000/`

Go to `http://localhost:8000/docs` for a swagger UI showing all endpoints and response models with documentation.


## Other Useful Make commands

**Run Tests**

While DB container is running, creating tables and seeding is recommended but not required.

```bash
make test
```

**Run coverage for tests**

```bash
make coverage
```

**To open coverage report in browser**

```bash
make show-coverage
```

**Make DB tables in Container**

```bash
make create-tables
```

**Seed DB in Container**

```bash
make seed
```

**Start DB in container**

```bash
make db
```

**Make DB tables in Container**

```bash
make create-tables
```

**Seed DB in Container**

```bash
make seed
```

**Create Tables and Seed DB in Container and start API locally**

```bash
make dev
```