from loader import Loader
from ui import Ui

Loader = Loader("conf.yaml")
Loader.load()

Ui = Ui()
Ui.add_fields(Loader.fields)


Ui.show()
