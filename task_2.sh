# Instructions for installing Docker in one's system: https://docs.docker.com/engine/install/

# Pull the latest Jenkins Docker image:
docker pull jenkins/jenkins

# Once the image is downloaded start a new Jenkins container:
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins

# Access web interface: http://localhost:8080 & complete the Jenkins setup wizard.

# Login: Jenkins initial setup is required. An admin user has been created and a password generated.
# Please use the following password to proceed to installation:

# 8851854ad9fa49d7aa941dafefdc01e4

# This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

# Create a new Jenkins job by clicking on "New Item" on the Jenkins dashboard and selecting "Pipeline" from the options.