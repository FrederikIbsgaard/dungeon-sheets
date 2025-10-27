from dungeonsheets.content_registry import default_content_registry


default_content_registry.add_module(__name__)


class Infusion:
    name = "Unknown infusion"
    item = "Item to be infused"
    prerequisite = ""
    classes = ("Artificer",)

    def __str__(self):
        indicator = ("$", self.special_material)
        if indicator:
            return self.name + f' ({"".join(indicator)})'
        else:
            return self.name

    def __repr__(self):
        return '"{:s}"'.format(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return 0

    @property
    def special_material(self):
        return "worth at least" in self.item.lower()


class BootsOfTheWindingPath(Infusion):
    """While wearing these boots, a creature can teleport up to 15 feet as a
    bonus action to an unoccupied space the creature can see. The creature
    must have occupied that space at some point during the current turn.
    """

    name = "Boots of the Winding Path"
    item = "A pair of boots (requires attunement"
    prerequisite = "6th-level artificer"


class EnhancedArcaneFocus(Infusion):
    """While holding this item, a creature gains a + 1 bonus to spell attack
    rolls. In addition, the creature ignores half cover when making a spell
    attack.

    The bonus increases to +2 when you reach 10th level in this class.
    """

    name = "Enhanced Arcane Focus"
    item = "A rod, staff, or wand (requires attunement)"


class EnhancedDefense(Infusion):
    """A creature gains a + 1 bonus to Armor Class while wearing (armor) or
    wielding (shield) the infused item.

    The bonus increases to +2 when you reach 10th level in this class.
    """

    name = "Enhanced Defense"
    item = "A suit of armor or shield"


class EnhancedWeapon(Infusion):
    """This magic weapon grants a +1 bonus to attack and damage rolls made with
    it.

    The bonus increases to +2 when you reach 10th level in this class.
    """

    name = "Enhanced Weapon"
    item = "A simple or martial weapon"


class HomunculusServant(Infusion):
    """You learn intricate methods for magically creating a special homunculus
    that serves you. The item you infuse serves as the creature's heart, around
    which the creature's body instantly forms.

    You determine the homunculus's appearance. Some artificers prefer
    mechanical-looking birds, whereas some like winged vials or miniature,
    animate cauldrons.

    The homunculus is friendly to you and your companions, and it obeys your
    commands. See this creature's game statistics in the Homunculus Servant
    stat block.

    In combat, the homunculus shares your initiative count, but it takes its
    turn immediately after yours. It can move and use its reaction on its own,
    but the only action it takes on its turn is the Dodge action, unless you
    take a bonus action on your turn to command it to take the action in its
    stat block or the Dash, Disengage, Help, Hide, or Search action.

    The homunculus regains 2d6 hit points if the *mending* spell is cast on it.
    If it dies, it vanishes, leaving its heart in its space.
    """

    name = "Homunculus Servant"
    item = "A gem worth at least 100gp or a dragonshard"


class RadiantWeapon(Infusion):
    """This magic weapon grants a + 1 bonus to attack and damage rolls made
    with it. While holding it, the wielder can take a bonus action to cause it
    to shed bright light in a 30-foot radius and dim light for an additional 30
    feet. The wielder can extinguish the light as a bonus action.

    The weapon has 4 charges. As a reaction immediately after being hit by an
    attack, the wielder can expend 1 charge and cause the attacker to be
    blinded until the end of the attacker's next turn, unless the attacker
    succeeds on a Constitution saving throw against your spell save DC. The
    weapon regains 1d4 expended charges daily at dawn.
    """

    name = "Radiant Weapon"
    item = "A simple or martial weapon (requires attunement)"
    prerequisite = "6th-level artificer"


class RepeatingShot(Infusion):
    """This magic weapon grants a + 1 bonus to attack and damage rolls made
    with it when it's used to make a ranged attack, and it ignores the loading
    property if it has it.

    If you load no ammunition in the weapon, it produces its own, automatically
    creating one piece of magic am­munition when you make a ranged attack with
    it. The ammunition created by the weapon vanishes the instant after it hits
    or misses a target.
    """

    name = "Repeating Shot"
    item = """A simple or martial weapon with the ammunition property (requires
              attunement)"""


class ReplicateMagicItem(Infusion):
    """Using this infusion, you replicate a particular magic item. You can
    learn this infusion multiple times; each time you do so, choose a magic
    item that you can make with it, picking from the Replicable Items tables
    below. A table's title tells you the level you must be in the class to
    choose an item from the table.

    In the tables, an item's entry tells you whether the item requires
    attunement. See the item's description in the *Dungeon Master's Guide* for
    more information about it, including the type of object required for its
    making. If you have *Xanathar's Guide to Everything*, you can choose from
    among the common magic items in that book when you pick a magic item you
    can replicate with this infusion.
    """

    name = "Replicate Magic Item"

class BagOfHolding(Infusion):
    """This bag has an interior space considerably larger than its outside dimensions, 
    roughly 2 feet in diameter at the mouth and 4 feet deep. The bag can hold up to 500 pounds, 
    not exceeding a volume of 64 cubic feet. The bag weighs 15 pounds, regardless of its contents. 
    Retrieving an item from the bag requires an action.
    
    If the bag is overloaded, pierced, or torn, it ruptures and is destroyed, and its contents are scattered in the Astral Plane. 
    If the bag is turned inside out, its contents spill forth, unharmed, but the bag must be put right before it can be used again. 
    Breathing creatures inside the bag can survive up to a number of minutes equal to 10 divided by the number of creatures (minimum 1 minute), 
    after which time they begin to suffocate.
    
    Placing a bag of holding inside an extradimensional space created by a handy haversack, portable hole, 
    or similar item instantly destroys both items and opens a gate to the Astral Plane. The gate originates where the one item was placed inside the other. 
    Any creature within 10 feet of the gate is sucked through it to a random location on the Astral Plane. The gate then closes. 
    The gate is one-way only and cant be reopened.
    """

    name = "Bag of Holding"

class AlchemyJug(Infusion):
    """This ceramic jug appears to be able to hold a gallon of liquid and weighs 12 pounds whether full or empty. 
    Sloshing sounds can be heard from within the jug when it is shaken, even if the jug is empty.
    You can use an action and name one liquid from the table below to cause the jug to produce the chosen liquid. 
    Afterward, you can uncork the jug as an action and pour that liquid out, up to 2 gallons per minute. 
    The maximum amount of liquid the jug can produce depends on the liquid you named.
    Once the jug starts producing a liquid, it can't produce a different one, or more of one that has reached its maximum, until the next dawn.
    

    Liquid Max Amount:

    - Acid 236 ml
    - Basic poison 15 ml
    - Beer 15 liter
    - Honey 3.8 liter
    - Mayonnaise 7.5 liter
    - Oil 1 liter
    - Vinegar 7.5 liter
    - Water, fresh 30 liter
    - Water, salt 45 liter
    - Wine 3.8 liter
    """

    name = "Alchemy Jug"

class SendingStones(Infusion):
    """Sending stones come in pairs, with each smooth stone carved to match the other so the pairing is easily recognized.
    While you touch one stone, you can use an action to cast the sending spell from it. 
    The target is the bearer of the other stone. 
    If no creature bears the other stone, you know that fact as soon as you use the stone and don't cast the spell.

    Once sending is cast through the stones, they can't be used again until the next dawn. 
    If one of the stones in a pair is destroyed, the other one becomes nonmagical.
    """

    name = "Sending Stones"

class CapOfWaterBreathing(Infusion):
    """While wearing this cap underwater, you can speak its command word as an action to create a bubble of air around your head. 
    It allows you to breathe normally underwater. 
    This bubble stays with you until you speak the command word again, the cap is removed, or you are no longer underwater.
    """

    name = "Cap of Water Breathing"


class RepulsionShield(Infusion):
    """A creature gains a + 1 bonus to Armor Class while wield­ing this shield.

    The shield has 4 charges. While holding it, the wielder can use a reaction
    immediately after being hit by a melee attack to expend 1 of the shield's
    charges and push the attacker up to 15 feet away. The shield regains 1d4
    expended charges daily at dawn.
    """

    name = "Repulsion Shield"
    item = "A shield (requires attunement)"


class ResistantArmor(Infusion):
    """While wearing this armor, a creature has resistance to one of the
    following damage types, which you choose when you infuse the item: acid,
    cold, fire, force, light­ning, necrotic, poison, psychic, radiant, or
    thunder.
    """

    name = "Resistant Armor"
    item = "A suit of armor (requires attunement)"


class ReturningWeapon(Infusion):
    """This magic weapon grants a + 1 bonus to attack and damage rolls made
    with it, and it returns to the wielder's hand immediately after it is used
    to make a ranged attack.
    """

    name = "Returning Weapon"
    item = "A simple or martial weapon with the thrown property"
