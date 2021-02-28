import qrcode
from PIL import Image
import argparse


class generator():
    def generate_text(text, version, boxsize, border, fg, bg, logo, output):
        qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxsize,
        border=border)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg, back_color=bg).convert('RGB')
        if logo != 'False':
            logo_display = Image.open(logo)
            logo_display.thumbnail((60, 60))
            logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
            img.paste(logo_display, logo_pos)
        if output != 'False':
            img.save(output)
        else:
            img.save('generated_qr.png')

    def generate_email(to, sub, body, version, boxsize, border, fg, bg, logo, output):
        qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxsize,
        border=border)
        qr.add_data('MATMSG:TO:%s;SUB:%s;BODY:%s;;'%(to, sub, body))
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg, back_color=bg).convert('RGB')
        if logo != 'False':
            logo_display = Image.open(logo)
            logo_display.thumbnail((60, 60))
            logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
            img.paste(logo_display, logo_pos)
        if output != 'False':
            img.save(output)
        else:
            img.save('generated_qr.png')
    
    def generate_sms(to, message, version, boxsize, border, fg, bg, logo, output):
        qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxsize,
        border=border)
        qr.add_data('SMSTO:%s:%s'%(to, message))
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg, back_color=bg).convert('RGB')
        if logo != 'False':
            logo_display = Image.open(logo)
            logo_display.thumbnail((60, 60))
            logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
            img.paste(logo_display, logo_pos)
        if output !='False':
            img.save(output)
        else:
            img.save('generated_qr.png')

    def generate_wifi(ssid, passwd, encryption, hidden, version, boxsize, border, fg, bg, logo, output):
        qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxsize,
        border=border)
        qr.add_data("WIFI:T:%s;S:%s;P:%s;H:%s;"%(encryption, ssid, passwd, hidden))
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg, back_color=bg).convert('RGB')
        if logo != 'False':
            logo_display = Image.open(logo)
            logo_display.thumbnail((60, 60))
            logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
            img.paste(logo_display, logo_pos)
        if output != 'False':
            img.save(output)
        else:
            img.save('generated_qr.png')
    
    def generate_contact_details(name, org, tel, email, cell, fax, street, city, region, postcode, country, url, version, boxsize, border, fg, bg, logo, output):
        qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxsize,
        border=border)
        qr.add_data('BEGIN:VCARD\nN:%s\nORG:%s\nEMAIL;TYPE=INTERNET:%s\nURL:%s\nTEL;TYPE=CELL:%s\nTEL:%s\nTEL;TYPE=FAX:%s\nADR:;;%s;%s;%s;%s;%s\nEND:VCARD'%(name, org, email, url, cell, tel, fax, street, city, region, postcode, country))
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg, back_color=bg).convert('RGB')
        if logo != 'False':
            logo_display = Image.open(logo)
            logo_display.thumbnail((60, 60))
            logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
            img.paste(logo_display, logo_pos)
        if output != 'False':
            img.save(output)
        else:
            img.save('generated_qr.png')