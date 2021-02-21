from pyzbar import pyzbar
import argparse
import cv2
import webbrowser

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])
# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(image)

# loop over the detected barcodes
for barcode in barcodes:
	# extract the bounding box location of the barcode and draw the
	# bounding box surrounding the barcode on the image
	(x, y, w, h) = barcode.rect
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	# the barcode data is a bytes object so if we want to draw it on
	# our output image we need to convert it to a string first
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type
	# draw the barcode data and barcode type on the image
	text = "{} ({})".format(barcodeData, barcodeType)
	cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)

	if 'http' in barcodeData:
		webbrowser.open(barcodeData)
		print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

	elif 'MATMSG' in barcodeData:
		email=barcodeData.split(':')
		to=email[2].split(';')
		sub=email[3].split(';')
		body=email[4].split(';')
		print("Email: to '{}' with subject '{}' \nBody:{}".format(to[0], sub[0], body[0]))
	
	elif 'SMSTO' in barcodeData:
		sms=barcodeData.split(':')
		num=sms[1]
		mes=sms[2]
		print("SMS: to {} with message {}".format(num, mes))

	else:
		print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)