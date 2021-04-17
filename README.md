[![](https://img.shields.io/badge/version-2.0-green)](https://github.com/coder12341/qr-tools/releases/tag/2.0)
![](https://img.shields.io/badge/license-GPLv3-blue)
![](https://img.shields.io/badge/language-Python3-red)
![](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
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
**If the dimensions of the logo you put are too large, your QR-Code might not be readable by scanners!**



### Read qr from file
```
python3 qr_reader.py -i qr-code.png
```



### Read qr (live)

```
python3 qr_reader_live.py
```



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



### [Download Binaries](https://github.com/coder12341/qr-tools/releases)

[QR Generator cli(for Windows_x64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_win_x64.exe)

[QR Generator Graphical(for Windows_x64_portable)](https://github.com/coder12341/qr-tools/releases/download/v2.0/QR.Generator_portable_win_x64.zip)

[QR Generator Graphical(for Windows_x64_installer)](https://github.com/coder12341/qr-tools/releases/download/v2.0/QR.Generator.setup_win_x64.exe)

[QR Generator cli(for Linux_x64)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_linux_x64)

[QR Generator Graphical(for Linux_x64)](https://github.com/coder12341/qr-tools/releases/download/2.0/QR.Generator_linux_x64.tar.xz)

[QR Generator cli(for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/2.0/qr-generator-cli_rpi)

[QR Generator Graphical(for Raspberry_pi_armhf)](https://github.com/coder12341/qr-tools/releases/download/2.0/QR.Generator_rpi.tar.gz)




### Terminal installation(Linux only)

Open a terminal and paste the following commands.

**Raspberry Pi**

```bash
wget https://raw.githubusercontent.com/coder12341/qr-tools/website/downloads/install_rpi.sh && chmod +x install_rpi.sh && sudo ./install_rpi.sh && rm install_rpi.sh && qr-generator -h
```

**Linux (x64)**

```bash
wget https://raw.githubusercontent.com/coder12341/qr-tools/website/downloads/install_linux.sh && chmod +x install_linux.sh && sudo ./install_linux.sh && rm install_linux.sh && qr-generator -h
```

### File hashes (SHA256)
- qr-generator-cli_linux_x64
``` 
597870fd7779f4cf2446bd6bd04eba4cd3acbfdb79032a244b55abccfc143fb4
```

- qr-generator-cli_rpi
```
fe80b0bdfcd7d851b4c318f61b730a3327700b59c869cc5d007479fecf9e8ab2
```

- qr-generator-cli_win_x64.exe
```
23de331dcbcf5e2274c6a5b2b3c33b342dfa0654a3d9e4d672f61731a5f6f205
```

- QR.Generator.setup_win_x64.exe
```
0f19ef6544d75032c514ba5cce741060acb41ac02e89d27ae7e32be476e5a61d
```

- QR.Generator_linux_x64.tar.xz
```
edad67aa894997e36471893a45bc0ae77a28acad13614dc5c90fe146a7d150dc
```

- QR.Generator_portable_win_x64.zip
```
72ed900973174cbc22dfafedf91da7cb3f7db96c72f78b48163fea51fa0e2144
```

- QR.Generator_rpi.tar.gz
```
d56ad7f4ab65c0d3f47d0018679452a6643b036401783c55a80fd56bcd841293
```


