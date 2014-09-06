from github3 import login
from getpass import getpass

user = 'k3rn3l-'
pw = getpass("Password : ")
gh = login(user, pw)

while True:
	issues = gh.iter_repo_issues(user, 'GitLearning', milestone=None, state=None, 
		assignee=None, mentioned=None, labels=None, sort=None, direction=None, 
		since=None, number=-1, etag=None)
	for issue in issues:
		issue.close()