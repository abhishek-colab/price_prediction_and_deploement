#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 03:08:00 2020

@author: abhisheksingh
"""
import json
import pickle
import copy
import numpy as np

__unique = None
__defaults = None
__req_indexing = None
__original_col = None
__model = None


def get_requirements():
    
    global __unique
    global __defaults
    global __req_indexing
    global __original_col
    global __model
    
    with open('/Users/abhisheksingh/project_MPP/requirments/metadata-2.json','r') as f:
        data = json.load(f)
        __unique=data['data']["unique"]
        __defaults = data['data']['defaults']
        __req_indexing = data['data']['req_indexing']
        __original_col = data['data']['columns']
        
    with open('/Users/abhisheksingh/project_MPP/requirments/mobile_price_stacked.pickle','rb') as f:
        __model = pickle.load(f)
    
    print('requirements loaded')
    
def predict_mobile_price(**kwargs):
  get_requirements()
  features= copy.deepcopy(__defaults)
  features.update(kwargs)
  for k,v in __unique.items():
    if features[k] not in v:
      features[k]=__defaults[k]
  delete=[]
  for k,v in features.items():
    if k not in __defaults.keys():
      delete.append(k)
  for k in delete:
    del features[k]
  #print(features)
  
  x=np.zeros(len(__original_col))
  for k,v in features.items():
    if k in __req_indexing:
      try:
        #ind = np.where(original_col==(k+'_'+v))[0][0]
        ind = __original_col.index(k+'_'+v)
        if ind>=0:
          x[ind]=1
      except:
        continue
    else:
      #ind = np.where(original_col==k)[0][0]
      ind = __original_col.index(k)
      x[ind]=v
  #assert len(x)==len(original_col)
  return __model.predict([x])[0]

if __name__ == '__main__':
    get_requirements()
    price1 = predict_mobile_price(brand='Appl',bands_4G=True,GPRS=False,statuses='val',weight_g=60,internal_memory=64,have_fingerprint=True,RAM=6)
    price2 = predict_mobile_price(brand='Acer',bands_4G=False,GPRS=False,status='Available',weight_g=180,internal_memory=64,have_fingerprint=True,RAM=6)
    price3 = predict_mobile_price(brand='Apple',bands_4G=False,GPRS=False,statuses='val',weight_g=200,internal_memory=128,have_fingerprint=True,RAM=8)
    print(price1)
    print(price2)
    print(price3)