import eel
from jinja2 import Template
from scripts.leadgen import leadogenerator
from scripts.csv_faker import faker_csv

eel.init("web")


@eel.expose
def send(url, login, password, sum, order ):
    print(url, login)
    leadogenerator(url, login, password, sum, order)


@eel.expose
def faking():
    faker_csv()


@eel.expose
def test():
    print()


@eel.expose
def end_leadgen():
    print()

try:
    eel.start("/templates/index.html", size=(800, 800), jinja_templates='templates', port=8080)
except (SystemExit, MemoryError, KeyboardInterrupt):
    # We can do something here if needed
    # But if we don't catch these safely, the script will crash
    pass
