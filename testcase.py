from astropy.io import fits
#import pyfits as fits
import numpy as np
import time

for i in range(100):
    with fits.open('test.fits') as hdulist:
        print i, np.sum(hdulist[1].data)

time.sleep(60)
