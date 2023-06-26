from github import Github
import os
import datetime

dt_now = datetime.datetime.now()

g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
commit = repo.get_commit(os.getenv("COMMIT_SHA"))
message = commit.commit.message

path = str(dt_now) + ".md"

f = open(path,'w')
f.write(message)
f.close()