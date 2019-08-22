import time
from fabric import task

@task
def task1(c):
    c.run('ls -lah')

    
@task
def task2(c):
    c.run('echo $(hostname)')