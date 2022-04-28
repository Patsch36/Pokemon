# Pokemon
Pygames Implementierg eines Open Wolrd 2D games mit automatischr Map- Generierung und Datenverwaltung/ Bearbeitung

## To Do:
- [ ] docstring (""" bla """) -> mit test: (wie könnte man testen) mit mkdocs html seite erstellen
- [ ] **PS** Spielfeld dynamisch erstellen 
- [ ] wetter api nutzen um wetter einzubinden (Standord-api/ IP API benötigt)
- [ ] Grafik von Uhrzeit abhängig machen
- [ ] **PS** Blockaden einfügen
- [ ] **SB** SQL Datenbank aufsetzen und einbinden
  - [ ] **SB** Konzept für keys abhängig von der Sprache
  - [ ] **SB** Übersetzen von icht vorhandener Sprache mit DeeplIO und anschließendes eintragen in die Datenbank
- [ ] **PS** Verschiedene CSV- Dateien fürs Levelerstellen

## Ideen:
- [ ] Beliebte Standorte tracken, zwischenspeichern, und die zwei Häufigsten an die Deutsche Bahn senden, die dann Ticktwerbung zwischen den zwei Standorten inGame anzeigt
- [ ] Installationspaket mit allen benötigten Bibliotheken

```python
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
```

```python
import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

def should_install_requirement(requirement):
    should_install = False
    try:
        pkg_resources.require(requirement)
    except (DistributionNotFound, VersionConflict):
        should_install = True
    return should_install


def install_packages(requirement_list):
    try:
        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        if len(requirements) > 0:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
        else:
            print("Requirements already satisfied.")

    except Exception as e:
        print(e)
```
