
import json
import numpy as np
import os
import sys

cmdargs = sys.argv
def getfile(path):
    file = os.path.abspath(os.path.join(os.path.dirname('__file__'), path))
    return file

file = getfile(cmdargs[1]) or getfile('../log_input/batch_log.json')
streamlog = getfile(cmdargs[2]) or getfile('../log_input/stream_log.json')             
flaggedPurchase = getfile(cmdargs[3]) or getfile('../log_output/flagged_purchases.json')

array = []
D = 1
T = 2
friend = {}
listoffriend = []
purchases = {}
purchaseDetails = []

#Reading from the file
with open(file, "r") as f:
  for line in f:
    if "D" in line and "T" in line:
     d = json.loads(line)
     D = int(d["D"]) 
     T = int(d["T"])
    if "befriend" in line:
        b = json.loads(line)
        id = b["id1"]
        if id in friend:
            friend[id].extend([b["id2"]])
        else:
             friend[id] = [b["id2"]]
        id1 = b["id2"]
        if id1 in friend:
            friend[id1].extend([b["id1"]])
        else:
             friend[id1] = [b["id1"]]
        
    elif "unfriend" in line:
        b= json.loads(line)
        id = b["id1"]
        if id in friend:
            friend[id].remove(b["id2"])
            friend[b["id2"]].remove(id)

            
    elif "purchase" in line:
        b = json.loads(line)
        if b["id"] in purchases.keys():
             purchases[b["id"]].extend([b["amount"],b["timestamp"]])
        else: 
             purchases[b["id"]] = [b["amount"],b["timestamp"]]

#print(friend)
#print(purchases)
#def networkpurchase(user):
    
def anomaly(user):
    y=[]
    aa =0
    mean =0
    sd =0
    network = 1
    networklist= []
    u = user
    while network > 0:
        if u not in networklist:
                networklist.append(u)
        for fri in friend[u]:
            if fri not in networklist:
                networklist.append(fri)
            u=fri   
        network = network -1
    #print(networklist)
    for j in networklist:
        if j in purchases:
            for k in purchases[j][::2]:
                        if len(y) <= T:
                            y.append(float(k))
            
                          
    
    if  len(y) !=0 or len(y) > 2:
        mean = np.mean(y) 
        sd = np.std(y)
        aa = mean + (3 * sd)
        
    return (aa,mean,sd)
open(flaggedPurchase,"w")
with open(streamlog, "r") as f:
    for line in f:
    # d = json.loads(line)
        if "befriend" in line:
            b = json.loads(line)
            id = b["id1"]
            if id in friend:
                friend[id].extend([b["id2"]])
            else:
                 friend[id] = [b["id2"]]
            id1 = b["id2"]
            if id1 in friend:
                friend[id1].extend([b["id1"]])
            else:
                 friend[id1] = [b["id1"]]

        elif "unfriend" in line:
            b= json.loads(line)
            id = b["id1"]
            if id in friend:
                friend[id].remove(b["id2"])
                friend[b["id2"]].remove(id)

        elif "purchase" in line:
            b = json.loads(line)
            t = anomaly(b["id"])
            if b["id"] in purchases.keys():
                 purchases[b["id"]].extend([b["amount"],b["timestamp"]])
            else: 
                 purchases[b["id"]] = [b["amount"],b["timestamp"]] 
           # print(t)
            if t[0] > 0:
                if float(b["amount"]) > t[0]:
                  with open(flaggedPurchase,"a")as w:
                    b["mean"]= '%.2f' % t[1]
                    b["sd"] = '%.2f' % t[2]
                    json.dump(b,w) 
