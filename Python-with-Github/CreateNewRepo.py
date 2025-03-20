from github import Github

# token
token = "github_access_token"
g = Github(token)

user = g.get_user()

# Create New Repository
repo_name = "Python-Assignments"
repo = user.create_repo(repo_name)

print(f"Repository : {repo_name} Created Successfully")