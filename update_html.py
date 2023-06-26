from github import Github
import os
import datetime

dt_now = datetime.datetime.now()

g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
commit = repo.get_commit(os.getenv("COMMIT_SHA"))
message = commit.commit.message
now = str(dt_now)
now = now.replace(" ","-")
now = now.replace(":","-")
now = now.replace(".","-")

path = now + ".md"

f = open(path,'w')
f.write(message)
f.close()