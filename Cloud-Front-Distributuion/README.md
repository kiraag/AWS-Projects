# AWS CloudFront Distribution Project

## Project Overview

This project involves the creation and deployment of an **AWS CloudFront distribution** with integration into **Route 53** and an **Application Load Balancer** to serve content from a backend application hosted on **EC2 instances**.

### Architecture Diagram

![Architecture Diagram](link-to-image-on-github)

This diagram illustrates the architecture of the project:

- **Users**: End-users accessing the web application.
- **Route 53**: DNS service routing user requests to the CloudFront distribution.
- **CloudFront**: Content Delivery Network (CDN) that caches content at edge locations to reduce latency and improve delivery speed.
- **Application Load Balancer**: Distributes incoming traffic across multiple EC2 instances running the web application.
- **App Server**: EC2 instances hosting the application.

## Key Components

### AWS Route 53
- Domain name setup.
- DNS routing policies.

### AWS CloudFront
- Origin setup pointing to the load balancer.
- Cache behavior settings.
- SSL/TLS configuration for secure communication.

### Application Load Balancer
- Creation of a load balancer.
- Adding EC2 instances as targets.
- Health checks configuration.

### EC2 Instances
- Launching and configuring EC2 instances.
- Deploying the application code.

## Setup and Configuration

### 1. Route 53 Configuration
   - Set up the domain name.
   - Configure DNS routing policies.

### 2. CloudFront Distribution Setup
   - Configure origin to point to the load balancer.
   - Set up cache behavior settings.
   - Enable SSL/TTLS for secure communication.

### 3. Application Load Balancer Configuration
   - Create an application load balancer.
   - Register EC2 instances as targets.
   - Configure health checks.

### 4. EC2 Instances Setup
   - Launch EC2 instances.
   - Deploy the application code on EC2 instances.

## How to Deploy

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/repository-name.git

