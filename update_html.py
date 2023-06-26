from github import Github
import os

g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
commit = repo.get_commit(os.getenv("COMMIT_SHA"))
message = commit.commit.message

path = "log.txt"

f = open(path,'w')
f.write(message)
f.close()