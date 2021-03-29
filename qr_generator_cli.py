import qrcode
from PIL import Image
import argparse
import segno
import getpass

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--logo", required=False, help="Add path to logo")
ap.add_argument("-lw", "--logo_width", required=False, default=60, help="Logo width")
ap.add_argument("-lh", "--logo_height", required=False, default=60, help="Logo height")

ap.add_argument("-qv", "--qrversion", required=False, nargs="?", default=1, help="QR Version")
ap.add_argument("-bs", "--boxsize", required=False, nargs="?", default=10, help="Box size")
ap.add_argument("-b", "--border", required=False, nargs="?", default=4, help="Border")
ap.add_argument("-t", "--text", required=True, help="Text input")

ap.add_argument("--micro", required=False, nargs="?", const=True, help="Micro qr-code output. Limited character handling!")
ap.add_argument("--scale", required=False, nargs="?", default=10, help="Micro qr-code scale")

ap.add_argument("-bg", "--background", required=False, nargs="?", default='white', help="Background color")
ap.add_argument("-fg", "--foreground", required=False, nargs="?", default='black', help="Foreground color")

ap.add_argument("-o", "--output", required=False, nargs="?", default='generated_qr.png', help="Output name")
args = vars(ap.parse_args())


print('''   ___  ____        ____          _         ____                           _             
  / _ \|  _ \      / ___|___   __| | ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | | | |_) |____| |   / _ \ / _` |/ _ \ | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_| |  _ <_____| |__| (_) | (_| |  __/ | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
  \__\_\_| \_\     \____\___/ \__,_|\___|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   ''')

print('\n'+'*'*40)
print('Copyright of coder12341')
print('https://coder12341.github.io/qr-tools')
print('*'*40+'\n')

qr = qrcode.QRCode(version=args['qrversion'], 
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=args['boxsize'], 
    border=args['border'])

if args['text']=='/EMAIL':
    if args['micro']:
        print('[!]Error!\n[+]Micro qr-codes cannot handle many characters.\n[+]For more information visit https://coder12341.github.io/qr-tools/micro-qr\n')
        exit()
    to=input("To: ")
    sub=input("Subject: ")
    body=input("Body:\n")
    qr.add_data('MATMSG:TO:%s;SUB:%s;BODY:%s;;'%(to, sub, body))
    
elif args['text']=='/SMS':
    if args['micro']:
        print('[!]Error!\n[+]Micro qr-codes cannot handle many characters.\n[+]For more information visit https://coder12341.github.io/qr-tools/micro-qr\n')
        exit()
    to=input('To: ')
    message=input('Message: ')
    qr.add_data('SMSTO:%s:%s'%(to, message))

elif args['text']=='/WIFI':
    if args['micro']:
        print('[!]Error!\n[+]Micro qr-codes cannot handle many characters.\n[+]For more information visit https://coder12341.github.io/qr-tools/micro-qr\n')
        exit()
    ssid=input('SSID: ')
    passwd=getpass.getpass('Password(no echo):')
    hidden=input('Hidden?(true/false)[false]: ')
    encryption=input('Encryption:\n(0)WPA\n(1)WEP\n(2)None\n:')
    encryption_list=['WPA', 'WEP', 'nopass']
    is_int=False
    while is_int!=True:
        try:
            int(encryption)
            is_int=True
        except:
            print('[!]ERROR\n[+]Type only the number!\n')
            encryption=input('Encryption:\n[0]WPA\n[1]WEP\n[2]nopass\n[number]: ')

    if hidden=='false':
        hidden=''

    qr.add_data("WIFI:T:%s;S:%s;P:%s;H:%s;"%(encryption_list[int(encryption)], ssid, passwd, hidden.lower()))

elif args['text']=='/CONTACT':
    if args['micro']:
        print('[!]Error!\n[+]Micro qr-codes cannot handle many characters.\n[+]For more information visit https://coder12341.github.io/qr-tools/micro-qr\n')
        exit()
    name=input('Name: ')
    org=input('Organization: ')
    url=input('Website: ')
    email=input('Email: ')
    tel=input('Telephone: ')
    cell=input('Cell Phone: ')
    fax=input('Fax: ')
    country=input("Country: ")
    city=input('City: ')
    region=input('Region/State: ')
    postcode=input('Postcode: ')
    street=input('Street: ')
    qr.add_data('BEGIN:VCARD\nN:%s\nORG:%s\nEMAIL;TYPE=INTERNET:%s\nURL:%s\nTEL;TYPE=CELL:%s\nTEL:%s\nTEL;TYPE=FAX:%s\nADR:;;%s;%s;%s;%s;%s\nEND:VCARD'%(name, org, email, url, cell, tel, fax, street, city, region, postcode, country))

elif args['text']=='/EVENT':
    if args['micro']:
        print('[!]Error!\n[+]Micro qr-codes cannot handle many characters.\n[+]For more information visit https://coder12341.github.io/qr-tools/micro-qr\n')
        exit()
    title=input('Event title: ')
    location=input('Event location: ')
    start_datetime=input('Start Date and Time(YYYY/MM/DD hh:mm:ss): ').split(' ')
    end_datetime=input('End Date and Time(YYYY/MM/DD hh:mm:ss): ').split(' ')

    end_date=end_datetime[0].split('/')
    end_time_=end_datetime[1].split(':')
    end_time=end_date[0]+end_date[1]+end_date[2]+'T'+end_time_[0]+end_time_[1]+end_time_[2]

    start_date=start_datetime[0].split('/')
    start_time_=start_datetime[1].split(':')
    start_time=start_date[0]+start_date[1]+start_date[2]+'T'+start_time_[0]+start_time_[1]+start_time_[2]
    
    qr.add_data('BEGIN:VEVENT\nSUMMARY:%s\nLOCATION:%s\nDTSTART:%s\nDTEND:%s\nEND:VEVENT\n'%(title, location, start_time, end_time))

else:
    if args['micro']:
        try:
            qr_micro = segno.make(args['text'], micro=True)
        except:
            print('[!]Error!\n[+]Micro qr-codes cannot handle many characters.\n[+]For more information visit https://coder12341.github.io/qr-tools/micro-qr\n')
            exit()
    else:
        qr.add_data(args['text'])



qr.make(fit=True)
img = qr.make_image(fill_color=args['foreground'], back_color=args['background']).convert('RGB')

if args['logo']:
    logo_display = Image.open(args['logo'])
    logo_display.thumbnail((int(args['logo_width']), int(args['logo_height'])))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)

if args['micro']:
    qr_micro.save(args['output'], border=args['border'], scale=args['scale'])
else:
    img.save(args['output'])
