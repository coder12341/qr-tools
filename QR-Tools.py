import gi
import splash
import json
from getpass import getuser
from platform import system
from datetime import datetime, date
import re

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject

global username
username=getuser()
global os
os=system()
#Splash screen
splash.main()

from qr_generator import generator
import qr_reader

class AboutDialog(Gtk.AboutDialog):
    def __init__(self, parent):
        builder=Gtk.Builder()
        builder.add_from_file("gui.glade")
        dialog=builder.get_object("about_window")
        dialog.show_all()

class CalDialog(Gtk.Dialog):
    """
    Calendar Dialog
    """
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Select Date", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))
 
        self.set_default_size(300, 200)
 
        self.value = None
 
        box = self.get_content_area()
 
        calendar = Gtk.Calendar()
        #calendar.set_detail_height_rows(1)
        calendar.set_property("show-details",True)
        calendar.set_detail_func(self.get_cal_date)
        #print(calendar.get_date())
 
        box.add(calendar)
 
        self.show_all()
 
    def get_cal_date(self, calendar, year, month, date):
        self.value = calendar.get_date()
        global date_qr_data
        date_qr_data=self.value


class main_win(Gtk.Window):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui.glade")
        
        #Define the main window
        self.window = self.builder.get_object("main_window")
        self.window.connect("destroy", Gtk.main_quit)

        #Variables
        self.logo_file_data="False"
        self.save_as_path=None
        #Define generate buttons
        self.generate_text_btn=self.builder.get_object("generate1")
        self.generate_text_btn.connect("clicked", self.generate_text_uri)
        uri_radio_btn=self.builder.get_object("url_radio_btn")
        uri_radio_btn.connect("toggled", self.on_text_button_toggled, "uri")
        self.uri_entry=self.builder.get_object("url_data")
        text_radio_btn=self.builder.get_object("text_radio_btn")
        text_radio_btn.connect("toggled", self.on_text_button_toggled, "text")
        self.text_data=self.builder.get_object("text_data")

        self.generate_wifi_btn=self.builder.get_object("generate2")
        self.generate_wifi_btn.connect("clicked", self.generate_wifi)
        self.essid_data=self.builder.get_object("essid_data")
        self.wifi_password_data=self.builder.get_object("wifi_password_data")
        self.wifi_encryption_data=self.builder.get_object("wifi_encryption_data")
        self.hidden_network_data=self.builder.get_object("hidden_network_data")

        self.generate_sms_btn=self.builder.get_object("generate3")
        self.generate_sms_btn.connect("clicked", self.generate_sms)
        self.phone_number_data=self.builder.get_object("phone_number_data")
        self.sms_data=self.builder.get_object("sms_data")
        self.country_code_data=self.builder.get_object("country_code_data")
        self.country_code_data.connect("changed", self.country_code_entry)
        self.sms_radio_btn=self.builder.get_object("encode_sms_rdio_btn")
        self.phone_radio_btn=self.builder.get_object("encode_phone_rdio_btn")
        self.sms_radio_btn.connect("toggled", self.enable_sms)
        self.phone_radio_btn.connect("toggled", self.enable_sms)

        self.generate_email_btn=self.builder.get_object("generate4")
        self.generate_email_btn.connect("clicked", self.generate_email)
        self.email_receiver_data=self.builder.get_object("email_receiver_data")
        self.email_subject=self.builder.get_object("email_subject_data")
        self.email_data=self.builder.get_object("email_body_data")

        self.generate_contact_btn=self.builder.get_object("generate5")
        self.generate_contact_btn.connect("clicked", self.generate_contact_details)
        self.name_data=self.builder.get_object("contact_name_data")
        self.organization=self.builder.get_object("contact_org_data")
        self.phone_num=self.builder.get_object("contact_landline_data")
        self.cell_phone_num=self.builder.get_object("contact_cell_data")
        self.fax=self.builder.get_object("contact_fax_data")
        self.email=self.builder.get_object("contact_email_data")
        self.country=self.builder.get_object("contact_country_data")
        self.state=self.builder.get_object("contact_state_data")
        self.city=self.builder.get_object("contact_city_data")
        self.street=self.builder.get_object("contact_street_data")
        self.postcode=self.builder.get_object("contact_postcode_data")
        self.website=self.builder.get_object("contact_website_data")

        self.generate_event_btn=self.builder.get_object("generate6")
        self.generate_event_btn.connect("clicked", self.generate_event)
        self.event_title=self.builder.get_object("event_title_data")
        self.location=self.builder.get_object("event_location_data")
        self.start_date_btn=self.builder.get_object("start_date_btn")
        self.start_date_btn.connect("clicked", self.calendar_dialog_start_date)
        self.start_hour=self.builder.get_object("event_start_hour_data")
        self.start_minute=self.builder.get_object("event_start_minute_data")
        self.end_date_btn=self.builder.get_object("end_date_btn")
        self.end_date_btn.connect("clicked", self.calendar_dialog_end_date)
        self.end_hour=self.builder.get_object("event_end_hour_data")
        self.end_minute=self.builder.get_object("event_end_minute_data")
        self.start_day="";self.start_month="";self.start_year=""
        self.end_day="";self.end_month="";self.end_year=""
        time=datetime.now().strftime("%H:%M")
        hour=time.split(":")[0]
        minute=time.split(":")[1]
        cur_date=date.today().strftime("%m/%d/%Y")
        self.start_date_btn.set_label(cur_date)
        self.start_hour.set_value(float(hour))
        self.start_minute.set_value(float(minute))
        self.start_day=str(cur_date.split("/")[1]);self.start_month=str(cur_date.split("/")[0]);self.start_year=str(cur_date.split("/")[2])

        self.generate_social_btn=self.builder.get_object("generate7")
        self.chat_type=self.builder.get_object("mode")
        self.skype_username=self.builder.get_object("skype_username")
        self.skype_data_box=self.builder.get_object("skype_data_box")
        self.zoom_data_box=self.builder.get_object("zoom_data_box")
        self.social_type_skype_radio_btn=self.builder.get_object("social_type_skype")      
        self.social_type_zoom_radio_btn=self.builder.get_object("social_type_zoom")
        self.zoom_id=self.builder.get_object("zoom_id")
        self.zoom_passwd=self.builder.get_object("zoom_passwd")
        self.social_type_skype_radio_btn.set_active(True)
        self.social_type_skype_radio_btn.connect("toggled", self.on_social_btn_toggled, "skype")
        self.social_type_zoom_radio_btn.connect("toggled", self.on_social_btn_toggled, "zoom")
        self.generate_social_btn.connect("clicked", self.generate_social)

        #Window menu Buttons
        self.quit_menu_btn=self.builder.get_object("quit_menu_btn")
        self.quit_menu_btn.connect("clicked", Gtk.main_quit)
        self.about_menu_btn=self.builder.get_object("about_menu_btn")
        self.about_menu_btn.connect("clicked", self.about_action)

        #Define settings" widgets
        self.fg_color=self.builder.get_object("fg_color_data")
        self.bg_color=self.builder.get_object("bg_color_data")
        self.border=self.builder.get_object("border_data")
        self.boxsize=self.builder.get_object("boxsize_data")
        self.qr_version=self.builder.get_object("qr_version_data")
        self.logo_chooser_btn=self.builder.get_object("logo_file_chooser")
        self.logo_chooser_btn.connect("clicked", self.choose_logo_file)
        self.clear_button=self.builder.get_object("clear_logo_button")
        self.clear_button.connect("clicked", self.clear_logo)
        if self.logo_chooser_btn.get_label()=="(None)":
            self.clear_button.set_sensitive(False)
        self.logo_chooser_filter=self.builder.get_object("Pictures")
        self.logo_width=self.builder.get_object("logo_width_data")
        self.logo_height=self.builder.get_object("logo_height_data")
        self.output_file_data=self.builder.get_object("output_file_data")
        self.output_file_data.set_text("/home/"+username+"/generated_qr.png")
        self.micro_qr=self.builder.get_object("micro_qr")
        self.micro_qr.connect("notify::active", self.on_micro_qr_switch_activated)
        self.micro_qr_scale=self.builder.get_object("micro_scale_data")
        self.save_qr_as=self.builder.get_object("ask_qr_save_location")
        self.save_qr_as.connect("notify::active", self.on_save_as_switch_activated)

        #Define boxes
        self.output_file_box=self.builder.get_object("output_file_box")
        self.dim_box=self.builder.get_object("dim_box")
        self.logo_box=self.builder.get_object("logo_box")
        self.qr_version_box=self.builder.get_object("qr_version_box")
        self.boxsize_box=self.builder.get_object("boxsize_box")
        self.border_box=self.builder.get_object("border_box")
        self.bg_color_box=self.builder.get_object("bg_color_box")
        self.fg_color_box=self.builder.get_object("fg_color_box")
        self.micro_qr_box=self.builder.get_object("micro_qr_box")

        #Warning bar
        self.warning_bar=self.builder.get_object("error_bar")
        self.warning_bar.connect("response", self.on_qr_error_response)
        self.warning_bar.set_revealed(False)
        self.more_info_btn=self.builder.get_object("more_info_link_btn")
        self.more_info_btn.set_label("More information")
        self.warning_label=self.builder.get_object("warning_label")

        #Custom country code bar
        self.custom_country_code_bar=self.builder.get_object("custom_country_code_bar")
        self.custom_country_code_bar.set_revealed(False)
        self.custom_code_data=self.builder.get_object("custom_country_code_data")
        self.custom_country_code_lbl=self.builder.get_object("custom_country_code_status_label")
        self.custom_country_code_ok_btn=self.builder.get_object("custom_country_code_ok_btn")
        self.custom_country_code_ok_btn.connect("clicked", self.custom_country_code)

        #Read QR-Code from file
        self.path_to_qr_code_to_read=""
        self.select_qr_code_btn=self.builder.get_object("select_qr_to_read_button")
        self.select_qr_code_btn.connect("clicked", self.choose_qr_code_file)
        self.formatted_data_out=self.builder.get_object("formatted_data_out")
        self.raw_data_out=self.builder.get_object("raw_data_out")

        self.window.show_all()

    def enable_sms(self, widget):
        if self.sms_radio_btn.get_active():
            self.sms_data.set_sensitive(True)
            self.custom_country_code_lbl.set_visible(True)
        else:
            self.custom_country_code_lbl.set_visible(False)
            self.sms_data.set_sensitive(False)
    def about_action(self, widget):
        dialog=AboutDialog(self.window)
        dialog.run()
        dialog.destroy()
    def on_qr_error_response(self, bar, respose_id):
        bar.set_revealed(False)
        self.more_info_btn.set_visible(False)
    
    def get_buffer_text(self, textview):
        buffer = textview.get_buffer()
        startIter, endIter = buffer.get_bounds()    
        text = buffer.get_text(startIter, endIter, False) 
        return text
    def custom_country_code(self, widget):
        global code
        code="+"+str(self.custom_code_data.get_value_as_int())
        self.custom_country_code_lbl.set_text("Saved!")
        GObject.timeout_add(1500, self.change_status_label_text_country_code)

    def change_status_label_text_country_code(self):
        self.custom_country_code_lbl.set_text("")
    def on_text_button_toggled(self, button, name):
        if name=="uri":
            if button.get_active():
                self.uri_entry.set_sensitive(True)
            else:
                self.uri_entry.set_sensitive(False)
        elif name=="text":
            if button.get_active():
                self.text_data.set_sensitive(True)
            else:
                self.text_data.set_sensitive(False)
    
    def country_code_entry(self, widget):
        if widget.get_active_id()=="custom":
            self.custom_country_code_bar.set_revealed(True)
        else:
            self.custom_country_code_bar.set_revealed(False)
    
    def on_social_btn_toggled(self, button, name):
        if name=="skype":
            self.zoom_data_box.set_sensitive(False)
            self.skype_data_box.set_sensitive(True)
        else:
            self.zoom_data_box.set_sensitive(True)
            self.skype_data_box.set_sensitive(False)

    def clear_logo(self, widget):
        self.logo_chooser_btn.set_label("(None)")
        self.clear_button.set_sensitive(False)

    def calendar_dialog_start_date(self, widget):
        calendar=CalDialog(self.window)
        response=calendar.run()
        if response==Gtk.ResponseType.OK:
            self.start_day=date_qr_data[2]
            self.start_month=date_qr_data[1]+1
            self.start_year=date_qr_data[0]
            self.start_date_btn.set_label("%d/%d/%d"%(self.start_month, self.start_day, self.start_year))
        calendar.destroy()
    
    def calendar_dialog_end_date(self, widget):
        calendar=CalDialog(self.window)
        response=calendar.run()
        if response==Gtk.ResponseType.OK:
            self.end_day=date_qr_data[2]
            self.end_month=date_qr_data[1]+1
            self.end_year=date_qr_data[0]
            self.end_date_btn.set_label("%d/%d/%d"%(self.end_month, self.end_day, self.end_year))
        calendar.destroy()

    def choose_logo_file(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Choose logo", parent=self.window, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        dialog.add_filter(self.logo_chooser_filter)
        dialog.set_current_folder("/home/%s"%username)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.logo_file_data=dialog.get_filename()
            self.logo_chooser_btn.set_label(self.logo_file_data)
            self.clear_button.set_sensitive(True)
        elif response == Gtk.ResponseType.CANCEL:
            self.logo_file_data="False"

        dialog.destroy()
    
    def check_for_data_overflow_err(self, excep, button):
        if "Data too large" and "Micro QR Code" in str(excep):
            button.set_visible(True)
        else:
            button.set_visible(False)

    def null_data_error(self, button, label, bar):
        button.set_visible(False)
        label.set_label("No data provided for encoding! Try filling any empty fields.")
        bar.set_revealed(True)

    def get_bg_fg_qr_color_data(self, fg_color_btn, bg_color_btn):
        self.fg_color_data=fg_color_btn.get_rgba().to_string().split("(");self.fg_color_data=self.fg_color_data[1].split(")")
        self.bg_color_data=bg_color_btn.get_rgba().to_string().split("(");self.bg_color_data=self.bg_color_data[1].split(")")

    def generate_text_uri(self, button):
        if self.uri_entry.get_sensitive()==True and self.text_data.get_sensitive()==False:
            data=self.uri_entry.get_text()

        elif self.text_data.get_sensitive()==True and self.uri_entry.get_sensitive()==False:
            data=self.get_buffer_text(self.text_data)

        else:
            return False
        if data:
            self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
            try:
                if self.save_qr_as.get_active():
                    self.save_qr_dialog()
                    if self.save_as_path:
                        save_qr=self.save_as_path
                    else:
                        return False
                else:
                    save_qr=self.output_file_data.get_text()

                generator.generate_text(data, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]), 
                eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
            except Exception as ex:
                if ex:
                    self.check_for_data_overflow_err(ex, self.more_info_btn)
                    self.warning_label.set_label(str(ex))
                else:
                    self.more_info_btn.set_visible(False)
                    self.warning_label.set_label("Unable to generate QR-Code!")

                self.warning_bar.set_revealed(True)
        else:
            self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)
            
        
    def generate_wifi(self, button):
        essid_data=self.essid_data.get_text()
        passwd_data=self.wifi_password_data.get_text()
        encryption_data=self.wifi_encryption_data.get_active_text()
        hidden=self.hidden_network_data.get_active()
        if essid_data:
            self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
            try:
                if self.save_qr_as.get_active():
                    self.save_qr_dialog()
                    if self.save_as_path:
                        save_qr=self.save_as_path
                    else:
                        return False
                else:
                    save_qr=self.output_file_data.get_text()

                generator.generate_wifi(essid_data, passwd_data, encryption_data, hidden, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
            except Exception as ex:
                if ex:
                    self.check_for_data_overflow_err(ex, self.more_info_btn)
                    self.warning_label.set_label(str(ex))
                else:
                    self.more_info_btn.set_visible(False)
                    self.warning_label.set_label("Unable to generate QR-Code!")
                self.warning_bar.set_revealed(True)
        else:
            self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)
    
    def generate_sms(self, button):
        phone_number=str(int(self.phone_number_data.get_value()))  
        sms_text=self.get_buffer_text(self.sms_data)
        ctr_code=str(self.country_code_data.get_active_id())
        print(ctr_code)
        if ctr_code=="null":
            ctr_code=""
        elif ctr_code=="custom":
            ctr_code=code
        else:
            ctr_code="+"+ctr_code
        if len(phone_number)>2:
            self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
            try:
                if self.save_qr_as.get_active():
                    self.save_qr_dialog()
                    if self.save_as_path:
                        save_qr=self.save_as_path
                    else:
                        return False
                else:
                    save_qr=self.output_file_data.get_text()
                if self.sms_radio_btn.get_active():
                    generator.generate_sms("%s%s"%(ctr_code, phone_number), sms_text, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                    eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
                else:
                    generator.generate_phone("%s%s"%(ctr_code, phone_number), self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
            except Exception as ex:
                if ex:
                    self.check_for_data_overflow_err(ex, self.more_info_btn)
                    self.warning_label.set_label(str(ex))
                else:
                    self.more_info_btn.set_visible(False)
                    self.warning_label.set_label("Unable to generate QR-Code!")
                self.warning_bar.set_revealed(True)
        else:
            self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)
    
    def generate_email(self, widget):
        receiver=self.email_receiver_data.get_text()
        subject=self.email_subject.get_text()
        body=self.get_buffer_text(self.email_data)
        if receiver:
            self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
            try:
                if self.save_qr_as.get_active():
                    self.save_qr_dialog()
                    if self.save_as_path:
                        save_qr=self.save_as_path
                    else:
                        return False
                else:
                    save_qr=self.output_file_data.get_text()

                generator.generate_email(receiver, subject, body, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
            except Exception as ex:
                if ex:
                    self.check_for_data_overflow_err(ex, self.more_info_btn)
                    self.warning_label.set_label(str(ex))
                else:
                    self.more_info_btn.set_visible(False)
                    self.warning_label.set_label("Unable to generate QR-Code!")
                self.warning_bar.set_revealed(True)
        else:
            self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)
    
    def generate_contact_details(self, widget):
        name=self.name_data.get_text()
        org=self.organization.get_text()
        phone=self.phone_num.get_text()
        cell=self.cell_phone_num.get_text()
        fax=self.fax.get_text()
        email=self.email.get_text()
        country=self.country.get_text()
        state=self.state.get_text()
        city=self.city.get_text()
        street=self.street.get_text()
        postcode=self.postcode.get_text()
        website=self.website.get_text()
        self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
        try:
            if self.save_qr_as.get_active():
                self.save_qr_dialog()
                if self.save_as_path:
                    save_qr=self.save_as_path
                else:
                    return False
            else:
                save_qr=self.output_file_data.get_text()

            generator.generate_contact_details(name, org, phone, email, cell, fax, street, city, state, postcode, country, website,
            self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
            eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
        except Exception as ex:
            if ex:
                self.check_for_data_overflow_err(ex, self.more_info_btn)
                self.warning_label.set_label(str(ex))
            else:
                self.more_info_btn.set_visible(False)
                self.warning_label.set_label("Unable to generate QR-Code!")
            self.warning_bar.set_revealed(True)
    
    def generate_event(self, widget):
        start_day=str(self.start_day)
        start_month=str(self.start_month)
        start_year=str(self.start_year)
        start_hour=str(self.start_hour.get_value_as_int())
        start_minute=str(self.start_minute.get_value_as_int())
        end_day=str(self.end_day)
        end_month=str(self.end_month)
        end_year=str(self.end_year)
        end_hour=str(self.end_hour.get_value_as_int())
        end_minute=str(self.end_minute.get_value_as_int())
        title=self.event_title.get_text()
        location=self.location.get_text()
        if len(start_day)==1:
            start_day="0"+str(start_day)
        if len(start_month)==1:
            start_month="0"+str(start_month)
        if len(start_hour)==1:
            start_hour="0"+str(start_hour)
        if len(start_minute)==1:
            start_minute="0"+str(start_minute)
        if len(end_day)==1:
            end_day="0"+str(end_day)
        if len(end_month)==1:
            end_month="0"+str(end_month)
        if len(end_hour)==1:
            end_hour="0"+str(end_hour)
        if len(end_minute)==1:
            end_minute="0"+str(end_minute)
        string_start="%s%s%sT%s%s00Z"%(start_year, start_month, start_day, start_hour, start_minute)
        string_end="%s%s%sT%s%sd00Z"%(end_year, end_month, end_day, end_hour, end_minute)
        if not end_year:
            end_hour=""
            end_minute=""
            string_end="T"
        self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
        if title:
            try:
                if self.save_qr_as.get_active():
                    self.save_qr_dialog()
                    if self.save_as_path:
                        save_qr=self.save_as_path
                    else:
                        return False
                else:
                    save_qr=self.output_file_data.get_text()

                generator.genereate_event(title, location, string_start, string_end, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
            
            except Exception as ex:
                if ex:
                    self.check_for_data_overflow_err(ex, self.more_info_btn)
                    self.warning_label.set_label(str(ex))
                else:
                    self.more_info_btn.set_visible(False)
                    self.warning_label.set_label("Unable to generate QR-Code!")
                self.warning_bar.set_revealed(True)
        else:
            self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)
    
    def generate_social(self, widget):      
        if self.social_type_skype_radio_btn.get_active(): 
            username_skype=self.skype_username.get_text()
            mode_skype=self.chat_type.get_active()
            print(mode_skype)
            print(username_skype)
            if mode_skype==True:
                mode_skype="call"
            else:
                mode_skype="chat"
            if username_skype:
                self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
                try:
                    if self.save_qr_as.get_active():
                        self.save_qr_dialog()
                        if self.save_as_path:
                            save_qr=self.save_as_path
                        else:
                            return False
                    else:
                        save_qr=self.output_file_data.get_text()

                    generator.generate_skype(mode_skype, username_skype, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                    eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
                except Exception as ex:
                    if ex:
                        self.check_for_data_overflow_err(ex, self.more_info_btn)
                        self.warning_label.set_label(str(ex))
                    else:
                        self.more_info_btn.set_visible(False)
                        self.warning_label.set_label("Unable to generate QR-Code!")
                    self.warning_bar.set_revealed(True)
            else:
                self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)
        
        else:
            id=self.zoom_id.get_text()
            passwd=self.zoom_passwd.get_text()
            if id and passwd:
                self.get_bg_fg_qr_color_data(self.fg_color, self.bg_color)
                try:
                    if self.save_qr_as.get_active():
                        self.save_qr_dialog()
                        if self.save_as_path:
                            save_qr=self.save_as_path
                        else:
                            return False
                    else:
                        save_qr=self.output_file_data.get_text()

                    generator.generate_zoom(id, passwd, self.qr_version.get_value_as_int(), self.boxsize.get_value_as_int(), self.border.get_value_as_int(), eval(self.fg_color_data[0]),
                    eval(self.bg_color_data[0]), self.logo_file_data, save_qr, self.logo_width.get_value_as_int(), self.logo_height.get_value_as_int(), self.micro_qr.get_active(), self.micro_qr_scale.get_value_as_int())
                except Exception as ex:
                    if ex:
                        self.check_for_data_overflow_err(ex, self.more_info_btn)
                        self.warning_label.set_label(str(ex))
                    else:
                        self.more_info_btn.set_visible(False)
                        self.warning_label.set_label("Unable to generate QR-Code!")
                    self.warning_bar.set_revealed(True)
            else:
                self.null_data_error(self.more_info_btn, self.warning_label, self.warning_bar)                  

    def no_ext_dlg(self):
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            title="No file extension detected!",
            text="No file extnsion was detected in the filename!\nDefaulting to \".PNG\".\nAny existing files with the same name will be replaced!",
        )
        r=dialog.run()
        dialog.destroy()
        return r

    def save_qr_dialog(self):
        dialog = Gtk.FileChooserDialog("Please choose a file", self.window,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        dialog.set_do_overwrite_confirmation(True)
        dialog.set_current_name("generated_qr")
        dialog.set_current_folder("/home/%s"%username)
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.save_as_path = dialog.get_filename()
            if not self.save_as_path.lower().endswith((".png", ".jpg", ".pdf", ".eps", ".pbm", ".ppm", ".xbm")):
                #Use default file extension
                dialog.destroy()
                self.no_ext_dlg()              
                self.save_as_path=self.save_as_path+".png"
        elif response == Gtk.ResponseType.CANCEL:
            self.save_as_path=None

        dialog.destroy()

    def on_save_as_switch_activated(self, switch, gparam):
        if switch.get_active():
            self.output_file_box.set_sensitive(False)
        else:
            self.output_file_box.set_sensitive(True)
    
    def on_micro_qr_switch_activated(self, switch, gparam):
        if switch.get_active():
            self.dim_box.set_sensitive(False)
            self.logo_box.set_sensitive(False)
            self.qr_version_box.set_sensitive(False)
            self.boxsize_box.set_sensitive(False)
            self.bg_color_box.set_sensitive(False)
            self.fg_color_box.set_sensitive(False)
            self.micro_qr_box.set_sensitive(True)
        else:
            self.dim_box.set_sensitive(True)
            self.logo_box.set_sensitive(True)
            self.qr_version_box.set_sensitive(True)
            self.boxsize_box.set_sensitive(True)
            self.bg_color_box.set_sensitive(True)
            self.fg_color_box.set_sensitive(True)
            self.micro_qr_box.set_sensitive(False)

    def add_filters(self, dialog):

        filter_png = Gtk.FileFilter()
        filter_png.set_name("PNG Image")
        filter_png.add_pattern("*.png")
        dialog.add_filter(filter_png)
        
        filter_jpg = Gtk.FileFilter()
        filter_jpg.set_name("JPG Image")
        filter_jpg.add_pattern("*.jpg")
        dialog.add_filter(filter_jpg)

        filter_pdf = Gtk.FileFilter()
        filter_pdf.set_name("PDF Document")
        filter_pdf.add_pattern("*.pdf")
        dialog.add_filter(filter_pdf)

        filter_eps = Gtk.FileFilter()
        filter_eps.set_name("EPS Image")
        filter_eps.add_pattern("*.eps")
        dialog.add_filter(filter_eps)

        filter_pbm = Gtk.FileFilter()
        filter_pbm.set_name("PBM Image")
        filter_pbm.add_pattern("*.pbm")
        dialog.add_filter(filter_pbm)

        filter_ppm = Gtk.FileFilter()
        filter_ppm.set_name("PPM Image")
        filter_ppm.add_pattern("*.ppm")
        dialog.add_filter(filter_ppm)

        filter_xbm = Gtk.FileFilter()
        filter_xbm.set_name("XBM Image")
        filter_xbm.add_pattern("*.xbm")
        dialog.add_filter(filter_xbm)

    #QR Reader
    def format_data(self, data):
        if data.startswith("http"):
            data="Website: <a href=\"%s\" title=\"%s\">%s</a>"%(data, data, data)
            return data
        elif data.startswith("MATMSG"):
            email=data.split(':')
            to=email[2].split(';')[0]
            sub=email[3].split(';')[0]
            body=email[4].split(';')[0]
            data="Email to <a href=\"mailto:%s\" title=\"%s\">%s</a>\nSubject:%s\nBody:\n%s"%(to, to, to, sub, body)
            return data
        elif data.startswith("SMSTO"):
            sms=data.split(':')
            num=sms[1]
            mes=sms[2]
            data="SMS to %s\nMessage:\n%s"%(num, mes)
            return data
        
    def read_qr_code(self, image):
        qr_type, data=qr_reader.main(image)
        fdata=self.format_data(str(data))
        return qr_type, data, fdata

    def add_filters_qr_reader(self, dialog):

        filter_png = Gtk.FileFilter()
        filter_png.set_name("PNG Image")
        filter_png.add_pattern("*.png")
        dialog.add_filter(filter_png)
        
        filter_jpg = Gtk.FileFilter()
        filter_jpg.set_name("JPG Image")
        filter_jpg.add_pattern("*.jpg")
        dialog.add_filter(filter_jpg)

    def choose_qr_code_file(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Choose a file", parent=self.window, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        dialog.add_filter(self.logo_chooser_filter) #PNG, JPG, JPEG File Filters
        dialog.set_current_folder("/home/%s"%username)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.path_to_qr_code_to_read=dialog.get_filename().split("/")
            self.select_qr_code_btn.set_label(self.path_to_qr_code_to_read[len(self.path_to_qr_code_to_read)-1])
            self.qr_type, self.data, self.fdata=self.read_qr_code(dialog.get_filename())
            self.raw_data_out.set_text(self.data)
            self.formatted_data_out.set_markup("Detected %s\n%s"%(self.qr_type, self.fdata))
            #self.formatted_data_out.set_text()
            print("Type: "+self.qr_type+"\nData: "+self.data)
        elif response == Gtk.ResponseType.CANCEL:
            self.path_to_qr_code_to_read="False"

        dialog.destroy()

window=main_win()
Gtk.main()
