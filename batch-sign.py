#!/usr/bin/env python3
#
# Copyright 2020 rowit Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################
# This is an example python script that takes 3 parameters:
# 1. The URL of the domain that is signing the files.
# 2. The path to the private key that coresponds to the URL in (1).
# 3. A path to a directory containing all the files to sign
#
# Once the files are signed it will upload the hash and signature of all of
# them to the umpint.com servers to allow users to authenticate at a later 
# date.
#
# It will finally print out the result detailing status of the files it
# signed.

from base64 import (
    b64encode,
    b64decode,
)

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

import sys
from os import path
import os
import urllib.request
import json

print('Args passed:'+str(sys.argv))

if not path.exists(sys.argv[2]):
        print('Could not find file: '+sys.argv[2])
        quit()

if not path.exists(sys.argv[3]):
        print('Could not find file: '+sys.argv[3])
        quit()

if not path.isdir(sys.argv[3]):
        print('3rd parm needs to be directory: '+sys.argv[3])
        quit()
# Read shared key from file
private_key = False
with open (sys.argv[2], "r") as myfile:
    private_key = RSA.importKey(myfile.read())

# Load private key and sign message
signer = PKCS1_v1_5.new(private_key)
results=[]
for filename in os.listdir(sys.argv[3]):
    print('processing file : '+filename)
    with open(sys.argv[3]+'/'+filename, 'r') as datafile:
        data = datafile.read()

    digest = SHA256.new()
    digest.update(data.encode('utf-8'))
    digestStr=str(digest.hexdigest())
    #print("hash String:"+digestStr)

    dig2=SHA256.new()
    dig2.update(digestStr.encode('utf-8'))

    sig = signer.sign(dig2)
    sigString=b64encode(sig).decode('utf-8')
    #print("Signature:"+sigString)
    sigParam=sigString.replace('\n','').replace('+','-').replace('=','_').replace('/','~').replace(' ','')
    result=[digestStr,sigParam]
    results.append(result)

resultsJSON=json.dumps(results)
print(resultsJSON)
req = urllib.request.Request("https://upint.com/api/v1/sign/"+sys.argv[1], resultsJSON.encode('utf-8'), {'Content-Type':'application/json'})
contents = urllib.request.urlopen(req).read()

print(contents)
