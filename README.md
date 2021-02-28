# ![icon](icon.png) QR-Tools
QR-Code Scanner and Generator

## Scan and generate qr-codes easily
### Install Required libraries
```
pip3 install pyzbar imutils opencv-python Pillow qrcode wireless PyQt5
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

[QR Generator(for Windows_x64)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_win_x64.exe)

[QR Generator Graphical(for Windows_x64_portable)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_win_x64_portable.graphical.zip)

[QR Generator Graphical(for Windows_x64_installer)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_win_x64_installer.graphical.exe)

[QR Generator Graphical(for Linux_x64)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_deb_x64)

[QR Generator Graphical(for Linux_x64)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_linux_x64.graphical.zip)

[QR Generator(for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_linux_armhf)

[QR Generator Graphical(for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/1.0/qr_generator_linux_armhf.graphical.zip)
