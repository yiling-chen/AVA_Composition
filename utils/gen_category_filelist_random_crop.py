#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import PIL
from PIL import Image
from os import listdir
from os.path import isfile, join
from clint.textui import progress, puts, colored
import random

IMG_ROOT = '../images/'
CROP_IMG_ROOT = '../crop_images/cityscape/'

def randomCropImage(imageID):
	try:
		im = Image.open(IMG_ROOT + str(imageID) + '.jpg')
		width = im.size[0]
		height = im.size[1]
		#print width, height

		assert width >= 500 and height >= 500
		dh = random.randint(0, (width - 256))
		dw = random.randint(0, (height - 256))
		ds = random.randint(128, 256)
		#print dh, dw, ds

		new_im = im.crop((dh, dw, dh+ds, dw+ds))
		new_im.save(CROP_IMG_ROOT + str(imageID) + '.jpg')
	except Exception as e:
		puts(colored.red('ERROR: {}'.format(e)))
	#else:
	#	puts(colored.green("Image random crop ... passed!"))

category_train = np.loadtxt('../aesthetics_image_lists/cityscape_train.jpgl', dtype=int)
category_test = np.loadtxt('../aesthetics_image_lists/cityscape_test.jpgl', dtype=int)

with open("test.txt", "w") as test_img_list:
	path = 'crop_images/cityscape/'
	for id in category_test:
		if isfile(IMG_ROOT + str(id) + '.jpg'):
			im = Image.open(IMG_ROOT + str(id) + '.jpg')
			if (im.size[0] < 500 or im.size[1] < 500):
				continue
			randomCropImage(id)
			test_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 0))

	path = 'images/'
	for id in category_test:
		if isfile(IMG_ROOT + str(id) + '.jpg'):
			im = Image.open(IMG_ROOT + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			test_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 1))

with open("train.txt", "w") as train_img_list:
	path = 'crop_images/cityscape/'
	for id in category_train:
		if isfile(IMG_ROOT + str(id) + '.jpg'):
			im = Image.open(IMG_ROOT + str(id) + '.jpg')
			if (im.size[0] < 500 or im.size[1] < 500):
				continue
			randomCropImage(id)
			train_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 0))

	path = 'images/'
	for id in category_train:
		if isfile(IMG_ROOT + str(id) + '.jpg'):
			im = Image.open(IMG_ROOT + str(id) + '.jpg')
			if (im.size[0] < 256 or im.size[1] < 256):
				continue
			train_img_list.write("%s %d\n" % (path+str(id)+'.jpg', 1))

