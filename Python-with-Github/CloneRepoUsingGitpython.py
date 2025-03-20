import git
import git.repo

# Define the url that we need to clone 
Repo_url = "https://github.com/devops-catchup/LoginWebAppApplicationWith-Docker.git"

# Define the Directory where we need to clone Repository
Clone_Dir = "/workspaces/Python-practice/Python-with-Github/Repos"

try:
    git.Repo.clone_from(Repo_url, Clone_Dir)
    print(f"Repository has been cloned successfully into the {Clone_Dir}")
except git.GitError as e:
    print(f"Error cloning the Repository: {e}")
