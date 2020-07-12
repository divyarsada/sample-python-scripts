import os
import json
from argparse import ArgumentParser
import random

count=int(os.getenv("linecount") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]
for identifier in range(count):
    amount = random.uniform(1.0,100)
    content= {'topic': random.choice(words), 'value':"%.2f" %amount}
    with open(f'/home/ec2-user/python_scrpits/receipt-{identifier}.json','w') as f:  
        json.dump(content,f)
with open(f'/home/ec2-user/python_scrpits/receipt-0.json') as f:
    val=json.load(f)
    print(val)
