# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Install Poetry
RUN pip install poetry

# Create a working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock .env /app/

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

RUN pip install pymilvus

# Copy the rest of the application code
COPY src /app/src

# Expose the port that the app will run on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "src.endpoint:app", "--host", "0.0.0.0", "--port", "8000"]