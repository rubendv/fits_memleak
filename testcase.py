from astropy.io import fits
#import pyfits as fits
import numpy as np
import time

for i in range(100):
    with fits.open('test.fits') as hdulist:
        print("{0}: {1}".format(i, np.sum(hdulist[1].data)))

print("Sleeping for 1 minute")
time.sleep(60)
