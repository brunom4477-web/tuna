# Tuna : 14 genres arabes et maghrébins

Ajout à Tuna (GPL-3.0-only, comme le reste) : 14 genres « dans la manière de », qui portent le total de 86 à 100.
Ils se trouvent dans la décennie de leur époque ; le fichier de données est `tools/genres/d_arab.py` (pas de C à écrire : `python3 tools/tuna_genres.py` le transforme).

| Genre | Décennie | Métrique | Gamme (approchée) | Suite d'accords |
| --- | --- | --- | --- | --- |
| TARAB CAIRE | 1950 | 4/4 maqsum, 88 | nahawand = mineur harmonique | i iv V i · VI iv V7 i |
| EL ATRACHE | 1950 | 4/4 maqsum, 96 | bayati ≈ éolien | i VII VI V7 i · iv V i |
| BALADI | 1960 | 4/4, 104 | dorien | i i bVII i |
| MALFUF | 1960 | 2/4, 132 | hijaz = phrygien dominant | I bII I V |
| SAIDI | 1960 | 4/4, 112 | dorien | i i IV i |
| SHAABI | 1970 | 4/4, 118 | mineur harmonique | i iv V i |
| CHAABI MAROC | 1970 | 6/8, 116 | éolien | i VII VI V (cadence andalouse) |
| CHAABI ALGER | 1970 | 4/4, 100 | mineur harmonique | i iv V i · VII VI V7 i |
| RAI | 1980 | 4/4, 108 | phrygien (couleur kurd) | i VII VI VII |
| RAI POP | 1990 | 4/4, 112 | éolien | i VI III VII |
| MEZWED | 1990 | 4/4, 116 | hijaz | I I bII I (bourdon) |
| POP ARABE | 1990 | 4/4, 104 | mineur harmonique | i iv VII III |
| DABKE | 2000 | 4/4, 128 | mineur harmonique | i i V i |
| KHALIJI | 2000 | 2/4, 104 | mixolydien (rast approché) | I bVII I IV |

Percussions : le kick joue le dum de la darbouka, le rim son tek, la conga aiguë son ka, le tambourin le riq ; les rythmes sont le maqsum, baladi, saidi, malfuf, le 6/8 chaabi, la figure raï, la figure mezwed, le dabke…
Instruments : oud, violon, violoncelle, harpe, accordéon, hautbois et cor anglais (pour les anches), banjo, orgue, synthés, basse électrique.

## À savoir
- **Pas de quarts de ton** : le moteur de Tuna joue 12 notes par octave. Le bayati et le rast sont donc joués avec la gamme à 12 notes la plus proche (éolien, mixolydien). Ça sonne « dans le sens » mais pas juste au sens du maqam.
- **Les suites d'accords sont une lecture harmonique** : la musique arabe est modale (mélodie + rythme) ; les accords sont ceux qu'un arrangeur ou un groupe met dessous (cadence andalouse i-VII-VI-V, boucles de pop-raï…). Je ne reproduis la grille d'aucun morceau précis, et les genres du Maghreb sont des **approximations écrites à l'oreille**. À corriger dans `d_arab.py` : les accords (`cycle`), la gamme (`scale`) et les lignes de percussion (en texte).
- Les **codes de partage** et l'ordre de la bibliothèque changent : les genres sont triés par année dans chaque décennie, donc un genre inséré décale les numéros des suivants.
- Compilé et testé **sur ordinateur** (tests de Tuna : théorie, mécanique, séquenceur, préréglages, MIDI ; rendu avec les moteurs de Felucca, sans saturation). **Pas** compilé avec la chaîne JieLi ni essayé sur un FM-1.

## Construire le .fwsc
Dans ta copie (fork) du dépôt, dépose les fichiers de ce paquet à leur place, puis, sur GitHub, lance **Actions → Firmware → Run workflow** : le paquet apparaît dans « Artifacts » (`tuna-firmware`). Sinon : `./build.sh` sur Linux (voir BUILDING.md).
