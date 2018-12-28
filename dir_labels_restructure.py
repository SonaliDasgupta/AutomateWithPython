import os
import shutil
def create_dir_structure(dir = 'cifar/train'):
  fnames = [f for f in os.listdir(dir)]
  for fname in fnames:
    if not os.path.isdir(dir):
      if not os.path.exists(f'{dir}/{fname.split("_")[1].split(".")[0]}'):
        os.mkdir(f'{dir}/{fname.split("_")[1].split(".")[0]}')
      shutil.move(f'{dir}/{fname}', f'{dir}/{fname.split("_")[1].split(".")[0]}/{fname}')