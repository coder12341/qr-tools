#! /usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from threading import Thread
from time import sleep
from os import listdir
from datetime import datetime
from os import path
class Splash(Thread):
    def __init__(self):
        #Create the GUI
        super(Splash, self).__init__()

        # Create a popup window
        self.window = Gtk.Window(Gtk.WindowType.POPUP)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect('destroy', Gtk.main_quit)
        self.window.set_default_size(400, 250)

        # Add box and label
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        bar=Gtk.ProgressBar()
        bar.set_show_text(False)
        spinner=Gtk.Spinner()
        spinner.start()
        logo=Gtk.Image()
        logo.set_from_file("icon.ico")
        err_lbl=Gtk.Label()
        lbl = Gtk.Label()
        lbl.set_markup("<big><big><big><big><b>QR-Tools</b></big></big></big></big>")
        global result
        result=self.splash_check(err_lbl, bar, self.window)
        box.pack_start(Gtk.Label(), False, True, 0)
        box.pack_start(logo, False, True, 0)
        box.pack_start(lbl, False, True, 0)
        box.pack_start(Gtk.Label(), False, True, 0)
        box.pack_start(spinner, False, True, 0)
        box.pack_start(err_lbl, False, True, 0)
        box.pack_start(Gtk.Label(), False, True, 0)
        box.pack_start(bar, False, True, 0)

        
        self.window.add(box)

    def run(self):
        self.window.set_auto_startup_notification(False)
        self.window.show_all()
        self.window.set_auto_startup_notification(True)
        Gtk.main()

    def destroy(self):
        self.window.destroy()



    def splash_check(self, lbl, bar, win):
        try:
            logs_file_size=path.getsize("logs.txt")
            if logs_file_size>3000000:
                logs=open("logs.txt", "w")
                logs.close() 
        except: pass
        logs=open("logs.txt", "a")
        logs.write("\n%s\nBooting...\n"%datetime.now())
        err_count=0
        #Check for required files
        error_msg=""
        errors=["The file \'icon.ico\'  was not found!", "The file \'qr_generator.py\' was not found!", "Although the file \'qr_generator.py\' was found it could not be imported!", 
    "The file \'gui.glade\' was not found!", "The file \'icon.png\' was not found!", "The file \'qr_reader.py\' was not found!", "Although the file \'qr_reader.py\' was found it could not be imported!"]
        dir=listdir()
        new_value=0
        bar.set_fraction(0)
        
        if "icon.ico" in dir:
            new_value=bar.get_fraction() + 0.175
            bar.set_fraction(new_value)
            logs.write("[+] Found file icon.ico\n")
            win.show_all()
        else:
            err_count+=1
            error_msg=error_msg+errors[0]
            logs.write("[!] File icon.ico not found\n")
    
        if "qr_reader.py" in dir:
            try:
                import qr_reader
                new_value=bar.get_fraction() + 0.175
                bar.set_fraction(new_value)
                logs.write("[+] Imported file qr-reader.py successfully\n")
                win.show_all()
            except Exception as e:
                err_count+=1
                error_msg=error_msg+"\n"+errors[6]
                logs.write("[!] Could not import file qr_reader.py : %s \n"%e)

        else:
            err_count+=1
            error_msg=error_msg+errors[5]
            logs.write("[!] File qr_reader.py not found\n")

           
        if "qr_generator.py" in dir:
            try:
                import qr_generator
                logs.write("[+] Imported qr_generator.py successfully\n")
                new_value=bar.get_fraction() + 0.25
                bar.set_fraction(new_value)
                win.show_all()
            except Exception as e:
                err_count+=1
                error_msg=error_msg+"\n"+errors[2]
                logs.write("[!] Could not import file qr_generator.py : %s \n"%e)

        else:
            error_msg=error_msg+"\n"+errors[1]
            err_count+=1
            logs.write("[!] File qr_generator.py not found\n")
        
        if "gui.glade" in dir:
            new_value=bar.get_fraction() + 0.25
            bar.set_fraction(new_value)
            logs.write("[+] Found file gui.glade\n")
            win.show_all()
        else:
            error_msg=error_msg+"\n"+errors[3]
            err_count+=1
            logs.write("[!] File gui.glade not found\n")

        if "icon.png" in dir:
            new_value=bar.get_fraction() + 0.25
            bar.set_fraction(new_value)
            logs.write("[+] Found file icon.png\n")
            win.show_all()
        else:
            err_count+=1
            error_msg=error_msg+"\n"+errors[4]
            logs.write("[!] File icon.png not found.")
        logs.write("Boot Errors:%s \n"%err_count)
        logs.close()
        if err_count>0:
            lbl.set_label(error_msg.strip())
            return False

        return True

def main():
    splash = Splash()
    splash.start()
    if result==True:
        sleep(1)
    elif result==False:
        sleep(7)
        splash.destroy()
        exit()
    splash.destroy()
    return True