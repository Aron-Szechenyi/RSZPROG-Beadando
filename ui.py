import tkinter
import collections
from tkinter import *
import config
from jsonwriter import JsonWriter


class Ui:
    ui_window = None
    ui_elements_list = collections.deque()
    writer = None
    collection = []

    def __init__(self):
        self.ui_window = Tk()
        self.ui_window.title("a3kwh7")
        pass

    def show(self):
        self.ui_window.mainloop()
        pass

    def exit(self):
        a = JsonWriter(self.collection, config.output_file)
        a.write()

    def save(self):
        tmp_collection = []
        for i in range(len(self.ui_elements_list)):
            if i % 2 == 0:
                tmp_collection.append(self.ui_elements_list[i].cget("text"))
            else:
                tmp_collection.append(self.ui_elements_list[i].get())
                self.ui_elements_list[i].delete(0, END)
        self.collection.append(tmp_collection)

    def add_fields(self, list_elements):
        length = len(list_elements)

        for i in range(length):
            if i % 2 == 0:
                self.ui_elements_list.append(
                    Label(self.ui_window, text=list_elements[i]["label"], textvariable=list_elements[i+1])
                )
                print(list_elements[i+1]['field_name'])
                self.ui_elements_list[-1].grid(column=0, row=i, sticky='W')
            else:
                self.ui_elements_list.append(
                    tkinter.Entry(self.ui_window)
                )

                self.ui_elements_list[-1].grid(column=1, row=i - 1)

        Button(self.ui_window, text="Mentés", command=self.save).grid(column=0, row=length)
        Button(self.ui_window, text="Kilépés", command=self.exit).grid(column=1, row=length)
