# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:30:03 2023

@author: bhasi
"""

!pip install PyDictionary
from PyDictionary import PyDictionary
import hashlib

y = ""
dictionary = PyDictionary()
m = hashlib.sha256()

def f1(x):
  if bool(dictionary.meaning(x, disable_errors=True)):
    return len(x)<=5
  else:
    print('Not a word in the PyDictionary. Try again!')

def f2(x):
  if bool(dictionary.meaning(x, disable_errors=True)):
    return any([x[0].lower() == c for c in ['a','e','i','o','u']])
  else:
    print('Not a word in the PyDictionary. Try again!')

def f3(x):
  entry = dictionary.meaning(x, disable_errors=True)
  if bool(entry):
    return 'Verb' in entry.keys()
  else:
    print('Not a word in the PyDictionary. Try again!')

def f4(x):
  if bool(dictionary.meaning(x, disable_errors=True)):
    return len(''.join(set(x))) == len(x)
  else:
    print('Not a word in the PyDictionary. Try again!')

def f5(x):
  if bool(dictionary.meaning(x, disable_errors=True)):
    return bool(dictionary.meaning(x[::-1], disable_errors=True));
  else:
    print('Not a word in the PyDictionary. Try again!')

def f6(x):
  global y
  temp = y
  if bool(dictionary.meaning(x, disable_errors=True)):
    y = x
    return (temp != "" and temp[0] == x[0].lower())
  else:
    print('Not a word in the PyDictionary. Try again!')

def f7(x):
  if bool(dictionary.meaning(x, disable_errors=True)):
    m = hashlib.sha256(x.lower().encode())
    return bool(int(bin(int(m.hexdigest(), 16))[-1]))
  else:
    print('Not a word in the PyDictionary. Try again!')