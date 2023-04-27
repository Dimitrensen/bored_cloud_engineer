# Instructions for installing Docker in one's system: https://docs.docker.com/engine/install/

# Pull the latest Jenkins Docker image:
docker pull jenkins/jenkins

# Once the image is downloaded start a new Jenkins container:
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins

# Access web interface: http://localhost:8080 & complete the Jenkins setup wizard.

# Login: Jenkins initial setup is required. An admin user has been created and a password generated.

# This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

# Create a new Jenkins job by clicking on "New Item" on the Jenkins dashboard and selecting "Pipeline" from the options.

# Input the code as shown on the Jenkinsfile in the pipeline script section

# Because we are using a public repo, I am just using a shell command git clone to clone the public repo

# If we were using a private repo, we'd need to set up credentials with github keys(SSH) and use the commented section inside Jenkinsfile

# Save the pipeline and run it by clicking on "Build Now" on the Jenkins dashboard

# Once the build is complete, you should receive an email with a link to the build.

# With this way every step is manual, however it would be recommended to use Configuration as Code, to manage Jenkins something like the plugin JCASC App.