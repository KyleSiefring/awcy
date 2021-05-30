#!/usr/bin/env python3

import requests
import subprocess
import json
from datetime import *

#our timestamping function, accurate to milliseconds
#(remove [:-3] to display microseconds)
def GetTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

key = None
with open('secret_key','r') as keyfile:
    key = keyfile.read().strip()

if key is None:
    print(GetTime(), "Could not open your secret_key file!")
    sys.exit(1)

config = None
with open('config.json','r',encoding='utf-8') as configfile:
    config = json.load(configfile)

if config is None:
    print(GetTime(), "Could not open config.json!")
    sys.exit(1)

if 'base_url' not in config:
    print(GetTime(), "base_url not in config.json!")
    sys.exit(1)

url = config['base_url']+'/submit/job'
codec = 'vp9'
task = 'subset1'
git_url = subprocess.check_output('git -C '+codec+' config --get remote.origin.url',shell=True).strip().decode("utf-8")
commit = subprocess.check_output('git ls-remote '+git_url+' refs/heads/master',shell=True).strip().split()[0]
short = commit[:7]
date = datetime.now(timezone.utc).isoformat()

run_id = codec+'-'+task+'-profile-'+short.decode("utf-8")+'@'+date

r = requests.post(url, {'run_id': run_id, 'commit': commit, 'key': key, 'codec': codec, 'task': task, 'profile_set': True})
