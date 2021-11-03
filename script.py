import json
from collections import namedtuple
import pprint
import paramiko
# Opening JSON file
a_json = open('worm.json',)
def json_to_obj(data): return json.load(data, object_hook=lambda converted_dict: namedtuple('configuration', converted_dict.keys())(*converted_dict.values()))
Config=json_to_obj(a_json) #Makes Our JSON an object, and loads it to Config
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(Config.server.ip, username=Config.server.user)
stdin, stdout, stderr = client.exec_command(f"rsync -abviuzP  {Config.client.user}@{Config.client.ip}:{Config.client.path}* {Config.server.path} && chmod -R 777 {Config.server.path}")
for line in stdout:
    print (line.strip('\n'))
print(f"rsync -abviuzP {Config.server.path} {Config.client.user}@{Config.client.ip}:{Config.client.path}")
stdin, stdout, stderr = client.exec_command(f"rsync -abviuzP {Config.server.path}* {Config.client.user}@{Config.client.ip}:{Config.client.path}")
for line in stdout:
    print (line.strip('\n'))