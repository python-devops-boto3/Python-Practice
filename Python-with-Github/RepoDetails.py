from github import Github

# token
token = "github_access_token"
g = Github(token)

# fetch the Github UserName
user = g.get_user()
print(f"username : {user.login}")

# fetch all public repos
print(f"Public Repos : {user.public_repos}")

# fetch the followers on github account
print(f"Followers: {user.followers}")



