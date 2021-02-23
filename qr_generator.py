import qrcode
from PIL import Image
import argparse
from getpass import getpass

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--logo", required=False, help="Add path to logo")
ap.add_argument("-qv", "--qrversion", required=False, default=1, type=int, const=1, nargs='?', help="QR Version")
ap.add_argument("-bs", "--boxsize", required=False, type=int, default=10, const=10, nargs='?', help="Box size")
ap.add_argument("-b", "--border", required=False, default=4, type=int, const=4, nargs='?', help="Border")
ap.add_argument("-t", "--text", required=True, type=str, help="Text input in quotes.\nFor Email type /EMAIL\n For SMS type /SMS\nFor Contact details type /CONTACT\nFor wifi type /WIFI")
ap.add_argument("-bg", "--background", required=False, default='white', nargs='?', const='white', help="Background color")
ap.add_argument("-fg", "--foreground", required=False, default='black', nargs='?', const='black', help="Foreground color")
ap.add_argument("-o", "--output", required=False, default='generated_qr.png', nargs='?', const='generated_qr.png', help="Output name")
args = vars(ap.parse_args())

qr = qrcode.QRCode(
    version=args['qrversion'],
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=args['boxsize'],
    border=args['border'])

if args['text']=='/EMAIL':
    to=input("TO: ")
    sub=input("SUBJECT: ")
    body=input("BODY:\n")
    qr.add_data('MATMSG:TO:%s;SUB:%s;BODY:%s;;'%(to, sub, body))

elif args['text']=='/SMS':
    to=input("TO: ")
    message=input("MESSAGE: ")
    qr.add_data('SMSTO:%s:%s'%(to, message))
elif args['text']=='/WIFI':
    ssid=input("WIFI SSID: ")
    passwd=getpass("WIFI PASSWORD(no echo):")
    encryption=input("WIFI Encryption(nopass, WPA, WEP): ")
    hidden=input("Hidden(true, false): ")
    qr.add_data("WIFI:T:%s;S:%s;P:%s;H:%s;"%(encryption, ssid, passwd, hidden))
elif args['text']=='/CONTACT':
    name=input("Name: ")
    org=input('Organization: ')
    tel=input('Telephone: ')
    email=input('Email: ')
    cell=input("Cell Phone: ")
    fax=input("Fax: ")
    street=input("Street: ")
    city=input("City: ")
    region=input('Region/State: ')
    postcode=input('Postcode: ')
    country=input("Country: ")
    url=input("Website: ")
    qr.add_data('BEGIN:VCARD\nN:%s\nORG:%s\nEMAIL;TYPE=INTERNET:%s\nURL:%s\nTEL;TYPE=CELL:%s\nTEL:%s\nTEL;TYPE=FAX:%s\nADR:;;%s;%s;%s;%s;%s\nEND:VCARD'%(name, org, email, url, cell, tel, fax, street, city, region, postcode, country))
else:
    qr.add_data(args['text'])

qr.make(fit=True)

img = qr.make_image(fill_color=args['foreground'], back_color=args['background']).convert('RGB')


if args['logo']:
    logo_display = Image.open(args['logo'])
    logo_display.thumbnail((60, 60))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)

img.save(args['output'])