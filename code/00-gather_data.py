## ---
# title: "RMS Letter Comparison"
# author: "Wm Salt Hale"
# date: "March 25, 2021"
# license: "GPL-3"
## --


import os
import time
import pandas as pd
import numpy as np
np.random.seed(42)

from github import Github
from github import RateLimitExceededException

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
  file = open(filename + '.log', 'a')
  file.write(str(text) + '\n')
  file.close()

def get_user_info(user, repo):
  utype = user.type
  if(utype == 'Anonymous'):
    if(user.email != ''):
      queried_users = gh.search_users(user.email)
    elif(user.name != ''):
      queried_users = gh.search_users(user.name + ' in:name')
    else:
      queried_users = None
      
    if(queried_users == None):
      utype = 'Anonymous'
    elif(queried_users.totalCount == 0):
      utype = 'Anonymous'
    elif(queried_users.totalCount > 1):
      utype = 'Multiple'
    else:
      user = queried_users.get_page(0)[0]
      utype = 'Queried'
      
    if((utype == 'Anonymous') or (utype == 'Multiple')):
      info = {
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
      }
      return(info)
      
  info = {
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
  }
  return(info)


i = 0
d = []
first_write = True
#import pdb; pdb.set_trace()
for u in rr_users:
  rate_limiter = True
  while rate_limiter:
    try:
      d.append(get_user_info(u, 'rr'))
      rate_limiter = False
    except RateLimitExceededException as e:
      # Q: Why is a rate limit exception being thrown despite being well within the 5,000 requests per hour limit?
      ## https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting
      ## A: It appears that the Search API is what is causing the problem, it is capped at 30 requests per minute. Luckily this does seem to be handling it.
      ## https://docs.github.com/en/rest/reference/search#rate-limit
      log_writer('[' + time.asctime() + '] Rate limit at time of error:', 'rate')
      log_writer(gh.get_rate_limit().core, 'rate')
      log_writer('---', 'rate')
      time.sleep(10)
      continue
    except Exception as e:
      print('[' + time.asctime() + '] An unhandled error occurred:')
      print(e)
      print('---')
      log_writer('An unhandled error occurred:', 'error')
      log_writer(e, 'error')
      log_writer('---', 'error')
      continue

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
  d.append(get_user_info(u, 'sr'))
  i = i + 1
  if(i > 100):
    log_writer('[' + time.asctime() + '] Wrote to CSV', 'write')
    pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False, header=None, mode='a')
    d = []
    i = 0

log_writer('[' + time.asctime() + '] Final write to CSV', 'write')
pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False, header=None, mode='a')

print('Contributor list complete!')

