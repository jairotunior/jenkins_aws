# Use the official Jenkins LTS image as the base
FROM jenkins/jenkins:lts

# Switch to root user to install system packages
USER root

# Update packages and install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip python3.13-venv gnupg wget build-essential 

# Switch back to the jenkins user
USER jenkins