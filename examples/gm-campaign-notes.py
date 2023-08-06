"""This file describes game-manager notes.

It's used for creating notes for the GM to keep track of various
monsters, etc.

"""

<<<<<<< HEAD
from dungeonsheets import mechanics, monsters
=======
from dungeonsheets import mechanics, monsters as _monsters
>>>>>>> origin/master

dungeonsheets_version = "0.14.0"

sheet_type = "gm"

session_title = "Objects in Space"

# Simple character definition
haryk_omanie = mechanics.Character(
    name="Haryk Omanie",
)

<<<<<<< HEAD
party = ["rogue1.py", "paladin2.py", haryk_omanie, monsters.Veteran]
=======
party = ["rogue1.py", "paladin2.py", haryk_omanie, _monsters.Veteran]
>>>>>>> origin/master

random_tables = ["conjure animals"]
