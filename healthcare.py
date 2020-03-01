import pandas as pd
import numpy as np
import os
import shutil

f = open('HAM10000_metadata.csv', 'r')

skincancer_df = pd.read_csv('HAM10000_metadata.csv')

id_n_type = skincancer_df[['image_id','dx']]
nv = id_n_type.query('dx == "nv"')
mel = id_n_type.query('dx == "mel"')
bkl = id_n_type.query('dx == "bkl"')
bcc = id_n_type.query('dx == "bcc"')
akiec = id_n_type.query('dx == "akiec"')
vasc = id_n_type.query('dx == "vasc"')
df = id_n_type.query('dx == "df"')

nv_images = []
for index, row in nv.iterrows():
  nv_images.append(row['image_id']+'.jpg')

mel_images = []
for index, row in mel.iterrows():
  mel_images.append(row['image_id']+'.jpg')

bkl_images = []
for index, row in bkl.iterrows():
  bkl_images.append(row['image_id']+'.jpg')

bcc_images = []
for index, row in bcc.iterrows():
  bcc_images.append(row['image_id']+'.jpg')

akiec_images = []
for index, row in akiec.iterrows():
  akiec_images.append(row['image_id']+'.jpg')

vasc_images = []
for index, row in vasc.iterrows():
  vasc_images.append(row['image_id']+'.jpg')

df_images = []
for index, row in df.iterrows():
  df_images.append(row['image_id']+'.jpg')

directory = os.fsencode('HAM10000_images_part_1')
for file in os.listdir(directory):
      filename = os.fsdecode(file)
      if filename in df_images:
            source = ('/Users/vanessalandayan/Downloads/skin-cancer-mnist-ham10000/HAM10000_images_part_1/'+filename)
            dest = ('/Users/vanessalandayan/Downloads/skin-cancer-mnist-ham10000/df_path')
            shutil.move(source, dest)
