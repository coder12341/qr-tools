import qrcode
from PIL import Image
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--logo", required=False, help="Add path to logo")
ap.add_argument("-qv", "--qrversion", required=False, default=1, help="QR Version")
ap.add_argument("-bs", "--boxsize", required=False, type=int, default=10, help="Box size")
ap.add_argument("-b", "--border", required=False, default=4, help="Border")
ap.add_argument("-t", "--text", required=True, type=str, help="Text input in quotes\nFor SMS: SMSTO:phone_number:message\nFor email: MATMSG:TO:to_email;SUB:subject;BODY:body;;")
ap.add_argument("-bg", "--background", required=False, default='white', help="Background color")
ap.add_argument("-fg", "--foreground", required=False, default='black', help="Foreground color")
ap.add_argument("-o", "--output", required=False, default='generated_qr.png', help="Output name")
args = vars(ap.parse_args())

if args['qrversion'] and args['boxsize'] and args['border'] and args['background'] and args['foreground']:
    qr = qrcode.QRCode(
        version=args['qrversion'],
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=args['boxsize'],
        border=args['border'])
else:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4)

qr.add_data(args['text'])
qr.make(fit=True)

if args['background'] and args['foreground']:
    img = qr.make_image(fill_color=args['foreground'], back_color=args['background']).convert('RGB')
else:
    img = qr.make_image(fill_color='black', back_color='white').convert('RGB')


if args['logo']:
    logo_display = Image.open(args['logo'])
    logo_display.thumbnail((60, 60))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)

if args['output']:
    img.save(args['output'])
else:
    img.save("generated_qr.png")