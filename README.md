# Student Performance Predictor


An end-to-end machine learning application designed to predict student performance. This project features a Flask web application deployed on AWS, using Docker for containerization and AWS services for continuous integration and deployment.

## Table of Contents

Prerequisites
Setup Instructions
Accessing the Web Application
Troubleshooting


The Student Performance Predictor is a web application built with Flask that provides insights and visualizations on student performance data. The application is containerized using Docker, and deployed on an AWS EC2 instance using Amazon ECR for storage and AWS CLI for management.

### Prerequisites

Before setting up the application, make sure you have the following:

AWS Account: An active AWS account with access to ECR and EC2 services.

AWS CLI: AWS Command Line Interface installed and configured with your credentials.
Docker: Docker installed and running on your local machine.
Git: Git installed for cloning the repository.
Environment Variables

Ensure the following environment variables are configured in your AWS environment:

Variable Name	Description
AWS_ACCESS_KEY_ID	Your AWS access key ID.
AWS_SECRET_ACCESS_KEY	Your AWS secret access key.
AWS_REGION	The AWS region where your resources are located.
AWS_ECR_LOGIN_URI	Your ECR login URI, e.g., 203918856764.dkr.ecr.us-east-2.amazonaws.com/studentperformance_app.
ECR_REPOSITORY_NAME	Name of your ECR repository, e.g., studentperformance_app.
Setting Environment Variables in GitHub Actions
Go to Settings > Security > Actions and add the necessary secret keys for GitHub Actions to access your AWS resources.

### Setup Instructions


1. Set Up Docker on Your EC2 Instance
Log into your EC2 instance and run the following commands to set up Docker:

```bash
Copy code
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker
```
 
 2.Set Up a Self-Hosted Runner for GitHub Actions
To set up a self-hosted runner:

Go to your GitHub repository: Settings > Actions > Runners.
Click New self-hosted runner and follow the instructions provided to set up the runner on your EC2 instance.
Deployment to AWS

1. Login to Amazon ECR
Run the following command to log in to Amazon ECR:

```bash
Copy code
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com
2. Build, Tag, and Push Docker Image to ECR
bash
Copy code
docker build -t studentperformance_app .
docker tag studentperformance_app:latest <aws-account-id>.dkr.ecr.<region>.amazonaws.com/studentperformance_app:latest
docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/studentperformance_app:latest
```
3. Run the Application on EC2
After pulling the Docker image on your EC2 instance, run:

``` bash
#Copy code
docker run -d -p 5000:5000 --name studentperformance_app <aws-account-id>.dkr.ecr.<region>.amazonaws.com/studentperformance_app:latest
```
Ensure that the EC2 instance's security group allows inbound HTTP traffic on port 5000.

### Accessing the Web Application

Once the application is running, you can access it via your web browser:

Home Page: http://<public-ip-of-ec2-instance>:5000
Predictor Page: http://<public-ip-of-ec2-instance>:5000/predictdata
Replace <public-ip-of-ec2-instance> with the public IP address of your EC2 instance.

### Troubleshooting

Port Accessibility: Ensure that port 5000 is open in your EC2 instance's security group settings.
Permissions: Make sure your AWS credentials have the necessary permissions to access ECR and EC2.
Environment Variables: Double-check that all environment variables are correctly set.
