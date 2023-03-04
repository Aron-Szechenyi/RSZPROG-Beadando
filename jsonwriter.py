from writer import Writer
import json


class JsonWriter(Writer):
    def __int__(self, collection, output_path):
        super().__init__(self, collection, output_path)

    def write(self):
        json_object = json.dumps(self.collection)
        print(json_object)
        with open(self.output_path, "w+") as outfile:
            outfile.write(json_object)
