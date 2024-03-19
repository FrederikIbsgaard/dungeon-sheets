"""This file describes the heroic adventurer Thalric.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""
# To add your own content, write a .py file with your definitions.
# Then, import here using the 'import_homebrew' function.
from dungeonsheets import import_homebrew
# from dungeonsheets.equipment_reader import explorers_pack
kits = import_homebrew("kits.py")

dungeonsheets_version = "0.18.0"

name = "Thalric \"Thal\" Shadeweaver"
player_name = "Frederik"

# Be sure to list Primary class first
classes = ['Artificer', 'Wizard']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1, 3]  # ex: [10] or [3, 2]
subclasses = ['', 'School of Divination']  # 'School of Divination' ex: ['Necromacy'] or ['Thief', None]
background = "Sage"
race = "Silver Tiefling"
alignment = "Neutral good"

xp = 0
hp_max = 22
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 11
dexterity = 12
constitution = 15
intelligence = 18
wisdom = 12
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'history', 'investigation', 'nature')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ('quarterstaff')  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ("cook's utensils", "thieves' tools", "tinkers' tools" )  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Dwarvish, Gnomish, Common, Infernal"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = []  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "None"  # Eg "leather armor"
shield = "None"  # Eg "shield"

equipment = kits.explorers_pack.format(rations=10, torches=10, 
                                       pitons=10, rope=50) + \
                                        ", spell book, cook's utensils" 

attacks_and_spellcasting = """ """

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
#spells_prepared = ('Ray Of Frost', 'Guidance',  'Mending', 'Mage Hand', 'Shocking Grasp')  # Todo: Learn some spells
spells_prepared = ('Ray Of Frost', 'Guidance',  'Mending', 'Mage Hand', 'Shocking Grasp', 'Thaumaturgy')  # Todo: Learn some spells

# Which spells have not been prepared
#__spells_unprepared = ()
__spells_unprepared = ('Glacial Rebuke', 
                "absorb elements",
                "alarm",
                "catapult",
                "cure wounds",
                "detect magic",
                "disguise self",
                "expeditious retreat",
                "faerie fire",
                "false life",
                "feather fall",
                "grease",
                "identify",
                "jump",
                "longstrider",
                "purify food and drink",
                "sanctuary", 
                "snare",
                'Tashas Caustic Brew')

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Infusions for Artificer
infusions = ('Bag of Holding', 'Alchemy Jug', 'Cap of Water Breathing', 'Sending Stones') # Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """ """

ideals = """ """

bonds = """ """

flaws = """ """

features_and_traits = """ """


# Appearance
portrait = True
age = 28
height = ""
weight = ""
eyes = "Silver"
skin = "Gray"
hair = "Silver"
