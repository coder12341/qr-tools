# ![icon](icon.png) QR-Tools
QR-Code Scanner and Generator

## Scan and generate qr-codes easily
### Install Required libraries
```
pip3 install pyzbar imutils opencv-python Pillow qrcode
```
### Generate qr
```
qr_generator.py -t 'Some Text' [-l logo.png] [--qrversion 1] [--boxsize 10] [--border 4] [--background white] [--foreground black] [--help]
```

### Read qr from file
```
qr_reader.py -i qr.png
```

### Read qr (live)
```
qr_reader_live.py
```

### [Download Binaries](https://github.com/coder12341/qr-tools/releases)

[QR Generator(for WIndows_x64)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_win_x64.exe)
