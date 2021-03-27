## ---
# title: "RMS Letter Comparison"
# author: "Wm Salt Hale"
# date: "March 26, 2021"
# license: "GPL-3"
## --


import os
import time
import pandas as pd
import numpy as np
np.random.seed(42)

from github import Github
from github import RateLimitExceededException
from github import GithubException

token = os.getenv('GITHUB_TOKEN')
gh = Github(token)

reject_rms_repo = gh.get_repo('rms-open-letter/rms-open-letter.github.io')
support_rms_repo = gh.get_repo('rms-support-letter/rms-support-letter.github.io')
rr = reject_rms_repo
sr = support_rms_repo

# Q: Why am I only getting ~500 users back per list?
## A: It seems as though the documentation is poor and all of the additional ones return as anonymous
## https://stackoverflow.com/questions/36410357/github-v3-api-list-contributors
rr_users = rr.get_contributors(anon=1)
sr_users = sr.get_contributors(anon=1)

def log_writer(text, filename):
  print(' >< in log_writer')
  file = open(filename + '.log', 'a')
  file.write(str(text) + '\n')
  file.close()

def rate_limiter(call, location):
  print(' <> in rate_limiter')
  successful_call = False
  while(not successful_call):
    try:
      print(' <> trying to call')
      print(str(successful_call))
#      print(str(call))
      response = call
#      print(str(response))
      successful_call = True
      if(successful_call):
        print('successful_call')
    except RateLimitExceededException as e:
      print(' <> trying to write 1.1')
      print(' <> ' + str(location))
      log_writer(location, 'rate')
      print(' <> trying to write 1.2')
      print(' <> ' + '[' + time.asctime() + '] Rate limit at time of error:')
      log_writer('[' + time.asctime() + '] Rate limit at time of error:', 'rate')
      print(' <> trying to write 1.3')
      print(' <> ' + str(gh.get_rate_limit().core))
      log_writer(gh.get_rate_limit().core, 'rate')
      print(' <> trying to write 1.4')
      log_writer('---', 'rate')
      time.sleep(10)
      continue
    except GithubException as e:
      print(' <> trying to write 2.1')
      print('[' + time.asctime() + '] An unhandled GH error occurred:')
      print(' <> trying to write 2.2')
      print(e)
      print(' <> trying to write 2.3')
      print('---')
      log_writer(location, 'error')
      log_writer('An unhandled error occurred:', 'error')
      log_writer(e, 'error')
      log_writer('---', 'error')
      time.sleep(10)
      continue
    except Exception as e:
      print(' <> trying to write 3.1')
      print('[' + time.asctime() + '] An unhandled error occurred:')
      print(' <> trying to write 3.2')
      print(e)
      print(' <> trying to write 3.3')
      print('---')
      log_writer(location, 'error')
      log_writer('An unhandled error occurred:', 'error')
      log_writer(e, 'error')
      log_writer('---', 'error')
      time.sleep(10)
      continue
  print('out of try block')
  print(str(response))
  return(response)

def get_user_info(user, repo):
  print(' . in get_user_info')
  uname = rate_limiter(user.name, '(get user name)')
  uemail = rate_limiter(user.email, '(get user email)')
  utype = rate_limiter(user.type, '(get user type)')
  print(utype)
  if(utype == 'Anonymous'):
    print(' > is anonymous')
    print(uname)
    print(uemail)
    print(utype)
    queried_users = None
    if(uemail != ''):
      print(' > email check')
      queried_users = rate_limiter(gh.search_users(uemail), '(email check)')
      print(queried_users)
      print(' > count check 1')
      qucount = rate_limiter(queried_users.totalCount, '(user count)')
      print(qucount)
      if((qucount == 0) and (uname != '')):
        print(' >> name check in email')
        queried_users = rate_limiter(gh.search_users(uname + ' in:name'), '(name check)')
        print(queried_users)
        print(' > count check 2')
        qucount = rate_limiter(queried_users.totalCount, '(user count)')
        print(qucount)
      print(' > in email passed zero and name')
    elif(uname != ''):
      print(' > name check')
      queried_users = rate_limiter(gh.search_users(uname + ' in:name'), '(name check)')
      print(queried_users)
      print(' > count check 3')
      qucount = rate_limiter(queried_users.totalCount, '(user count)')
      print(qucount)
    if(queried_users == None):
      utype = 'Anonymous'
    else:
      print(' > count check 4')
      qucount = rate_limiter(queried_users.totalCount, '(user count)')
      print(qucount)
      if(qucount == 0):
        utype = 'Anonymous'
      elif(qucount > 1):
        utype = 'Multiple'
      else:
        print(' > user id check')
        user = rate_limiter(queried_users.get_page(0)[0], '(get individual user)')
        print(user)
        utype = 'Queried'
  print(' > passed anonymous')
  print(uname)
  print(uemail)
  print(utype)
  if((utype == 'Anonymous') or (utype == 'Multiple')):
    print(' >> store unidentified')
    info = rate_limiter({
      'ID': None,
      'NodeID': None,
      'Username': None,
      'Name': user.name,
      'Avatar': None,
      'Bio': None,
      'Email': user.email,
      'Location': None,
      'Blog': None,
      'Company': None,
      'Hireable': None,
      'Twitter': None,
      'Collaborators': None,
      'Contributions': user.contributions,
      'Followers': None,
      'Following': None,
      'Gravatar': None,
      'Hireable': None,
      'Created': None,
      'Updated': None,
      'Suspended': None,
      'Inviter': None,
      'PrivateGists': None,
      'PublicGists': None,
      'PublicRepos': None,
      'PrivateRepos': None,
      'OwnedPrivateRepos': None,
      'Plan': None,
      'Role': None,
      'TeamCount': None,
      'Type': utype,
      'SiteAdmin': None,
      'DiskUsage': None,
      'URL': None,
      'FollowersURL': None,
      'FollowingURL': None,
      'ReposURL': None,
      'StarredURL': None,
      'GistsURL': None,
      'htmlURL': None,
      'EventsURL': None,
      'OrganizationsURL': None,
      'InvitationTeamsURL': None,
      'ReceivedEventsURL': None,
      'SubscriptionsURL': None,
      'Repo': repo
    }, '(store anonymous user)')
  else:
    print(' >> store identified')
    info = rate_limiter({
      'ID': user.id,
      'NodeID': user.node_id,
      'Username': user.login,
      'Name': user.name,
      'Avatar': user.avatar_url,
      'Bio': user.bio,
      'Email': user.email,
      'Location': user.location,
      'Blog': user.blog,
      'Company': user.company,
      'Hireable': user.hireable,
      'Twitter': user.twitter_username,
      'Collaborators': user.collaborators,
      'Contributions': user.contributions,
      'Followers': user.followers,
      'Following': user.following,
      'Gravatar': user.gravatar_id,
      'Hireable': user.hireable,
      'Created': user.created_at,
      'Updated': user.updated_at,
      'Suspended': user.suspended_at,
      'Inviter': user.inviter,
      'PrivateGists': user.private_gists,
      'PublicGists': user.public_gists,
      'PublicRepos': user.public_repos,
      'PrivateRepos': user.total_private_repos,
      'OwnedPrivateRepos': user.owned_private_repos,
      'Plan': user.plan,
      'Role': user.role,
      'TeamCount': user.team_count,
      'Type': utype,
      'SiteAdmin': user.site_admin,
      'DiskUsage': user.disk_usage,
      'URL': user.url,
      'FollowersURL': user.followers_url,
      'FollowingURL': user.following_url,
      'ReposURL': user.repos_url,
      'StarredURL': user.starred_url,
      'GistsURL': user.gists_url,
      'htmlURL': user.html_url,
      'EventsURL': user.events_url,
      'OrganizationsURL': user.organizations_url,
      'InvitationTeamsURL': user.invitation_teams_url,
      'ReceivedEventsURL': user.received_events_url,
      'SubscriptionsURL': user.subscriptions_url,
      'Repo': repo
    }, '(store identified user)')
  return(info)


i = 0
d = []
first_write = True
#import pdb; pdb.set_trace()
for u in rr_users:
  d.append(rate_limiter(get_user_info(u, 'rr'), '(rr loop)'))
  i = i + 1
  if(i > 100):
    log_writer('[' + time.asctime() + '] Wrote to CSV', 'write')
    if first_write:
      pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False)
      first_write = False
    else:
      pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False, header=None, mode='a')
    d = []
    i = 0

for u in sr_users:
  d.append(rate_limiter(get_user_info(u, 'sr'), '(sr loop)'))
  i = i + 1
  if(i > 100):
    log_writer('[' + time.asctime() + '] Wrote to CSV', 'write')
    pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False, header=None, mode='a')
    d = []
    i = 0

log_writer('[' + time.asctime() + '] Final write to CSV', 'write')
pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False, header=None, mode='a')

print('Contributor list complete!')

