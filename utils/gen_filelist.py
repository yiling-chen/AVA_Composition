#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import PIL
from PIL import Image

def centerCrop(im, id):
	left = (im.size[0] - 256) / 2
	top = (im.size[1] - 256) / 2
	im.crop((left, top, left+256, top+256)).save('/home/robin/Libraries/caffe/data/ava/images/'+str(id)+'.jpg')

def resize(im, id, path):
	baseLength = 500
	scale = 1
	if im.size[0] > im.size[1]:
		scale = float(baseLength) / im.size[0]
	else:
		scale = float(baseLength) / im.size[1]
	new_size = (int(im.size[0] * scale), int(im.size[1] * scale))
	im.resize(new_size, PIL.Image.ANTIALIAS).save(path+str(id)+'.jpg')



ava = np.loadtxt('AVA.txt', dtype=int)

ranking = ava[:,2:12]
weight = np.array(range(1,11), dtype=float)
ID = ava[:,1]

total_score = np.dot(ranking, weight)
total_votes = np.sum(ranking, axis=1)
avg_rank = np.divide(total_score, total_votes)

high_rank_id = ID[avg_rank > 6]
np.random.shuffle(high_rank_id)
low_rank_id = ID[avg_rank < 4]
np.random.shuffle(low_rank_id)

split = 2500
with open("test.txt", "w") as test_img_list:
	path = '/tmp2/yiling/AVA/images/'
	for id in high_rank_id[:split]:
		if os.path.isfile('images/' + str(id) + '.jpg'):
			im = Image.open('images/' + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			#resize(im, id, path)
			#test_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 1))
			test_img_list.write("%s %d\n" % (str(id)+'.jpg', 1))

	for id in low_rank_id[:split]:
		if os.path.isfile('images/' + str(id) + '.jpg'):
			im = Image.open('images/' + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			#resize(im, id, path)
			#test_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 0))
			test_img_list.write("%s %d\n" % (str(id)+'.jpg', 0))

with open("train.txt", "w") as train_img_list:
	path = '/tmp2/yiling/AVA/images/'
	for id in high_rank_id[split:]:
		if os.path.isfile('images/' + str(id) + '.jpg'):
			im = Image.open('images/' + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			#resize(im, id, path)
			#train_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 1))
			train_img_list.write("%s %d\n" % (str(id)+'.jpg', 1))

	for id in low_rank_id[split:]:
		if os.path.isfile('images/' + str(id) + '.jpg'):
			im = Image.open('images/' + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			#resize(im, id, path)
			#train_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 0))
			train_img_list.write("%s %d\n" % (str(id)+'.jpg', 0))

