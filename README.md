# Django-Recipe

# Build Dockerfile
docker build .

# Build Docker Compose
docker-compose build

# Run flake8 Lint
docker-compose run --rm app sh -c "flake8"

# Create Django Project via Docker Compose
docker-compose run --rm app sh -c "django-admin startproject app ."


# Run the service via Docker Compose
docker-compose up