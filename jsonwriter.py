from writer import Writer
import json


class JsonWriter(Writer):
    def __int__(self, collection, output_path):
        super(collection, output_path)

    def write(self, data):
        with open(self.output_path, "w") as write_file:
            json.dump(data, write_file)
