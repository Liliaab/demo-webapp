# Web Application Project

A simple Python Flask web application containerized with Docker and designed for deployment on AWS App Runner.

## Overview

This application serves a lightweight Flask web app behind a Gunicorn WSGI server, packaged in a Docker container. It listens on port **8080** and returns a greeting message at the root endpoint.

Developer Push code  --> GitHub Repository --> triggers Github Actions (CI/CD) --> Build Docker Image --> push image to EDR registry --> AWS App Runner deploy the changes  --> web app

## CI/CD Pipeline

This project uses **GitHub Actions** to automatically build and deploy the application on every push to the `main` branch. The workflow (`.github/workflows/deploy.yml`) performs the following steps:

1. **Checkout** — clones the repository.
2. **Configure AWS credentials** — authenticates using secrets stored in the GitHub repository.
3. **Login to Amazon ECR** — authenticates Docker with the ECR registry.
4. **Build** — builds the Docker image.
5. **Tag & Push** — tags the image and pushes it to the `lilia_webapp` ECR repository.

### Required GitHub Secrets

| Secret                  | Description                     |
|-------------------------|---------------------------------|
| `AWS_ACCESS_KEY_ID`     | IAM access key ID               |
| `AWS_SECRET_ACCESS_KEY` | IAM secret access key           |
| `AWS_SESSION_TOKEN`     | Temporary session token         |
| `AWS_REGION`            | AWS region  |


## AMAZON Elastic container registery

An Amazon ECR private registry hosts your container images in a highly available and scalable architecture.

## Deploying to AWS App Runner
AWS App Runner takes your source code or source image from a repository, and creates and maintains a running web service for you in the AWS Cloud.
1. Push to the `main` branch — the GitHub Actions pipeline builds and pushes the Docker image to Amazon ECR.
2. AWS App Runner detects the new image and automatically deploys the updated application.


## Dependencies

- **Flask** — web framework
- **Gunicorn** — production WSGI server
