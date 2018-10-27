#!/usr/bin/python

import glob
import os
import shutil
import commands

user = commands.getoutput('whoami')
home = '/Users/' + user + '/'
src_path = '/Users/' + user + '/Desktop/'

file_types_and_destinations = [
    {'type': 'scripts', 'extensions': ['py','sh','yml'], 'path': home + 'scripts/'},
    {'type': 'documents', 'extensions': ['pdf','docx','zip'], 'path': home + 'Documents/'},
    {'type': 'pictures', 'extensions': ['png','jpg'], 'path': home + 'Pictures/'}
]

def move_files(file_type,dst_path):
  beforefiles = [f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path, f))]
  # print(beforefiles)
  for t in file_type:
    t = '.' + str(t)
    files = filter(lambda x:x.endswith(t), beforefiles)
    for f in files:
      src = src_path+f
      dst = dst_path+f
      print(dst)
      shutil.move(src,dst)

def check_dir_move_files(file_type,dst_path):
  if  os.path.isdir(dst_path):
      move_files(file_type,dst_path)
  else:
      os.mkdir(dst_path)
      move_files(file_type,dst_path)

for each in file_types_and_destinations:
    check_dir_move_files(each['extensions'],each['path'])

