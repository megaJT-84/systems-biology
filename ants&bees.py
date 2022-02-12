class ants:
    kind  = 'ant'
    def __init__(self, species_name, hive_name):
        self.species = species_name
        self.hive = hive_name

class bees:
    kind = 'bee'
    def __init__(self, species_name, hive_name):
        self.species = species_name
        self.hive = hive_name

ant1 = ants('large worker', "anty's little hive 1")
ant2 = ants('smal worker', "colony 117")
ant3 = ants('soldier', "warrior's den")
ant_q = ants('queen', "queen ant's royal palace")

bee1 = bees('worker', "bee No.1's sweet home")
bee2 = bees('laying worker', "place for laying stuff")
bee3 = bees('drone', "I'm just a drone, have no home to go")
bee_q = bees('queen', "queen's jackpot where all the nectar is")

ant_bee = input("please enter the ant's or bee's name\n")

def ant_bee_info(i):
    switcher = {
        "ant 1":"ant 1 is " + ant1.species + ", it lives in hive " + "'" + ant1.hive + "'",
        "ant 2":"ant 2 is " + ant2.species  + ", it lives in hive " + "'"+ ant2.hive + "'",
        "ant 3":"ant 3 is " + ant3.species + ", it lives in hive " + "'" + ant3.hive + "'",
        "ant queen":"ant queen is " + ant_q.species + ", it lives in hive " + "'" + ant_q.hive + "'",
        "bee 1":"bee 1 is " + bee1.species + ", it comes from hive " + "'" + bee1.hive + "'",
        "bee 2":"bee 2 is " + bee2.species + ", it comes from hive " + "'" + bee2.hive + "'",
        "bee 3":"bee 3 is " + bee3.species + ", it comes from hive " + "'" + bee3.hive + "'",
        "bee queen":"bee queen is " + bee_q.species + ", it comes from hive " + "'" + bee_q.hive + "'"
    }
    return switcher.get(i, "invalid ant or bee input")

print(ant_bee_info(ant_bee))