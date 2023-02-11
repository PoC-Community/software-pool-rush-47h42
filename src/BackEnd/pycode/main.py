import time
from testclass import *

#####################
logf = '.test.log'
#####################

def gval(file):
    file = open(file, 'r')
    value = file.read()
    file.close()
    return value

def filewrite(file, content):
    file = open(file, 'w')
    file.write(content)
    file.close()

def get_loop(file):
    if gval(file) == 'True':
        return True
    else:
        return False

def lunch(config):
    test = Report(config.split())
    test.dir()
    test.pull_repo()
    test.ccreport_gen()
    test.destroy()

def update():
    lines = gval(logf).split('\n')
    state = int(gval('pycode/.line'))
    new = len(lines) - state
    if new:
        for i in range(new):
            lunch(lines[state + (i - 1)])
    filewrite('pycode/.line', str(len(lines)))

def mainloop(file):
    while True:
        if get_loop('pycode/.loop'):
            update()
        time.sleep(1)

mainloop('.line')