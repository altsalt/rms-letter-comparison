## ---
# title: "RMS Letter Comparison"
# author: "Wm Salt Hale"
# date: "March 25, 2021"
# license: "GPL-3"
## --


import pandas as pd
import numpy as np
np.random.seed(42)

from github import Github
import os
import time
from pprint import pprint

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

reject_rms_repo = g.get_repo("rms-open-letter/rms-open-letter.github.io")
support_rms_repo = g.get_repo("rms-support-letter/rms-support-letter.github.io")
rr = reject_rms_repo
sr = support_rms_repo

rr_users = rr.get_contributors()
sr_users = sr.get_contributors()

d = []

def get_user_info(user, repo):
  time.sleep(1)
  if(g.rate_limiting[0] < 10):
    time.sleep(10)
  info = {
    'ID': u.id,
    'NodeID': u.node_id,
    'Username': u.login,
    'Name': u.name,
    'Avatar': u.avatar_url,
    'Bio': u.bio,
    'Email': u.email,
    'Location': u.location,
    'Blog': u.blog,
    'Company': u.company,
    'Hireable': u.hireable,
    'Twitter': u.twitter_username,
    'Collaborators': u.collaborators,
    'Contributions': u.contributions,
    'Followers': u.followers,
    'Following': u.following,
    'Gravatar': u.gravatar_id,
    'Hireable': u.hireable,
    'Created': u.created_at,
    'Updated': u.updated_at,
    'Suspended': u.suspended_at,
    'Inviter': u.inviter,
    'PrivateGists': u.private_gists,
    'PublicGists': u.public_gists,
    'PublicRepos': u.public_repos,
    'PrivateRepos': u.total_private_repos,
    'OwnedPrivateRepos': u.owned_private_repos,
    'Plan': u.plan,
    'Role': u.role,
    'TeamCount': u.team_count,
    'Type': u.type,
    'SiteAdmin': u.site_admin,
    'DiskUsage': u.disk_usage,
    'URL': u.url,
    'FollowersURL': u.followers_url,
    'FollowingURL': u.following_url,
    'ReposURL': u.repos_url,
    'StarredURL': u.starred_url,
    'GistsURL': u.gists_url,
    'htmlURL': u.html_url,
    'EventsURL': u.events_url,
    'OrganizationsURL': u.organizations_url,
    'InvitationTeamsURL': u.invitation_teams_url,
    'ReceivedEventsURL': u.received_events_url,
    'SubscriptionsURL': u.subscriptions_url,
    'Repo': repo
  }
  return(info)

#import pdb; pdb.set_trace()
for u in rr_users:
  d.append(get_user_info(u, 'rr'))

for u in sr_users:
  d.append(get_user_info(u, 'sr'))

pd.DataFrame(d).to_csv('data/rms-letter-signers.csv', index=False)

