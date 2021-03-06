[![](https://img.shields.io/badge/version-2.0-green)](https://github.com/coder12341/qr-tools/releases/tag/2.0)
![](https://img.shields.io/badge/license-GPLv3-blue)
![](https://img.shields.io/badge/language-Python3-red)
![](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
[![qr-tools](https://snapcraft.io/qr-tools/badge.svg)](https://snapcraft.io/qr-tools)
[![qr-tools](https://snapcraft.io/qr-tools/trending.svg?name=0)](https://snapcraft.io/qr-tools)

# ![QR-Tools](icon.png) QR-Tools
A collection of tools to read and generate QR-Codes

<br>

## Scan and generate qr-codes easily
### Install Required libraries
```
pip3 install pyzbar imutils opencv-python Pillow qrcode wireless PyQt5 segno
```

### Generate qr
```
python3 qr_generator.py -t 'Some Text' [-l logo.png] [-logo_width 60] [-logo_height 60] [--micro] [--scale 10] [--qrversion 1] [--boxsize 10] [--border 4] [--background white] [--foreground black] [--help]
```
**If the dimensions of the logo you put are too large, your QR-Code might not be readable by scanners!**



### Read qr from file
```
python3 qr_reader.py -i qr-code.png
```



### Read qr (live)

```
python3 qr_reader_live.py
```
<br>

### For Developers

To make your own build, just paste the following commands into a terminal.

``` bash
#Before pasting the commands make sure that you have python3 and pip3 installed!
git clone https://github.com/coder12341/qr-tools.git #Download the source code
cd qr-tools
pip3 install -r requirements.txt #Install the required libraries
pip3 install pyinstaller
pyinstaller -F --icon icon.ico [the_name_of_the_program.py]
```

<br>

### [Download Binaries](https://github.com/coder12341/qr-tools/releases)

**Windows amd64**

[QR Generator cli (for Windows_amd64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_win_amd64.exe)

[QR Generator Graphical (for Windows_amd64_portable)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator_portable_win_x64.zip)

[QR Generator Graphical (for Windows_amd64_installer)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator_setup_win_amd64.exe)


**Linux amd64**

[QR Generator cli (for Linux_amd64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_linux_amd64)

[QR Generator Graphical (for Linux_amd64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator_linux_amd64.tar.xz)

[QR Generator Graphical (installer for Debian based distros amd64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator_setup_linux_amd64.deb)


**Raspberry Pi**

[QR Generator cli (for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_rpi)

[QR Generator Graphical (for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator_rpi.tar.gz)

[QR Generator Graphical (installer for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator_setup_rpi.deb)

Notes: 

- **Binaries are only available the QR-Code Generator app.**

- **You should also have installed 'libnotify-bin' in order for the application to work properly on Linux. You can install it via your package manager.**



<br>

### Terminal installation(Linux only)

To install the CLI versiob of QR-Code Generator open a terminal and paste the following commands.

**Raspberry Pi**

```bash
wget https://raw.githubusercontent.com/coder12341/qr-tools/website/downloads/install_rpi.sh && chmod +x install_rpi.sh && sudo ./install_rpi.sh && rm install_rpi.sh && qr-generator -h
```

**Linux (x64)**

```bash
wget https://raw.githubusercontent.com/coder12341/qr-tools/website/downloads/install_linux.sh && chmod +x install_linux.sh && sudo ./install_linux.sh && rm install_linux.sh && qr-generator -h
```
<br>

### Extra
[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/qr-tools)

<br>

### File hashes (SHA256)
You can find the file hashes in the [releases section](https://github.com/coder12341/qr-tools/releases/tag/2.0)

