import tkinter
import collections
from tkinter import *
import config
from jsonwriter import JsonWriter
from sqlwriter import SqlWriter


class Ui:
    ui_window, writer = None, None
    ui_entries_list = collections.deque()
    collection, tags = [], []

    def __init__(self):
        self.ui_window = Tk()
        self.ui_window.title("a3kwh7")

    def show(self):
        self.ui_window.mainloop()

    def exit(self):
        json_writer = JsonWriter(self.collection, config.output_file)
        json_writer.create_dir()
        json_writer.write(self.collection)

        sql_write = SqlWriter(self.collection, config.data_file)
        sql_write.create_dir()
        sql_write.connect()
        sql_write.create_table_from_tags(self.tags)
        sql_write.insert_data()

        self.ui_window.destroy()

    def save(self):
        tmp_collection = dict()

        for i in range(len(self.ui_entries_list)):
            tmp_collection[self.tags[i]] = self.ui_entries_list[i].get()
        self.collection.append(tmp_collection)
        self.clear_entries()

    def clear_entries(self):
        for item in self.ui_entries_list:
            item.delete(0, END)

    def save_tags(self, list_elements):
        for i in reversed(range(len(list_elements))):
            if i % 2 != 0:
                self.tags.append(list_elements[i]["field_name"])

    def add_fields(self, list_elements):
        length = len(list_elements)

        for i in range(length):
            if i % 2 == 0:
                Label(self.ui_window, text=list_elements[i]["label"]).grid(column=0, row=i, sticky="w")
            else:
                self.ui_entries_list.append(
                    tkinter.Entry(self.ui_window)
                )
                self.ui_entries_list[-1].grid(column=1, row=i - 1)

        Button(self.ui_window, text="Mentés", command=self.save).grid(column=0, row=length)
        Button(self.ui_window, text="Kilépés", command=self.exit).grid(column=1, row=length)
        self.save_tags(list_elements)
