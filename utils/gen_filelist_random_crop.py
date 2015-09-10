#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import PIL
from PIL import Image
from os import listdir
from os.path import isfile, join


ava = np.loadtxt('../AVA.txt', dtype=int)

ranking = ava[:,2:12]
weight = np.array(range(1,11), dtype=float)
ID = ava[:,1]

total_score = np.dot(ranking, weight)
total_votes = np.sum(ranking, axis=1)
avg_rank = np.divide(total_score, total_votes)

high_rank_id = ID[avg_rank > 6]
np.random.shuffle(high_rank_id)
#low_rank_id = ID[avg_rank < 4]
#np.random.shuffle(low_rank_id)

crop_images_path = '../crop_images/'
crop_image_files = [ f for f in listdir(crop_images_path) if isfile(join(crop_images_path,f)) ]

split = 5000
with open("test.txt", "w") as test_img_list:
	path = 'crop_images/'
	for f in crop_image_files[:split]:
		im = Image.open(join(crop_images_path,f))
		#if (im.size[0] < 256 or im.size[1] < 256):
		#	continue
		test_img_list.write("%s %d\n" % (path+f, 0))

	path = 'images/'
	for id in high_rank_id[:split]:
		if os.path.isfile('../images/' + str(id) + '.jpg'):
			im = Image.open('../images/' + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			test_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 1))

with open("train.txt", "w") as train_img_list:
	path = 'crop_images/'
	for f in crop_image_files[split:]:
		im = Image.open(join(crop_images_path,f))
		#if (im.size[0] < 256 or im.size[1] < 256):
		#	continue
		train_img_list.write("%s %d\n" % (path+f, 0))

	path = 'images/'
	for id in high_rank_id[split:]:
		if os.path.isfile('../images/' + str(id) + '.jpg'):
			im = Image.open('../images/' + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			train_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 1))

