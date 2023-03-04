import yaml
import config


class Loader:
    loader_string = None
    fields = None
    output_file = None
    data_file = None

    def __init__(self, s_string):
        self.loader_string = s_string

    def load(self):
        with open(self.loader_string, "r") as stream:
            data_loaded = yaml.safe_load(stream)
        fields = data_loaded["fields"]

        for i in range(0, len(fields), 2):
            if i+1 >= len(fields):
                break

            temp = fields[i]
            fields[i] = fields[i+1]
            fields[i+1] = temp

        self.fields = fields
        config.output_file = data_loaded["output_file"]
        config.data_file = data_loaded["data_file"]
        config.table_name = data_loaded["table_name"]

