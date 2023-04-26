# bored_cloud_engineer

A) Markdown Python script
B) Jenkins pipeline deployment

TASK 1
------
A bored cloud engineer comes to you and says he needs a Python script that will generate a Markdown file with suggestions for activities. The script should take a number between 1-100 as an input, which will indicate how many activity suggestions there will be. To generate the activities you should use the bored api: https://www.boredapi.com/.
 
The produced Markdown file should have in the first section a table of the 1-100 activities and all details that the boredapi produces:
Key | Type | Activity | Participants | Price | Link | Accessibility
xxx | xxxx | xxxxxx   | xxxxxxxxxx   | xxxxx | xxx  | xxxxxxx
xxx | xxxx | xxxxxx   | xxxxxxxxxx   | xxxxx | xxx  | xxxxxxx
 
Then the second section in the Markdown file will give some insights to the activities such as:
Most Participants: Hold a video game tournament with some friends (participants: 4)
Duplicate Activities: [here list of activities in case there are duplicates in the list, otherwise just "-"]
Most characters in Activity: Play football with your family and friends (characters: 42)
 
In the end you will have a markdown file with those two sections and the cloud engineer will be happy!
 
 
 
TASK 2
------
Another bored cloud engineer comes to you and asks you to deploy Jenkins for him. Only requirement is that it needs to run inside a container. You can use the official Jenkins Docker image (latest version is fine). You can either run it with Docker (option a) or if you want to totally impress the bored cloud engineer you can deploy it on Kubernetes (option b).
 
Instructions:
- Install Docker Desktop (free for private use): https://docs.docker.com/desktop/windows/install/
- Option a:
  - Use Jenkins Docker image: https://hub.docker.com/r/jenkins/jenkins
  - Run the Jenkins Docker container and see if you can access the application
- Option b:
  - Check how to deploy Kubernetes locallly on your computer using Docker Desktop: https://docs.docker.com/desktop/kubernetes/
  - Install Helm: https://helm.sh/docs/
  - Use Jenkins helm chart to deploy: https://github.com/jenkinsci/helm-charts
  - Once Jenkins is deployed see if you can access the application
 
 
Once you have Jenkins up and running it would be great if you created a Jenkins declarative pipeline as an example for the bored cloud engineer. The pipeline stages would be as follows:
- 1st stage does git clone on repository https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition
- 2nd stage lists the files in that repo
- 3rd stage sends an email with link to the build