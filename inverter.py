import os
from datetime import datetime as dt
import tkinter as tk
import tkinter.filedialog as filedialog
# from PIL import ImageTk, Image
import xml.etree.ElementTree as ET
import parsers
from Invoice import Invoice


def save_epp(metadata, invoice_list):
    f = filedialog.asksaveasfile(mode='w', defaultextension=".epp")
    if f is None:  # None is returned if user cancels.
        return
    f.write("[INFO]")
    f.write("\n")
    # f.write("\"1.07\",0,1250,\"Inverter\",,,,,,,,,,,,1,20190501000000,20190531000000,,20190531145803,"Polska","PL",,1")
    # 1,20190501000000,20190531000000 == tak, podajemy zakres dat, początek zakresu dat, koniec zakresu dat
    f.write(f"\"1.07\",0,1250,\"Inverter\",,,,,,,,,,,,0,19000101000000,20501231000000,,{metadata['communication_date']},\"Polska\",\"PL\",,1")
    f.write("\n")
    f.write("\n")
    for invoice in invoice_list:
        f.write(invoice.to_epp())
    f.close()


def get_xml_type(xml_file_root):
    tag = xml_file_root.tag
    if "Batch" in tag:
        return 0
    elif "invoice" in tag:
        return 1
    else:
        raise RuntimeError("Nieznany typ pliku xml.")


def open_xml():
    xml_file = filedialog.askopenfile(mode="r")
    # tree = ET.parse('example_data/jotim_04_2021.xml')
    if xml_file:
        tree = ET.parse(xml_file.name)
        root = tree.getroot()
        xml_type = get_xml_type(root)
        return root, xml_type


def xml_parser_router(xml_type):
    if xml_type == 0:
        return parsers.parser_0
    elif xml_type == 1:
        return parsers.parser_1
    else:
        raise RuntimeError("Unknown xml_type passed to xml_parser_router.")


def operate():
    to_unpack = open_xml()
    if to_unpack:
        document, xml_type = to_unpack
        xml_parser_function = xml_parser_router(xml_type)
        metadata, invoice_list = xml_parser_function(document)
        save_epp(metadata, invoice_list)

window = tk.Tk()
window.title('Inverter - konwerter faktur')
window.resizable(False, False)
window.geometry('280x250')
button = tk.Button(window, text="Kliknij tutaj, aby rozpocząć", command=operate)
button.pack(expand=True)
copyright_notice = tk.Label(text="Copyright © 2021 Krzysztof Setlak IT Consulting")
copyright_notice.pack()
# canv = tk.Canvas(window, bg="white", bd=10, height=250, width=250)
# img = ImageTk.PhotoImage(Image.open("assets/dnd_banner.png"))
# canv.create_image(10, 10, image=img, anchor='nw')
# canv.pack()


window.mainloop()
