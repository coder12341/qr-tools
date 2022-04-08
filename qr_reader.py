from pyzbar import pyzbar
import webbrowser
import cv2


def main(image):
	# load the input image
	image = cv2.imread(image)
	# find the barcodes in the image and decode each of the barcodes
	barcodes = pyzbar.decode(image)

	# loop over the detected barcodes
	for barcode in barcodes:
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
		return barcodeType, barcodeData
