# Installation and Configuration of Apache Tomcat on Ubuntu Server

## Project Objectives
- **Install Apache Tomcat on an Ubuntu Server**: Ensure that Apache Tomcat is correctly installed and configured to run as a service.
- **Configure Java Environment**: Set up the appropriate Java environment necessary for running Tomcat.
- **Implement Security Measures**: Secure the Tomcat installation by configuring user access, setting up a firewall, and implementing HTTPS.
- **Test and Verify Installation**: Verify that Tomcat is running correctly and is accessible.

## Project Phases

### 1. Planning and Preparation

#### 1.1. Determine Server Requirements
- **Ubuntu Version**: Ensure you are using a supported version of Ubuntu (e.g., Ubuntu 20.04 or 22.04).
- **Java Version**: Apache Tomcat 11 requires Java 17 or later.

#### 1.2. Prepare the Server
1. **Update the Server**:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
2. **Install Required Packages**:
    - Install `wget` and `tar` if they are not already installed.
    ```bash
    sudo apt install wget tar -y
    ```

### 2. Installation of Java

#### 2.1. Install OpenJDK
1. **Install OpenJDK 17**:
    ```bash
    sudo apt install openjdk-17-jdk -y
    ```
2. **Verify Java Installation**:
    ```bash
    java -version
    ```
    - You should see output similar to:
    ```
    openjdk version "17.x.x" 
    ```

### 3. Download and Extract Tomcat

#### 3.1. Download Tomcat Binary
1. **Download the Latest Tomcat 11 Release**:
    ```bash
    wget https://dlcdn.apache.org/tomcat/tomcat-11/v11.0.0-M24/bin/apache-tomcat-11.0.0-M24.tar.gz
    ```

#### 3.2. Extract the Archive
1. **Extract the Downloaded Archive**:
    ```bash
    sudo tar -xvf apache-tomcat-11.0.0-M24.tar.gz -C /opt/
    ```
2. **Rename the Directory for Simplicity**:
    ```bash
    sudo mv /opt/apache-tomcat-11.0.0-M24 /opt/tomcat
    ```

#### 3.3. Set Permissions
1. **Set the Correct Permissions**:
    ```bash
    sudo chown -R $USER:$USER /opt/tomcat
    sudo chmod +x /opt/tomcat/bin/*.sh
    ```

### 4. Configuration of Apache Tomcat

#### 4.1. Set Up Environment Variables
1. **Edit the Environment File**:
    ```bash
    sudo nano /etc/environment
    ```
2. **Add the Following Lines** (adjust the paths as necessary):
    ```bash
    JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
    CATALINA_HOME="/opt/tomcat"
    ```
3. **Reload the Environment Variables**:
    ```bash
    source /etc/environment
    ```

#### 4.2. Configure Tomcat as a Service
1. **Create a Systemd Service File**:
    ```bash
    sudo nano /etc/systemd/system/tomcat.service
    ```
2. **Add the Following Configuration**:
    ```ini
    [Unit]
    Description=Apache Tomcat 11
    After=network.target

    [Service]
    Type=forking

    Environment=JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
    Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
    Environment=CATALINA_HOME=/opt/tomcat
    Environment=CATALINA_BASE=/opt/tomcat
    Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
    Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

    ExecStart=/opt/tomcat/bin/startup.sh
    ExecStop=/opt/tomcat/bin/shutdown.sh

    User=$USER
    Group=$USER
    UMask=0007
    RestartSec=10
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
3. **Reload Systemd**:
    ```bash
    sudo systemctl daemon-reload
    ```
4. **Start and Enable the Tomcat Service**:
    ```bash
    sudo systemctl start tomcat
    sudo systemctl enable tomcat
    ```


#### Access Tomcat Interface
1. **Access Tomcat**:
    - Open a web browser and navigate to `http://your-server-ip:8080`.
    - You should see the Tomcat welcome page.

#### Check Logs
1. **View Tomcat Logs**:
    ```bash
    sudo tail -f /opt/tomcat/logs/catalina.out
    ```
    - Check for any errors or warnings.


---

## Summary

This guide provides a comprehensive step-by-step process for installing and configuring Apache Tomcat on an Ubuntu server. It covers everything from setting up Java, installing Tomcat, to verifying that the server is running correctly. Follow these instructions to ensure a successful deployment of Tomcat as a service on your server.

