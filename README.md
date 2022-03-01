# LaTeX-Vorlage für die FOM Hochschule für Oekonomie & Management - ITM Leitfaden

[![Build](https://github.com/andygrunwald/FOM-LaTeX-Template/actions/workflows/Check.yml/badge.svg)](https://github.com/andygrunwald/FOM-LaTeX-Template/actions/workflows/Check.yml)

Eine [LaTeX](https://de.wikipedia.org/wiki/LaTeX)-Vorlage für den persönlichen Gebrauch für Haus-, Seminar-, Bachelor und Master-Arbeiten an der [FOM Hochschule für Oekonomie & Management](https://www.fom.de/). Das Template entspricht dem aktuellen Stand des Leitfadens ITM in Version 1.2.

Wie das **Ergebnis** aussieht, könnt ihr euch in der Datei [*thesis_main.pdf*](./thesis_main.pdf) ansehen.

Diese Vorlage hat weder einen Anspruch auf Richtigkeit, noch auf Vollständigkeit (ITM-Leitfaden Version 1.2).
Verbesserungen sind jederzeit willkommen. Dies ist ein Fork von https://github.com/andygrunwald/FOM-LaTeX-Template, welches meine persönlichen Bedürfnisse und Designentscheidungen wiederspiegelt. 


---

## Inhaltsverzeichnis

- [LaTeX-Vorlage für die FOM Hochschule für Oekonomie & Management - ITM Leitfaden](#latex-vorlage-für-die-fom-hochschule-für-oekonomie--management---itm-leitfaden)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Für die eigene Arbeit nutzen](#für-die-eigene-arbeit-nutzen)
  - [Vorlage personalisieren](#vorlage-personalisieren)
  - [Unterschiedliche Anforderungen](#unterschiedliche-anforderungen)
  - [Dokumentensprache](#dokumentensprache)
  - [TextCommands](#textcommands)
  - [Zitation](#zitation)
    - [IEEE-Style im Text](#ieee-style-im-text)
  - [Inhaltsverzeichnis Latex](#inhaltsverzeichnis-latex)
  - [Literaturverzeichnis](#literaturverzeichnis)
  - [Sperrvermerk](#sperrvermerk)
  - [Quellcode einbinden](#quellcode-einbinden)
  - [Schriftarten](#schriftarten)
  - [LaTeX zu PDF kompilieren](#latex-zu-pdf-kompilieren)
  - [IDE zur Bearbeitung nutzen](#ide-zur-bearbeitung-nutzen)
    - [Texpad](#texpad)
    - [Visual Studio Code](#visual-studio-code)
  - [Overleaf zur Bearbeitung nutzen](#overleaf-zur-bearbeitung-nutzen)
  - [Wörter zählen](#wörter-zählen)
  - [/tools](#tools)
  - [Disclaimer](#disclaimer)
  - [Lizenz](#lizenz)
    - [TexCount v3.2](#texcount-v32)

## Für die eigene Arbeit nutzen

Aufgrund der gewählten [Lizenz](./LICENSE) [MIT Lizenz](https://en.wikipedia.org/wiki/MIT_License), darfst du diese Vorlage für den persönlichen oder kommerziellen Gebrauch nutzen und abändern.
Um dies zu tun, gibt es mehrere Möglichkeiten, die wir nachfolgend kurz vorstellen.

**Generell gilt**:
Dieses Dokument beschreibt eine ganze Menge Details, die dir beim Erstellen und bearbeiten des Dokuments hilfreich sein könnten.
Leider wird es unmöglich sein, jede Frage abzudecken.
Solltest du uns kontaktieren wollen, um eine Frage zu stellen, ein Problem mit zuteilen oder um einfach nur mal Danke sagen zu wollen, eröffne doch ein Issue in diesem Projekt.

## Vorlage personalisieren

Wenn du diese Vorlage nutzt, ist der erste Einstiegspunkt die Datei [`skripte/meta.tex`](./skripte/meta.tex).
In der Datei haben wir einige Variablen hinterlegt, die im Dokument (u. a. auf dem Deckblatt) genutzt werden.

Ersetze die Muster-Werte durch deine persönlichen Angaben und diese werden automatisch im Dokument verwendet.

## Unterschiedliche Anforderungen 

Um den Anforderungen von unterschiedlichen Dozenten zu begegnen werden verschiedene Versionen der main-Branch mit den Dozenten-spezifischen Anpassungen in seperaten Branches gepflegt. 

## Dokumentensprache

Die Vorlage ist sowohl auf Deutsch, als auch auf Englisch umgesetzt. Dadurch wird das Titelblatt, Verzeichnisüberschriften und auch der Inhalt des Literaturverzeichnisses auf die englische Sprache umgestellt.
Um die Datei auf Englisch zu kompilieren, muss mit docker-compose folgender Befehl umgesetzt werden:
```
docker-compose run --service-ports fom ./compile.sh en
```
Ohne Docker muss die Datei mit der compile.sh folgendermaßen aufgerufen werden:
```
./compile.sh en
```
Für die Batch-Datei ist das Kompilieren auf Englisch über folgenden Workaround möglich.
1. Suche in der thesis_main.tex nach der Codezeile `%\def\FOMEN{}`
2. Entkommentiere diese Codezeile, indem du das Prozentzeichen entfernst
3. Kompiliere neu

Anmerkung: Der beschriebene Workaround funktioniert auch, wenn du Overleaf oder einen anderen TEX-Editor verwendest und die compile.bat nicht benötigst.

Nach dem kompilieren findet sich das Ergebnis in der Datei [`thesis_main.pdf`](./thesis_main.pdf). Die [`thesis_englisch.pdf`](./thesis_englisch.pdf) ist nur dazu da auf Github die Möglichkeit aufzuzeigen.

## TextCommands

Das Arbeiten mit Commands innerhalb des Textes kann eine schöne Möglichkeit darstellen um:
- Wörter oder Abkürzungen, welche häufig falsch geschrieben werden, einmalig zu definieren
- bestimmte Wörter die z. B. einfach zu lang sind durch ein Kürzel schneller schreiben zu können
- Wörter oder Abkürzungen die häufig verwendet werden nie an der falschen Stelle zu trenen

In meinen Arbeiten haben ich gemerkt, dass es sinnvoll ist verschiedene standard Abkürzungen zu verwenden und diese nur einmalig zu definieren. Beispielsweise habe ich die Abkürzung von "zum Beispiel" --> "z. B." immer ohne Leerzeichen geschrieben. Allerdings ist die Schreibweise mit Leerzeichen [wesentlich korrekter](https://de.wiktionary.org/wiki/z._B.#:~:text=Anmerkung%3A,z.B.). Einmal richtig definiert, lässt sich die Abkürzung "z. B." im Text-File einfach durch folgenden Code aufrufen:
```
\zb
```
Man sparrt sich sogar 2 Tastaturanschläge ;-)

Auf der Seite skripte\textcommands.tex befinden sich zwei Bereiche:
- common textCommands
- project individual textCommands

Hier könnt ihr die verschiedenen Commands definieren und dann sind sie auch zentral an einer Stelle verfügbar und pflegbar.

TextCommands können bei Bedarf auch zweisprachig gepflegt werden:
```
\newcommand{\vglf}{\langde{Vgl.}\langen{compare}}
```

## Zitation
Es gibt viele Zitationsstile, deshalb schaut ihr am besten in den für euch gültigen Leitfaden und sprecht dann die präferierte/vorgegebene Zitationsweise mit eurem Dozenten ab.

### IEEE-Style im Text
**Achtung, nur im Hochschulbereich IT-Management**

Dies ist das aktuelle Standardformat

Der IEEE Zitationsstil wird hauptsächlich in technischen Studiengängen verwendet und ist ein sehr einfacher Zitationsstil, da hier nicht auf Dinge wie z.B. "vgl."/"ebd." geachtet werden muss. Ein direktes Zitat steht in Anführungszeichen. Wird ohne Anführungszeichen zitiert weiß man, dass es ein indirektes Zitat ist ("vgl." kann dann weg gelassen werden). Normalerweise müssten auch keine Seitenzahlen angegeben werden, jedoch steht im aktuellen Leitfaden des Hochschulbereichs IT-Management, dass bei jeglicher Zitationsweise die Seitenzahl anzugeben ist, deshalb auch bei IEEE.

## Inhaltsverzeichnis Latex

**Ebene des ausgegebenen Inhaltsverzeichnis einstellen**<br>
Bis zu welcher Ebene das Inhaltsverzeichnis aufgelistet wird, kann über tocdepth Parameter eingestellt werden
```latex
\setcounter{tocdepth}{4}
```

**Tabellen- und Abbildungsverzeichnis im Inhaltsverzeichnis**<br>
Die Anzeige des Tabbellen- und des Abbildungsverzeichnis lässt sich gleich am Anfang in der \documentclass einstellen.

**Glossar im Inhaltsverzeichnis**<br>
Folgenden Eintrag auskommentieren, damit das Glossar nicht im Inhaltsverzeichnis angezeigt wird
```latex
\glstoctrue
```

**Symbolverzeichnis**<br>
Damit das Symbolverzeichnis nicht mehr angezeigt wird, folgendes auskommentieren
```latex
 \addcontentsline{toc}{section}{Symbolverzeichnis}
```

**Abkürzungsverzeichnis**<br>
Damit das Symbolverzeichnis nicht mehr angezeigt wird, folgendes auskommentieren
```latex
\addcontentsline{toc}{section}{Abkürzungsverzeichnis}
```

## Literaturverzeichnis

Einige Professoren bevorzugen ein sortiertes (Webseite, Buch, Artikel...) Literaturverzeichnis.
Dies kann mit folgender Änderung im Quellcode ([*thesis_main.tex*](./thesis_main.tex)) erreicht werden:

Zunächst diese Zeile auskommentieren:

```latex
%\printbibliography
```

Und die folgenden Zeilen einkommentieren und ggf. anpassen.

```latex
\printbibheading
\printbibliography[type=article,heading=subbibliography,title={Artikel}]
\printbibliography[type=book,heading=subbibliography,title={Bücher}]
\printbibliography[type=online,heading=subbibliography,title={Webseiten}]
```

## Sperrvermerk

Sollte ein Sperrvermerk für die Arbeit notwendig sein, so kann dieser durch Einkommentieren der folgenden Zeile aktiviert werden:

```latex
\input{kapitel/anhang/sperrvermerk}
```

Die Angaben zu Titel der Arbeit und Name der Firma werden dabei aus den Metadaten entnommen.

## Quellcode einbinden

Um euren Quellcode einzubinden, wurde bereits das Paket *listings* in der Datei [*thesis_main.tex*](./thesis_main.tex) eingebunden.
Dieses wird dort auch mit den Farben für Kommentare, Strings, etc. konfiguriert.
Folgendermaßen könnt ihr Quellcode einbauen:

```latex
\lstinputlisting[language=JavaScript]{./Quellcode/Dateiname.js}
```

Für [Javascript](https://de.wikipedia.org/wiki/JavaScript) wurde eine eigene Definition erstellt und eingebaut. 
Für eine genauere Beschreibung aller im Standard verfügbaren Sprachen empfehlen wir folgenden Artikel: [LaTeX/Source Code Listings @ Wikibooks](http://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings).

## Schriftarten

Die voreingestellte Schriftart enthält Serifen. Mit den folgenden Zeilen kann in der Datei [*thesis_main.tex*](./thesis_main.tex) die Nutzung der Schriftart Helvet erzwungen werden.

```latex
% Überschreibe die default Schriftart mit helvet
\usepackage[scaled]{helvet}
\renewcommand\familydefault{\sfdefault}
```


## LaTeX zu PDF kompilieren

Wir empfehlen das Dokument mit Docker (siehe unten) zu kompilieren.

Alternativ kann auch über die Ausführung der Skripte kompiliert werden, dafür müssen aber die unten beschriebenen [LaTeX-Pakete](#latex-pakete) installiert sein.
Unter **Windows** muss dafür die beiliegende `compile.bat` ausführen.
Benutzer von **macOS** und **Linux** verwenden bitte die ```compile.sh```.


Wenn das Kompilieren nicht ohne Fehler möglich ist, kontrolliert bitte ganz genau eure LaTeX-Versionen oder nutzt Docker.


## IDE zur Bearbeitung nutzen

Prinzipiell reicht ein normaler Text-Editor zur Bearbeitung aus.
Jedoch kannst du zum Schreiben der Arbeit auch ein IDE verwenden.
Hierzu gibt es nachfolgend einige Software:

- [TeXstudio](http://texstudio.sourceforge.net/) (Windows, macOS, Linux)
- [Texpad](https://www.texpadapp.com/) (macOS, iOS)
- [Visual Studio Code](https://code.visualstudio.com/) (macOS, iOS, Linux)

### Texpad

Für die Nutzung von Texpad unter macOS müssen einige Einstellungen beachtet werden.
Standardmäßig ist _biber_ nicht aktiviert.
Dies führt dazu, dass das Literaturverzeichnis einfach "verschwindet", wenn man mit Texpad kompliliert.
Daher musst Du unter _Preferences_ > _Typesettings_ > _Bibliography Compilation_ als Engine _biber_ auswählen.

### Visual Studio Code

Wer eine etwas moderne IDE benutzen möchte, kann auch Visual Studio Code verwenden. Folgende Extension ist notwendig:

[Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

Mit Hilfe der Extension kann das Projekt kompiliert und als Vorschau angesehen werden. In der ```settings.json``` sind die Einstellungen der ```compile.sh``` für Latex Workshop hinterlegt.

Zusätzlich kann die Extension [LTeX](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex) hilfreich sein, die eine **offline Grammatik- und Rechtschreibprüfung** für LaTeX-Dokumente bietet.

## Overleaf zur Bearbeitung nutzen

Anstatt dir einen TEX-Editor und alle weiteren Pakete selber zu installieren und wie oben beschrieben zu kompilieren etc. kannst du auch Online-Tools wie Overleaf (https://www.overleaf.com/) verwenden. Beides hat seine Vor- und Nachteile auf die hier nicht näher eingegangen wird.

Zum Einbinden dieser Vorlage in Overleaf gibt es zwei Möglichkeiten:
1. Der [klassische Download](#klassischer-download) wonach du das ZIP-File einfach bei Overleaf wieder hochlädst.
2. Du kannst deinen [Fork von Github](#fork-auf-github) in Overleaf einbinden.

## Wörter zählen

Gerade bei der Verwendung eines Texteditors ist das Zählen der Wörter unter umständen eine mühselige Aufgabe. Mit den folgenden Vorschlägen kann man die Wörter der Arbeit zählen:

- Über die Seite [TeXcount](https://app.uio.no/ifi/texcount/online.php) können Latex Dateien hochgeladen und gezählt werden.
- Unter Unix und macOS kann das mitgelieferte Script helfen die Wörter zu zählen. Dafür muss nur `perl` installiert sein. Das Skript wird einfach über `sh ./countwords.sh` gestartet und führt die entsprechenden Perl-Skripte zum Zählen der Wörter aus. 

## /tools 

Hier finden sich verschiedene Python-Skripte die als Basis zur Generierung von spezifischen Graphen z.B Wordclouds oder Pie-Charts aus der Bibliografie genutzt werden. Diese Skripte benötigen manuelle Anpassungen und werden nicht mit allen Bibliografien standardmäßig funktionieren.

## Disclaimer

Die Nutzung des Projektes ist auf eigene Gefahr und es kann keine Vollständigkeit gewährleistet werden.
Bitte überprüfe das Ergebnis erneut anhand der entsprechenden Leitfäden deines Studiengangs.
Einzelne Standorte und Professoren stellen abgeänderte Leitfäden bereit.

## Lizenz

Dieses Projekt ist unter den Bedingungen der [MIT Lizenz](http://en.wikipedia.org/wiki/MIT_License) öffentlich verfügbar.

Folgende Software ist im Projekt inkludiert 

### TexCount v3.2 
```
TeXcount version 3.2

Copyright 2008-2020 Einar Andreas Rodland

The TeXcount script is published under the LaTeX Project Public License (LPPL)
  https://www.latex-project.org/lppl.txt
which grants you, the user, the right to use, modify and distribute the script. However, if the script is modified, you
must change its name or use other technical means to avoid confusion.

The script has LPPL status "maintained" with Einar Andreas Rodland being the current maintainer.```