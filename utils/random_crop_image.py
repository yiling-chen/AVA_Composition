#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
import numpy as np
from bs4 import BeautifulSoup
from clint.textui import progress, puts, colored
from PIL import Image
import random

IMG_ROOT = '../images/'
CROP_IMG_ROOT = '../crop_images/'

def getPhotoIDs():
	ava = np.loadtxt('../AVA.txt', dtype=int)
	return ava[:,1]

def randomCropImage(imageID):
	try:
		im = Image.open(IMG_ROOT + str(imageID) + '.jpg')
		width = im.size[0]
		height = im.size[1]
		print width, height

		assert width > 500 and height > 500
		dh = random.randint(0, (width - 256))
		dw = random.randint(0, (height - 256))
		ds = random.randint(128, 256)
		print dh, dw, ds

		new_im = im.crop((dh, dw, dh+ds, dw+ds))
		new_im.save(CROP_IMG_ROOT + str(imageID) + '.jpg')
	except Exception as e:
		puts(colored.red('ERROR: {}'.format(e)))
	#else:
	#	puts(colored.green("Image random crop ... passed!"))

def main():
	# load image IDs
	puts(colored.yellow("Loading image IDs..."))
	IDs = getPhotoIDs()
	puts("Done")
	
	for ID in IDs[:150000]:
		if os.path.isfile(IMG_ROOT + str(ID) + '.jpg'):
			randomCropImage(ID)


if __name__ == "__main__":
	main()