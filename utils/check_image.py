#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
import numpy as np
from bs4 import BeautifulSoup
from clint.textui import progress, puts, colored
from PIL import Image

IMG_ROOT = '../images/'

def savePhotoByUrl(url, imageID):
	fname = IMG_ROOT + str(imageID) + '.jpg'
	print "Downloading " + url + '...'
	
	try:
		handle = urllib2.urlopen(url, timeout=5)
		with open(fname, "wb") as f:
			while True:
				chunk = handle.read(1024)
				if not chunk: break
				f.write(chunk)
		puts(colored.green("Finished downloading " + fname))
	except Exception as e:
		print('ERROR: {}'.format(e))

def getPhotoByID(imageID):
	BASE_URL = 'http://www.dpchallenge.com/image.php?IMAGE_ID='

	data = None
	imgURL = None
	try:
		data = urllib2.urlopen(BASE_URL + str(imageID), timeout=5).read()
	except Exception as e:
		print('ERROR: {}'.format(e))
	else:
		soup = BeautifulSoup(data, 'html.parser')
		title = soup.title.string.split('by')[0][:-1]
		
		results = soup.find(id='img_container').findAll('img')
		for result in results:
			#if (result.has_attr('alt') and result['alt'] == title):
			if (result.has_attr('alt')):
				imgURL = result['src']
				savePhotoByUrl(imgURL, imageID)

def getPhotoIDs():
	ava = np.loadtxt('../AVA.txt', dtype=int)
	return ava[:,1]

def verifyImage(imageID):
	try:
		im = Image.open(IMG_ROOT + str(imageID) + '.jpg')
		#im.verify()
		im.load()
	except Exception as e:
		puts(colored.red('ERROR: {}'.format(e)))
		puts(colored.yellow("Redownloading image ..."))
		getPhotoByID(imageID)
	#else:
	#	puts(colored.green("Image virification ... passed!"))


def main():
	
	# load image IDs
	#puts(colored.yellow("Loading image IDs..."))
	#IDs = getPhotoIDs()
	#puts("Done")

	IDs = [954130, 423283, 682625, 353511, 721605, 729377, 401281, 316751]
	
	for ID in IDs:
		if os.path.isfile(IMG_ROOT + str(ID) + '.jpg'):
			verifyImage(ID)


if __name__ == "__main__":
	main()