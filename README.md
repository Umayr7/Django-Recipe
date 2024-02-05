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

# Command to Run Django Tests
docker-compose run --rm app sh -c "python manage.py test"

# Creating app
docker-compose run --rm app sh -c "python manage.py startapp core"

# Run Test
docker-compose run --rm app sh -c "python manage.py test" 

# Run wait_for_db management command with lint check
docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"