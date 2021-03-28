# ![icon](icon.png) QR-Tools
QR-Code Scanner and Generator

## Scan and generate qr-codes easily
### Install Required libraries
```
pip3 install pyzbar imutils opencv-python Pillow qrcode wireless PyQt5 segno
```
### Generate qr
```
python3 qr_generator.py -t 'Some Text' [-l logo.png] [-logo_width 60] [-logo_height 60] [--micro] [--scale 10] [--qrversion 1] [--boxsize 10] [--border 4] [--background white] [--foreground black] [--help]
```

### Read qr from file
```
python3 qr_reader.py -i qr-code.png
```

### Read qr (live)
```
python3 qr_reader_live.py
```

### [Download Binaries](https://github.com/coder12341/qr-tools/releases)

>QR Generator(for Windows_x64) Coming soon!
>

[QR Generator Graphical(for Windows_x64_portable)](https://github.com/coder12341/qr-tools/releases/download/v2.0/QR.Generator_portable_win_x64.zip)

[QR Generator Graphical(for Windows_x64_installer)](https://github.com/coder12341/qr-tools/releases/download/v2.0/QR.Generator.setup_win_x64.exe)

[QR Generator cli(for Linux_x64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_linux_x64)

[QR Generator Graphical(for Linux_x64)](https://github.com/coder12341/qr-tools/releases/download/2.0/QR.Generator_linux_x64.tar.xz)

>QR Generator(for Raspberry_pi_armhf) Coming soon!
>

>QR Generator Graphical(for Raspberry_pi_armhf) Coming soon!
>
