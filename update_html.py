from github import Github
from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.main_tag = False
        self.html = ''

    def handle_starttag(self, tag, attrs):
        self.html += '<' + tag
        for attr in attrs:
            self.html += ' ' + attr[0] + '=' + '"' + attr[1] + '"'
        self.html += '>'
        if tag == 'main':
            self.main_tag = True

    def handle_endtag(self, tag):
        if self.main_tag and tag == 'main':
            self.main_tag = False
        if not self.main_tag:
            self.html += '</' + tag + '>'

    def handle_data(self, data):
        self.html += data

g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
commit = repo.get_commit(os.getenv("COMMIT_SHA"))
message = commit.commit.message

with open("index.html", "r") as f:
    html = f.read()

parser = MyHTMLParser()
parser.feed(html)
parser.html += f"<p>Last commit: {message}</p>"
parser.html += '</main>'

with open("index.html", "w") as f:
    f.write(parser.html)