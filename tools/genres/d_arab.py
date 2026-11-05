# SPDX-License-Identifier: GPL-3.0-only
# TUNA genres of the Arab world and the Maghreb (tools/tuna_genres.py writes them out; the genre's decade puts it in
# the library). Written "in the manner of": Arabic music is modal and mostly melody and rhythm, so a chord loop is a
# harmonic reading of a maqam, the kind a band or an arranger puts under it, not a transcription of any song. TUNA's
# scales have no quarter-tones: bayati and rast are played with their nearest 12-tone scale (aeolian, mixolydian),
# hijaz as phrygian dominant, nahawand as harmonic minor, kurd as phrygian.
#
# Drums: the kick is the darbuka's dum, the rim shot its tek, the high conga its ka, the tambourine the riq.

def two(s):                            # a one-bar pattern, played twice (the groove is two bars)
    return s + s


GROOVES = {
    # maqsum 4/4 (D T . T D . T .): dum on 1 and 3, teks between, a soft riq in eighths. Tarab: Cairo orchestras, 1950s
    "ARAB_TARAB": dict(kit="STD", kick="ROUND", tune=58, tone=56, decay=62, snap=50, fill=0, lanes=[
        ("KICK", 92, two("X.......x.......")),
        ("RIM", 78, two("..x...x.....x...")),
        ("CONGA_HI", 54, two("....g.....g.g...")),
        ("TAMB", 50, two("x.x.x.x.x.x.x.x.")),
    ]),
    # baladi 4/4 (D D . T D . T .): two dums to start, the folk beat of Cairo's streets
    "ARAB_BALADI": dict(kit="STD", kick="ROUND", tune=56, tone=54, decay=60, snap=60, lanes=[
        ("KICK", 100, two("X.x.....x.......")),
        ("RIM", 90, two("......x.....x...")),
        ("CONGA_HI", 58, two("....g..g..g.g...")),
        ("TAMB", 56, two("x.x.x.x.x.x.x.x.")),
        ("CLAP", 64, two("....x.......x...")),
    ]),
    # malfuf 2/4 (D . . T . . T .): a fast roll in eighths, belly-dance and cabaret
    "ARAB_MALFUF": dict(kit="STD", kick="ROUND", tune=60, tone=58, decay=54, snap=70, len=16, lanes=[
        ("KICK", 100, "X.......x......."),
        ("RIM", 92, "...x..x....x..x."),
        ("CONGA_HI", 56, ".g.g.g.g.g.g.g.g"),
        ("TAMB", 62, "x.x.x.x.x.x.x.x."),
    ]),
    # saidi (D T . D D . T .): Upper Egypt, the heavy stick beat of the tabla baladi
    "ARAB_SAIDI": dict(kit="STD", kick="ROUND", tune=52, tone=52, decay=64, snap=74, lanes=[
        ("KICK", 106, two("X.....x.x.......")),
        ("RIM", 94, two("..x.......x.....")),
        ("FLOOR_TOM", 70, two("..........g.g...")),
        ("TAMB", 56, two("x.x.x.x.x.x.x.x.")),
    ]),
    # shaabi: the maqsum louder, with handclaps on 2 and 4 and a street-party shaker
    "ARAB_SHAABI": dict(kit="STD", kick="PUNCH", tune=60, tone=60, decay=56, snap=84, lanes=[
        ("KICK", 108, two("X.......x.x.....")),
        ("RIM", 92, two("..x...x.....x...")),
        ("CLAP", 86, two("....x.......x...")),
        ("SHAKER", 58, two("xxxxxxxxxxxxxxxx")),
    ]),
    # chaabi of Morocco in 6/8 (twelve ticks a bar, eighths): dum, teks, a rolling groove
    "ARAB_CHAABI68": dict(kit="STD", kick="ROUND", tune=58, tone=56, decay=58, snap=62, len=24, lanes=[
        ("KICK", 100, "X.....x.....X.....x....."),
        ("RIM", 90, "..x.x.....x...x.x.....x."),
        ("CONGA_HI", 56, ".....g.g.....g...g.g...."),
        ("TAMB", 54, "x.xx.xx.xx.xx.xx.xx.xx.x"),
    ]),
    # chaabi of Algiers, 4/4: the dum on the one and the "and" of two, teks, the riq
    "ARAB_CHAABIDZ": dict(kit="STD", kick="ROUND", tune=56, tone=54, decay=60, snap=56, lanes=[
        ("KICK", 98, two("X.....x.x.......")),
        ("RIM", 88, two("..x.........x...")),
        ("CONGA_HI", 54, two(".g..g..g..g..g..")),
        ("TAMB", 52, two("x.x.x.x.x.x.x.x.")),
    ]),
    # rai: the drum machine's darbuka, dum-dum-tek, with the snare on the offbeat and a closed hat
    "ARAB_RAI": dict(kit="80", tune=60, decay=54, snap=84, lanes=[
        ("KICK", 106, two("X..x..x..x......")),
        ("RIM", 92, two("......x.....x.x.")),
        ("CLAP", 70, two("....x.......x...")),
        ("HAT", 56, two("x.x.x.x.x.x.x.x.")),
        ("CONGA_HI", 52, two("..g..g..g..g..g.")),
    ]),
    # pop-rai of the 1990s: the same beat, rounder and cleaner, a shaker on sixteenths
    "ARAB_RAIPOP": dict(kit="STD", kick="PUNCH", tune=62, tone=60, decay=52, snap=82, lanes=[
        ("KICK", 104, two("X..x..x..x......")),
        ("SNARE", 88, two("....x.......x...")),
        ("RIM", 80, two("......x.....x.x.")),
        ("SHAKER", 54, two("xxxxxxxxxxxxxxxx")),
        ("CONGA_HI", 50, two("..g..g..g..g..g.")),
    ]),
    # mezwed of Tunisia: dum, tek, a ka, then a long answer; a bendir's low thud and the riq running
    "ARAB_MEZWED": dict(kit="STD", kick="ROUND", tune=58, tone=58, decay=56, snap=72, lanes=[
        ("KICK", 104, two("X.....x.x.......")),
        ("RIM", 94, two("..x.x.......x.x.")),
        ("TOM_LO", 70, two("x.......x.......")),
        ("CONGA_HI", 58, two("...g...g...g...g")),
        ("TAMB", 62, two("x.x.x.x.x.x.x.x.")),
    ]),
    # Arab pop (Egyptian, 1990s): a clean maqsum on a drum machine, claps, a hat
    "ARAB_POP": dict(kit="STD", kick="PUNCH", tune=62, tone=60, decay=50, snap=86, lanes=[
        ("KICK", 106, two("X.......x.......")),
        ("RIM", 86, two("..x...x.....x...")),
        ("CLAP", 74, two("....x.......x...")),
        ("HAT", 58, two("x.x.x.x.x.x.x.x.")),
    ]),
    # dabke 4/4: a stamping, driving beat, the dum on every beat, teks between, claps; for the dancing line
    "ARAB_DABKE": dict(kit="STD", kick="ROUND", tune=60, tone=58, decay=52, snap=84, lanes=[
        ("KICK", 108, two("X...x...X...x...")),
        ("RIM", 92, two("..x...x...x...x.")),
        ("CLAP", 84, two("....x.......x...")),
        ("TAMB", 62, two("x.x.x.x.x.x.x.x.")),
    ]),
    # khaliji 2/4 (D . . D . . T .): the Gulf's light, bouncing beat, claps on the offbeats
    "ARAB_KHALIJI": dict(kit="STD", kick="ROUND", tune=58, tone=56, decay=56, snap=68, len=16, lanes=[
        ("KICK", 98, "X..x....X..x...."),
        ("RIM", 86, "......x.......x."),
        ("CLAP", 66, "..x.....x..x...."),
        ("TAMB", 56, "x.x.x.x.x.x.x.x."),
    ]),
}

GENRES = [
    dict(id="AR_TARAB", name="TARAB CAIRE", decade=1950, year=1953,
         comment="Cairo's orchestras of the tarab (Umm Kulthum, Abdel Halim, Farid el Atrache's films): nahawand "
                 "(harmonic minor) under strings, oud and accordion; slow, rubato, a swelling line, the maqsum underneath",
         key="D", scale="HARM_MINOR", bpm=88, div=4, chord_beats=4, period_bars=8, rubato=0.35, swell=0.4,
         vocab="CLASSIC", harmony="CYCLE", cycle=["i", "iv", "V", "i", "VI", "iv", "V7", "i"],
         melody=dict(density=0.5, base=62, range=15, profile=(0.15, 0.6, 0.85, 0.95), max_leap=4, sync=0.2,
                     motif=0.75, turn=0.15, appoggiatura=0.2),
         bass=dict(mode="ROOT", rhythm="x.......x.....x."),
         pad=dict(mode="BLOCK", base=53, tones=4),
         groove="ARAB_TARAB", orch_mode="CONTRAST",
         orch=[("CELLO", "VIOLIN", "STRINGS"), ("UPRIGHT", "OUD", "STRINGS"), ("CELLO", "ACCORDION", "HARP"),
               ("CONTRABASS", "VIOLIN", "OUD")]),
    dict(id="AR_ATRACHE", name="EL ATRACHE", decade=1950, year=1955,
         comment="In the manner of Farid el Atrache: the oud's long phrases and a descending line over a minor "
                 "loop (bayati, played as aeolian), the Andalusian fall i-VII-VI-V, then iv and back, strings and harp",
         key="D", scale="AEOLIAN", bpm=96, div=4, chord_beats=4, period_bars=8, rubato=0.25, swell=0.3,
         vocab="CLASSIC", harmony="CYCLE", cycle=["i", "VII", "VI", "V7", "i", "iv", "V", "i"],
         melody=dict(density=0.55, base=60, range=17, profile=(0.15, 0.62, 0.85, 0.95), max_leap=5, sync=0.25,
                     motif=0.7, turn=0.2, appoggiatura=0.25, direction=-0.1),
         bass=dict(mode="ROOT", rhythm="x.....x.x......."),
         pad=dict(mode="BROKEN", base=55, tones=3),
         groove="ARAB_TARAB", orch_mode="CYCLE",
         orch=[("CELLO", "OUD", "STRINGS"), ("UPRIGHT", "VIOLIN", "HARP"), ("CELLO", "OUD", "ACCORDION")]),
    dict(id="AR_BALADI", name="BALADI", decade=1960, year=1960,
         comment="Egyptian baladi: the folk beat of the street, an accordion line over a drone-like loop, i and "
                 "bVII answering each other",
         key="D", scale="DORIAN", bpm=104, div=4, chord_beats=4, period_bars=8, repeat=0.6,
         vocab="MODAL", harmony="CYCLE", cycle=["i", "i", "bVII", "i"],
         melody=dict(density=0.6, base=62, range=14, profile=(0.15, 0.65, 0.86, 0.95), max_leap=3, sync=0.3,
                     motif=0.85, motif_use=0.8, turn=0.2),
         bass=dict(mode="ROOT", rhythm="x.x.....x......."),
         pad=dict(mode="RHYTHM", rhythm="..x.....x..x....x.....x..x......", gate=1, base=55, tones=3),
         groove="ARAB_BALADI", orch_mode="CONTRAST",
         orch=[("UPRIGHT", "ACCORDION", "ORGAN"), ("EBASS", "ACCORDION", "OUD"), ("UPRIGHT", "OBOE", "ACCORDION")]),
    dict(id="AR_MALFUF", name="MALFUF", decade=1960, year=1965,
         comment="Malfuf in 2/4, the fast cabaret and belly-dance beat: hijaz (phrygian dominant), the minor second "
                 "answered by the tonic, a quick line of eighths with an oud and an accordion",
         key="D", scale="PHRYG_DOM", bpm=132, div=4, beats=2, chord_beats=2, period_bars=8, repeat=0.5,
         vocab="CLASSIC", harmony="CYCLE", cycle=["I", "bII", "I", "V"],
         melody=dict(density=0.7, base=62, range=14, profile=(0.15, 0.65, 0.85, 0.95), max_leap=3, sync=0.2,
                     motif=0.8, motif_beats=2, turn=0.25),
         bass=dict(mode="ROOT", rhythm="x...x..."),
         pad=dict(mode="AFTERBEAT", base=55, tones=3),
         groove="ARAB_MALFUF", orch_mode="CONTRAST",
         orch=[("UPRIGHT", "OUD", "ACCORDION"), ("EBASS", "VIOLIN", "ORGAN"), ("UPRIGHT", "ACCORDION", "STRINGS")]),
    dict(id="AR_SAIDI", name="SAIDI", decade=1960, year=1962,
         comment="Saidi, Upper Egypt: the stick dance and a reed (mizmar) line over a dorian i-IV, hard and repeating",
         key="D", scale="DORIAN", bpm=112, div=4, chord_beats=4, period_bars=8, repeat=0.7,
         vocab="POP", harmony="CYCLE", cycle=["i", "i", "IV", "i"],
         melody=dict(density=0.6, base=62, range=12, profile=(0.2, 0.7, 0.9, 0.97), max_leap=3, sync=0.25,
                     motif=0.9, motif_use=0.85, turn=0.3),
         bass=dict(mode="ROOT", rhythm="x.....x.x......."),
         pad=dict(mode="BLOCK", base=53, tones=3),
         groove="ARAB_SAIDI", orch_mode="CONTRAST",
         orch=[("UPRIGHT", "ENGLISHHORN", "ACCORDION"), ("EBASS", "OBOE", "ORGAN"), ("CONTRABASS", "OBOE", "OUD")]),
    dict(id="AR_SHAABI", name="SHAABI", decade=1970, year=1972,
         comment="Shaabi, Cairo's street pop (Ahmed Adaweyya, Hakim, Sha'ban): organ and synth over a hard maqsum, "
                 "handclaps, a harmonic-minor i-iv-V loop",
         key="E", scale="HARM_MINOR", bpm=118, div=4, chord_beats=4, period_bars=8, repeat=0.5,
         vocab="CLASSIC", harmony="CYCLE", cycle=["i", "iv", "V", "i"],
         melody=dict(density=0.65, base=64, range=13, profile=(0.15, 0.62, 0.84, 0.95), max_leap=3, sync=0.3,
                     motif=0.85, turn=0.25),
         bass=dict(mode="ROOT", rhythm="x...x.x.x...x.x."),
         pad=dict(mode="AFTERBEAT", base=55, tones=3),
         groove="ARAB_SHAABI", orch_mode="CONTRAST",
         orch=[("EBASS", "ROCKORGAN", "ACCORDION"), ("SYNTHBASS", "SYNCLEAD", "ORGAN"), ("EBASS", "ACCORDION", "STRMACH")]),
    dict(id="AR_CHAABI_MA", name="CHAABI MAROC", decade=1970, year=1974,
         comment="Moroccan chaabi (Nass el Ghiwane, Najat Aatabou, the Andalusian-Gnawa street) in 6/8: banjo and "
                 "oud over the Andalusian fall Am-G-F-E",
         key="A", scale="AEOLIAN", bpm=116, div=2, beats=6, chord_beats=6, period_bars=8, repeat=0.6,
         vocab="POP", harmony="CYCLE", cycle=["i", "VII", "VI", "V"],
         melody=dict(density=0.6, base=60, range=13, profile=(0.2, 0.68, 0.88, 0.96), max_leap=3, sync=0.2,
                     motif=0.85, motif_beats=3, turn=0.25),
         bass=dict(mode="ROOT", rhythm="x.....x....."),
         pad=dict(mode="TREMOLO", base=57, tones=3),
         groove="ARAB_CHAABI68", orch_mode="CONTRAST",
         orch=[("UPRIGHT", "BANJO", "OUD"), ("EBASS", "OUD", "ACCORDION"), ("UPRIGHT", "VIOLIN", "BANJO")]),
    dict(id="AR_CHAABI_DZ", name="CHAABI ALGER", decade=1970, year=1966,
         comment="Algiers chaabi (El Anka, Dahmane El Harrachi): mandole tremolo and violin, the loop i-iv-V and "
                 "VII-VI-V, a patient 4/4",
         key="A", scale="HARM_MINOR", bpm=100, div=4, chord_beats=4, period_bars=8, repeat=0.55, rubato=0.15,
         vocab="CLASSIC", harmony="CYCLE", cycle=["i", "iv", "V", "i", "VII", "VI", "V7", "i"],
         melody=dict(density=0.55, base=60, range=15, profile=(0.15, 0.62, 0.85, 0.95), max_leap=4, sync=0.2,
                     motif=0.75, turn=0.2, appoggiatura=0.2),
         bass=dict(mode="ROOT", rhythm="x.....x.x......."),
         pad=dict(mode="TREMOLO", base=57, tones=3),
         groove="ARAB_CHAABIDZ", orch_mode="CONTRAST",
         orch=[("UPRIGHT", "VIOLIN", "BANJO"), ("CELLO", "OUD", "ACCORDION"), ("UPRIGHT", "VIOLIN", "OUD")]),
    dict(id="AR_RAI", name="RAI", decade=1980, year=1982,
         comment="Rai of Oran (Cheb Khaled, Cheb Mami's start, Chaba Fadela): drum machine and synth, an accordion "
                 "and a trumpet, a minor drone loop i-VII-VI-VII on the phrygian scale (kurd's colour)",
         key="A", scale="PHRYGIAN", bpm=108, div=4, chord_beats=4, period_bars=8, repeat=0.7, open=0.15,
         vocab="POP", harmony="CYCLE", cycle=["i", "VII", "VI", "VII"],
         melody=dict(density=0.65, base=62, range=13, profile=(0.15, 0.65, 0.86, 0.95), max_leap=3, sync=0.35,
                     motif=0.9, motif_use=0.85, turn=0.3),
         bass=dict(mode="ROOT", rhythm="x..x..x..x......"),
         pad=dict(mode="AFTERBEAT", base=55, tones=3),
         groove="ARAB_RAI", orch_mode="CONTRAST",
         orch=[("SYNTHBASS", "ACCORDION", "SYNTH"), ("EBASS", "TRUMPET", "STRMACH"), ("SYNTHBASS", "OUD", "ACCORDION")]),
    dict(id="AR_RAI_POP", name="RAI POP", decade=1990, year=1992,
         comment="Pop-rai of the 1990s (Khaled, Faudel, Cheb Mami): a clean beat, guitar and strings, the pop minor "
                 "loop i-VI-III-VII under a sung line",
         key="A", scale="AEOLIAN", bpm=112, div=4, chord_beats=4, period_bars=8, repeat=0.6,
         vocab="POP", harmony="CYCLE", cycle=["i", "VI", "III", "VII"],
         melody=dict(density=0.6, base=64, range=13, profile=(0.15, 0.62, 0.86, 0.95), max_leap=4, sync=0.3,
                     motif=0.85, turn=0.2),
         bass=dict(mode="ROOT", rhythm="x..x..x..x......"),
         pad=dict(mode="ARPEGGIO", base=55, tones=3),
         groove="ARAB_RAIPOP", orch_mode="CONTRAST",
         orch=[("EBASS", "ACCORDION", "STRINGS"), ("SLAPBASS", "OUD", "EPIANO"), ("EBASS", "VOICE", "GUITAR")]),
    dict(id="AR_MEZWED", name="MEZWED", decade=1990, year=1990,
         comment="Tunisian mezwed: the bagpipe's loud reed line over a drone, a fast darbuka and bendir, hijaz "
                 "(phrygian dominant) on a pedal with the minor second as a push",
         key="E", scale="PHRYG_DOM", bpm=116, div=4, chord_beats=4, period_bars=8, repeat=0.8, open=0.1,
         vocab="CLASSIC", harmony="CYCLE", cycle=["I", "I", "bII", "I"],
         melody=dict(density=0.75, base=64, range=12, profile=(0.2, 0.72, 0.9, 0.97), max_leap=3, sync=0.3,
                     motif=0.9, motif_use=0.9, turn=0.35),
         bass=dict(mode="PEDAL", rhythm="x...x...x...x..."),
         pad=dict(mode="BLOCK", base=52, tones=2, power=True),
         groove="ARAB_MEZWED", orch_mode="CONTRAST",
         orch=[("EBASS", "ENGLISHHORN", "ACCORDION"), ("UPRIGHT", "OBOE", "DRONE"), ("EBASS", "ENGLISHHORN", "ORGAN")]),
    dict(id="AR_POP", name="POP ARABE", decade=1990, year=1996,
         comment="Egyptian and Lebanese pop (Amr Diab, Nancy Ajram, Cheb Khaled's crossovers): nahawand under guitar "
                 "and synth, the loop i-iv-VII-III, a bright clean maqsum",
         key="D", scale="HARM_MINOR", bpm=104, div=4, chord_beats=4, period_bars=8, repeat=0.55,
         vocab="POP", harmony="CYCLE", cycle=["i", "iv", "VII", "III"],
         melody=dict(density=0.6, base=64, range=13, profile=(0.15, 0.62, 0.86, 0.95), max_leap=4, sync=0.3,
                     motif=0.8, turn=0.2),
         bass=dict(mode="ROOT", rhythm="x.....x.x.....x."),
         pad=dict(mode="ARPEGGIO", base=57, tones=3),
         groove="ARAB_POP", orch_mode="CONTRAST",
         orch=[("EBASS", "EGUITAR", "STRMACH"), ("SYNTHBASS", "OUD", "EPIANO"), ("EBASS", "ACCORDION", "STRINGS")]),
    dict(id="AR_DABKE", name="DABKE", decade=2000, year=2000,
         comment="Dabke of the Levant (Lebanon, Syria, Palestine): a stamping beat for the line dance, a mijwiz-like "
                 "reed and an accordion over i-V in harmonic minor",
         key="D", scale="HARM_MINOR", bpm=128, div=4, chord_beats=4, period_bars=8, repeat=0.7,
         vocab="CLASSIC", harmony="CYCLE", cycle=["i", "i", "V", "i"],
         melody=dict(density=0.75, base=64, range=12, profile=(0.2, 0.7, 0.9, 0.97), max_leap=3, sync=0.25,
                     motif=0.9, motif_use=0.9, turn=0.35),
         bass=dict(mode="ROOT", rhythm="x...x...x...x..."),
         pad=dict(mode="AFTERBEAT", base=55, tones=3),
         groove="ARAB_DABKE", orch_mode="CONTRAST",
         orch=[("EBASS", "OBOE", "ACCORDION"), ("SYNTHBASS", "CLARINET", "ORGAN"), ("EBASS", "OUD", "STRMACH")]),
    dict(id="AR_KHALIJI", name="KHALIJI", decade=2000, year=2002,
         comment="Khaliji, the Gulf's pop (Kuwait, Emirates, Saudi): a light 2/4, oud and strings over a mixolydian "
                 "I-bVII-I-IV (rast, as the 12-tone scale has it)",
         key="C", scale="MIXOLYDIAN", bpm=104, div=4, beats=2, chord_beats=2, period_bars=8, repeat=0.55,
         vocab="MODAL", harmony="CYCLE", cycle=["I", "bVII", "I", "IV"],
         melody=dict(density=0.6, base=64, range=13, profile=(0.15, 0.62, 0.86, 0.95), max_leap=4, sync=0.25,
                     motif=0.8, motif_beats=2, turn=0.2),
         bass=dict(mode="ROOT", rhythm="x..x...."),
         pad=dict(mode="BLOCK", base=55, tones=3),
         groove="ARAB_KHALIJI", orch_mode="CONTRAST",
         orch=[("EBASS", "OUD", "STRINGS"), ("SYNTHBASS", "OUD", "STRMACH"), ("UPRIGHT", "VIOLIN", "OUD")]),
]
