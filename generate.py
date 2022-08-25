# generate.py
from jinja2 import Environment, FileSystemLoader

inputbase = "."
project ="project"
app = "app"
outputbase = "project/" + project +"/"

environment = Environment(loader=FileSystemLoader(inputbase + "setup-files/"))

models = [
    {"name": "Server"},
    {"name": "Mailbox"},
    {"name": "Termin"},
    {"name": "Kontakt"},
    {"name": "Vorlage"},
]

# string functions
# "".lower()
# "".capitalize()

def write(filename, content):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(content)
        print(f"... wrote {filename}")

def viewsets():
    template = environment.get_template("setup-viewset.txt")
    for model in models:
        content = template.render(model)
        filename = outputbase + "viewsets/" + model['name'] + "ViewSet.py"
        write(filename, content)

def serializers():
    template = environment.get_template("setup-serializer.txt")
    for model in models:
        content = template.render(model)
        filename = outputbase  + "serializers/" + model['name'] + "Serializer.py"
        write(filename, content)

def initModels():
    template = environment.get_template("setup-model.txt")
    for model in models:
        #filename = outputbase + f"message_{model['name'].lower()}.txt"
        filename = outputbase  + "models/" + model['name'] +".py"
        content = template.render(model)
        write(filename, content)

    filename = outputbase + "models/__init__.py"
    content =""
    for model in models:
        content += "from ." + model +" import *"
        content += "\n"
    write(filename, content)

viewsets()
initModels()
serializers()
