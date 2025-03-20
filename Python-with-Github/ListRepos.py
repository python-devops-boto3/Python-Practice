from github import Github

# token
token = "github_access_token"
g = Github(token)

user = g.get_user("devops-catchup")

# List All Repository
for repo in user.get_repos():
    print(f"Repository Name : {repo}")

