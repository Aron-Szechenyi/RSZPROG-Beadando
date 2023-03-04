import sqlite3

import config
from writer import Writer


class SqlWriter(Writer):
    con = None
    tags = []

    def __int__(self, collection, output_path, tags):
        super(collection, output_path)

    def connect(self):
        self.con = sqlite3.connect(self.output_path)

    def create_table_from_tags(self, tags):
        self.tags = tags
        sql_ = "CREATE TABLE IF NOT EXISTS " + config.table_name + " ("

        for item in self.tags:
            sql_ += item + " varchar(255), "

        sql_ = sql_[0:-2] + ");"
        self.con.cursor().execute(sql_)

    def insert_data(self):
        sql_ = "INSERT OR IGNORE INTO " + config.table_name + " VALUES ("
        for i in range(len(self.tags)):
            sql_ += "?, "
        sql_ = sql_[0:-2] + ");"

        cur = self.con.cursor()

        for i in range(len(self.collection)):
            records = []

            for item in self.tags:
                records.append(self.collection[i][item])
            cur.execute(sql_, records)

        self.con.commit()
        self.con.close()
