import sys
import os
from pathlib import Path
from PIL import Image 
 
main_path = os.getcwd()
 
image_path = f"{main_path}/Pokedex/"
new_path = f"{main_path}/New/"
 
Path(new_path).mkdir(parents=True, exist_ok=True)
 
 
for filename in os.listdir(image_path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{image_path}{filename}')
  img.save(f'{new_path}/{clean_name}.png', 'png')
  print('all done!')