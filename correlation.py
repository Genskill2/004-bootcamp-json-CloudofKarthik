import json
import math

def load_journal(file_name):
  f = open(file_name)
  data = json.loads(f.read())
        
  return data
  
def compute_phi(file_name, event_name):
  data = load_journal(file_name)
  n11 = 0
  n00 = 0
  n10 = 0
  n01 = 0
  n12 = 0
  n02 = 0
  n21 = 0
  n20 = 0
  for i in data:
    p = 0
    q = 0
    for j in i["events"]:
      if j == event_name:
        p += 1
    if i["squirrel"] is True:
      q += 1
    if p == 1 and q == 1:
      n11 += 1
    elif p == 0 and q == 0:
      n00 += 1
    elif p == 1 and q == 0:
      n10 += 1
    elif p == 0 and q == 1:
      n01 += 1
    if p == 1:
      n12 += 1
    else:
      n02 += 1
    if q == 1:
      n21 += 1
    else:
      n20 += 1
  return (n11*n00 - n10*n01)/(math.sqrt(n12*n02*n21*n20))


def compute_correlations(file_name):
  data = load_journal(file_name)
  list1 = []
  for i in data:
    for j in i["events"]:
      if j not in list1:
        list1.append(j)
  
  dictionary = {} 
  for i in list1:
    dictionary[i] = compute_phi(file_name, i)
    
        
  return dictionary

def diagnose(file_name):
  dictionary = compute_correlations(file_name)
  minim = 1
  maxim = -1
  
  for x,y in dictionary.items():
    if y > maxim:
      max_item = x
      maxim = y
    if y < minim:
      min_item = x
      minim = y
  return max_item, min_item# Add the functions in this file
