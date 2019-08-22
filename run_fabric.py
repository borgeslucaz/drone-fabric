#!/usr/bin/env python
# _ docker run --rm -e TASKS=task1,task2 -e HOSTS=root@nightwing.cloudezapp.io:22000 -e KEY=$(cat ~/.ssh/id_rsa | awk '{printf "%s\\n", $0}') -v $(pwd):$(pwd) -w $(pwd) borgeslucaz/drone-fabric

import os
from envparse import Env
from subprocess import Popen, PIPE

#A=$(cat ~/.ssh/id_rsa | awk '{printf "%s\\n", $0}') _ docker run --rm -e KEY=$A -e TASKS=task1,task2 -e HOSTS=root@nightwing.cloudezapp.io:22000 -v $(pwd):$(pwd) -w $(pwd) borgeslucaz/drone-fabric
#A= _ docker run --rm -e KEY="$(cat ~/.ssh/id_rsa | awk '{printf "%s\\n", $0}')" -e TASKS=task1,task2 -e HOSTS=root@nightwing.cloudezapp.io:22000 -v $(pwd):$(pwd) -w $(pwd) borgeslucaz/drone-fabric


def main():
    env = Env(HOSTS=dict(cast=list, subcast=str),
              TASKS=dict(cast=list, subcast=str),
              KEY=str)

    host_list = ','.join([str(x) for x in env('HOSTS')])
    task_list = env('TASKS')
    private_key = env('KEY')

    with open('/key.pem', 'w') as f: 
        f.write(private_key)
        f.close()

    command = ['fab', '--identity', '/key.pem', '--hosts', host_list] + task_list

    p = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    
    if stdout:
        print('-------STARTING FABFILE-------')
        print(stdout)
        print('-------- END FABFILE  --------')

    if stderr:
        raise Exception(stderr)

if __name__ == "__main__":
    main()



