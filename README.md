<p align='center'>
  <img width='400' heigth='450' src='https://user-images.githubusercontent.com/62605744/171186764-43f7aae0-81a9-4b6e-b4ce-af963564eafb.png'>
</p>

# SmartMarketPlace
Web application for commercing products in stock and providing sales information

## Backend-repository
https://github.com/Daga2001/SmartMarketPlace_backend

## Authors
- Mauricio Carrillo
- David Alberto
- Camilo Ordoñez
- Alejandro Montero

## Requirements
It's mandatory to have some special tools and programming languages installed in your computer:
- Python
- Node
- requirements.txt (list a group of libraries, it's stored inside the backend folder, you may install it with pip)

## Pipeline: Despliegue en GKE
This pipeline is triggered on pushes to the `main` or `hotfix` branches and 
also on pull requests targeting those branches. It's used to deploy our web application into a production environment.

### Pipeline Steps

1. Checkout the source code.
2. Configure Google Cloud SDK: to install the Google CLI in github's environment.
3. Authenticate with Google Cloud: to authenticate my account with some credentials from Google Cloud.
4. Select Google Cloud account: to specify which account to use.
5. Authenticate with GKE: to check the kubernetes cluster.
6. Deploy to GKE: the final step, the deployment, where we apply changes to our cluster.

## Pipeline: Build

This pipeline is triggered on any push to any branch or any pull request event. Used to scan our
web application for debugging purposes.

### Pipeline Steps

1. Set up the PostgreSQL service: to check some tests later in 7th step.
2. Checkout the source code.
3. Set up Python 3.9.
4. Install dependencies.
5. Run migrations: to migrate our DB schema in PostgreSQL service.
6. Run the core app: here we run the DB service.
7. Run tests: here we test our web application, where a DB is required.
8. Run coverage: returns the results and we read it in sonarcloud.
9. Perform SonarCloud scan: this will allows us monitoring our application, i.e. To check the coverage of our tests.

![image](https://github.com/Daga2001/SmartMarketPlace/assets/62605744/aeb8fd85-d4a7-4831-8c7e-6ab372499891)

## Pipeline: Django API and WEB Application - Docker Push

This pipeline is triggered on pushes to the `main` or `hotfix` branches and also on pull requests targeting those branches.
It's used to deploy our web application into a testing environment.

### Tests - steps

1. Set up the PostgreSQL service.
2. Checkout the source code.
3. Set up Python 3.9.
4. Install dependencies.
5. Run migrations.
6. Run the core app.
7. Run tests.

### Build and Push Docker - steps

9. Checkout the source code.
10. Log in to Docker Hub.
11. Build Docker images.
12. List Docker images: for debugging purposes, but not relevant at all for the pipeline itself.
13. Push Docker images.
14. Send email notification: this last pipeline is executed only when the application is successfully deployed.

