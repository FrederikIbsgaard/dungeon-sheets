"""This file describes the heroic adventurer Jörmun Ragnar.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.12.0"

name = "Jörmun Ragnar"
player_name = "Frederik"

# Be sure to list Primary class first
classes = ['Sorceror']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [11]  # ex: [10] or [3, 2]
subclasses = ["Draconic Bloodline"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Acolyte"
race = "Half-Orc"
alignment = "Neutral good"

xp = 0
hp_max = 66
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 11
dexterity = 16
constitution = 12
intelligence = 12
wisdom = 11
charisma = 18

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'persuasion', 'insight', 'religion', 'intimidation')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('Empowered Spell', 'Subtle Spell', 'Transmuted Spell')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Deep Speech, Under Common, Common, Orc"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ['Quarterstaff', "Dagger", "Dart"]  # Example: ('shortsword', 'longsword')
magic_items = ('Pearl of Power', 
                'Scrying Eye',
                'Ragnars Staff of Acid',)  # Example: ('ring of protection',)
armor = "None"  # Eg "leather armor"
shield = "None"  # Eg "shield"

equipment = """Handy Haversack"""

attacks_and_spellcasting = """Ragnars Staff of Acid """

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ( 'Acid Splash',
                    'Dancing Lights',
                    'Mage Hand',
                    'Mending',
                    'Message',
                    'Minor Illusion',
                    'Prestidigitation',
                    'Chromatic Orb',
                    'Detect Magic',
                    'Ice Knife',
                    'Magic Missile',
                    'Detect Thoughts',
                    'Misty Step',
                    'Scorching Ray',
                    'Counterspell',
                    'Dimension Door',
                    'Vitriolic Sphere', 
                    'Dominate Person',
                    'Globe of Invulnerability')  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Infusions for Artificer
infusions = () # Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """TODO"""

ideals = """TODO"""

bonds = """TODO"""

flaws = """TODO"""

features_and_traits = """TODO:"""
