<p align='center'>
  <img width='400' heigth='450' src='https://user-images.githubusercontent.com/62605744/171186764-43f7aae0-81a9-4b6e-b4ce-af963564eafb.png'>
</p>

# SmartMarketPlace_backend
Web application for commercing products in stock and providing sales information

## Frontend-repository
https://github.com/Daga2001/SmartMarketPlace

## Authors
- Mauricio Carrillo
- David Alberto
- Camilo Ordoñez
- Alejandro Montero

## NOTES
- There're two branches, used to test github-actions workflows: test and test2.

## Requirements
It's mandatory to have some special tools and programming languages installed in your computer:
- Python
- requirements.txt (list a group of libraries, it's stored inside the backend folder, you may install it with pip)

## Pipeline: Python Application - Django Tests

This pipeline is triggered on pushes to the `develop` branch and also on pull requests targeting the `develop` branch.
Its function is to execute some tests regarding DB service and Django API.

### Pipeline Steps

1. Set up the PostgreSQL service: to check some tests later in 7th step.
2. Checkout the source code.
3. Set up Python 3.9.
4. Install dependencies.
5. Run migrations: to migrate our DB schema in PostgreSQL service.
6. Run the core app: here we run the DB service.
7. Run tests: here we test our web application, where a DB is required.

## Pipeline: Backend to Frontend Workflow

This pipeline is triggered on pushes to the `main` branch and also on pull requests targeting the `main` branch.
It was useful to push automatically backend content into features branch in frontend repository.

### Pipeline Steps

1. Checkout the front-end repository.
2. Set the back-end repository URL.
3. Fetch remote branches from the back-end repository.
4. Fetch the `main` branch from the back-end repository.
5. Set Git configuration for username and password.
6. Merge the back-end `main` branch with the current branch.
7. Set the front-end repository URL.
8. Debugging (outputting information about the current state).
9. Push changes to the front-end repository.
