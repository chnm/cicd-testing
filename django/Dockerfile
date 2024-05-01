# Pull base image for Python 3.11
FROM python:3.11

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# add path to poetry binary
ENV PATH="$PATH:/root/.local/bin"

# Set working directory
WORKDIR /app

# Copy project
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
#RUN poetry install --no-root #--no-dev

FIZZBUZZ

CMD poetry run python manage.py runserver 0.0.0.0:8000
