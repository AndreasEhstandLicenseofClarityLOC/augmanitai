Text und Beispieldaten mit KI erstellt.

# Korrekturen mit Anlass und Folgeprüfung festhalten

Eine KI-Ausgabe wurde korrigiert. Welche frühere Aussage wurde ersetzt, woher stammt der Anlass und welche weiteren Texte müssen noch geprüft werden? Ein kurzer Korrektureintrag kann diese Angaben zusammenhalten.

Dieses Material ergänzt [AGENT_BRIEF.md](AGENT_BRIEF.md): Dort geht es um Ziel, Befugnis, Fertigkriterium, Stoppregel und Beleg eines Auftrags. Hier geht es um eine Änderung an einer bereits vorliegenden Ausgabe.

## Ein konstruiertes Beispiel

Für ein erfundenes Büchertauschregal formuliert eine KI einen Hinweis. Alle folgenden Texte, Kennungen und Versionen sind synthetisch:

| Fassung | Inhalt |
|---|---|
| Aushang `aushang-v1`, Abschnitt „Annahme“ | Wir nehmen nur Bücher an. |
| Bisheriger Hinweis `hinweis-v1` | Bücher und Spiele sind willkommen. |
| Überarbeiteter Hinweis `hinweis-v2` | Bücher sind willkommen. |
| Noch zu prüfende Kurzfassung `kurzfassung-v1` | Bücher und Spiele willkommen. |

Der Anlass der Korrektur ist eine übersehene Angabe im vorhandenen Aushang. Der neue Hinweis entfernt „Spiele“. Die Kurzfassung enthält die alte Angabe weiterhin und bleibt als offene Folgeprüfung vermerkt.

## Die Beispieldatei lesen

[correction-record-example.json](correction-record-example.json) enthält den Eintrag samt Ausgangstexten. Die Kennungen verweisen auf die in derselben Datei gespeicherten Fassungen:

- `sources`: Ausgangsmaterial mit Version und Fundstelle.
- `outputs`: frühere, überarbeitete und noch zu prüfende Texte.
- `correction`: Verbindung zwischen den Hinweisfassungen, bisherige Aussage, Änderungsanlass und neue Aussage.
- `follow_up`: betroffene Kurzfassung, Vergleichsquelle, Prüfauftrag und Status `offen`.

So lassen sich Änderung und Folgeprüfung getrennt lesen. Die Korrektur des Hinweises bedeutet nicht, dass die Kurzfassung bereits bearbeitet wurde. Ihr Status sollte erst nach dem Vergleich wechseln; eine daraufhin geänderte Kurzfassung braucht eine eigene, erhaltene Fassung. Kennungen allein bewahren keine Inhalte.

Auch der Anlass kann unterschiedlich sein: Eine übersehene Quellenangabe, eine neue Information oder ein geänderter Nutzerwunsch sollten als solche erkennbar bleiben. Im Beispiel bezeichnet `overlooked_source` ausschließlich den ersten Fall.

## Hintergrund und Einordnung

Das W3C-Datenmodell PROV beschreibt unter anderem die Beziehung zwischen einer Revision und ihrer vorherigen Fassung. Dies ist der begriffliche Hintergrund des Beispiels. Die hier verwendeten Felder sind ein eigener praktischer Vorschlag, keine PROV-Implementierung und keine Studie.

- [W3C PROV-DM, insbesondere Abschnitt 5.2.2 „Revision“](https://www.w3.org/TR/prov-dm/)
- [Begleittext: Was eine KI-Korrektur zum Nachlesen braucht](https://medium.com/@augmanitai/was-eine-ki-korrektur-zum-nachlesen-braucht-89cbace519f3)

## English summary

AI-generated text and example data. This synthetic book-exchange example connects an earlier statement, its correction and the source that prompted the change. A separate summary still contains the old claim and remains marked for review. The record complements the task brief with a way to document corrections; it is a practical proposal, not a PROV implementation or a study.

