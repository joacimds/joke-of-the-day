import requests
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password',
        'username': 'deCastillon', 'password': 'TCF6GAfzs58c'}
auth = requests.auth.HTTPBasicAuth(
    'tRLX1U8HSRXogA', 'v-7bizF5h9_sWCtRe6X8rhkB2A4')
# A token created using username, password, app-id and app-secret.
r = requests.post(base_url + 'api/v1/access_token', data=data,
                  headers={'user-agent': 'joke-of-the-day by deCastillon'}, auth=auth)
d = r.json()

# API requests should be done to https://oauth.reddit.com
token = 'bearer' + d['access_token']
base_url = 'https://oauth.reddit.com'

# Authentication token
headers = {'Authorization': token,
           'User-Agent': 'joke-of-the-day by deCastillon'}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])

print(r.status_code)
