# Configuring an EC2 Instance as a Web Server with Nginx Using User Data Script

## Overview
This project demonstrates how to configure an Amazon EC2 instance as a web server running Nginx using a user data script during instance launch. The script automates the installation and setup of Nginx, making the web server accessible immediately after the instance is launched.

## Steps

### 1. Launch EC2 Instance
- Go to the **AWS Management Console** and launch a new EC2 instance.
- Choose **Amazon Linux 2** or **Ubuntu** as the AMI.
- Select an appropriate instance type (e.g., `t2.micro` for free-tier eligibility).
- Configure the security group to allow inbound traffic for:
  - **SSH (port 22)** for remote access.
  - **HTTP (port 80)** for web traffic.

### 2. Add User Data Script
In the **Advanced Details** section of the instance configuration, add the following user data script to automate the installation and configuration of Nginx:

```bash
#!/bin/bash
# Update package repositories
sudo yum update -y   # Use 'apt update' for Ubuntu.

# Install Nginx
sudo yum install nginx -y   # Use 'apt install nginx -y' for Ubuntu.

# Start Nginx service
sudo systemctl start nginx
sudo systemctl enable nginx

# Create a basic HTML page
echo "<h1>Hello from Nginx!</h1>" | sudo tee /usr/share/nginx/html/index.html
```
## 3. Launch and Access

1. **Complete the EC2 launch process.**
2. Once the instance is running, obtain the **Public IP** from the EC2 dashboard.
3. Open a browser and visit `http://<EC2_Public_IP>` to view the Nginx welcome page.

### Key Points

- **Automated Setup**: The user data script ensures Nginx is installed and configured automatically during instance launch.
- **Web Access**: The server is accessible via the EC2 public IP immediately after the instance is running.

### Usage

This setup is suitable for hosting static web content or simple web applications on an EC2 instance, eliminating the need for manual configuration after launch.

### References

- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Nginx Documentation](https://nginx.org/en/docs/)
