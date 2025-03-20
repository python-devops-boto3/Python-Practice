import subprocess

# Define the url that we need to clone 
Repo_url = "https://github.com/devops-catchup/LoginWebAppApplicationWith-Docker.git"

# Define the Directory where we need to clone Repository
Clone_Dir = "/workspaces/Python-practice/Python-with-Github/Clone-Repos"

# Run the git clone using SubProcess Module
subprocess.run(["git", "clone", Repo_url, Clone_Dir])

