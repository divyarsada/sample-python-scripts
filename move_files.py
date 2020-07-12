import os
import shutil
import json
import glob
#create a directory, if directory exists, creating it again  raises an expection so included in try block
try:
    os.mkdir("./processed")
except OSError: #all exceptions under OSError is handeled
    print("'processed' directory already existst")

#glob to get the list of pathnames matching the pattern
receipts=glob.glob('./receipt-[0-9]*.json')
subtotal=0.0

#iterating through the list of pathnames, calculating the values in the files and moving the files to dest
for path in receipts:
    with open(path, 'r') as f:
       content= json.load(f)
       subtotal+= float(content['value'])
    name = path.split('/')[-1]
    destination = f"./processed/{name}"
    shutil.move(path,destination)
    print(f"moved {path} to {destination}")
print("subtotal:{0:.2f}".format(subtotal))
