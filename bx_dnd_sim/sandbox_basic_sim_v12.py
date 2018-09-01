import csv
import random

class Character(object):
	"""
	An object that describes a series of characters from a dictionary
	"""
	def __init__(self, dictionary):
		"""
		Constructor for the Character object
		"""
		for k, v in dictionary.items():
			setattr(self, k, v)


	def __str__(self):
		stats = self.NAME + "\t" + self.TYPE + "\t" + self.CLASS + "\t" + str(self.HP) + "\t" + str(self.AC)
		return stats

	def isAlive(self):
		if self.HP>0:
			return 1

class Monster(object):
	def __init__(self, dictionary):
		for k, v in dictionary.items():
			setattr(self, k, v)

	def __str__(self):
		#print "NAME" + "\t" + "TYPE" + "\t" + "HP" + "\t" + "AC" + "\t" + "MORALE"
		stats = self.NAME + "\t" + self.TYPE + "\t" + str(self.HP) + "\t" + str(self.AC) + "\t" + str(self.MORALE)
		return stats

	def isAlive(self):
		if self.HP > 0:
			return 1

class Dice(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self, number):
    	return [random.randint(1,self.sides) for _ in range(number)]

    def roll_one(self):
        return random.randint(1, self.sides)

def main():

	# The lists here are for printing out to the screen some basic info about the 
	# the PCs and NPCs. I think we can populate the Fight class directly with the
	# instances. 

	char_instances = []
	

	#This reads in the csv file with all the character info in it
	with open('characters.txt','rb') as characterfile:
		dialect_character = csv.Sniffer().sniff( characterfile.read( 10*1024 ) )
		characterfile.seek(0)
		
		character_reader = csv.DictReader(characterfile, dialect= dialect_character, quoting=csv.QUOTE_NONE)
		#Returns a list of dictionaries not an actual dictionary
		
		#print "Player characters loaded:"
		#char_fields = character_reader.fieldnames
		#print ('\t'.join(char_fields))

		#This takes a row from the list of dictionaries and gives you a single dictionary
		#which is passed to the Character object to create a single instance of a character

		for characters in character_reader:
			#print('\t'.join(characters[field] for field in char_fields))
			#print characters
			char1 = Character(characters)
			char_instances.append(char1)
			#print char1

	
	mon_instances = []	
	with open('monsters.txt','rb') as monsterfile:
		dialect_monster = csv.Sniffer().sniff( monsterfile.read( 10*1024 ) )
		monsterfile.seek(0)

		monster_reader = csv.DictReader(monsterfile, dialect=dialect_monster)
		#print ""
		#print "Monsters loaded:"

		#mon_fields = monster_reader.fieldnames
		#print ('\t'.join(mon_fields))
		
		for monsters in monster_reader:
			#print characterrow
			mon1 = Monster(monsters)
			mon_instances.append(mon1)
			#print mon1

	char_instances = [char1 for char1 in char_instances if char1.isAlive()]
	mon_instances = [mon1 for mon1 in mon_instances if mon1.isAlive()]

	# Sets up the different dice
	d4 = Dice(4)
	d6 = Dice(6)
	d8 = Dice(8)
	d10 = Dice(10)
	d20 = Dice(20)

	# Into the fray
 	rounds = 0
 	combat_counts = 0

 	to_hit_ac = {'9':10,'8':11,'7':12,'6':13,'5':14,'4':15,'3':16,'2':17,'1':18,'0':19,'-1':20}

	print ""
	print "Into the Fray"
	thefray = char_instances + mon_instances
	#print thefray
	for meat in thefray:
		print meat
	print ""

	# Test to see if we can access the instances in the list
	#for meat in thefray:
	#	if meat.TYPE == "PC":
	#		print meat.TYPE
	combats = raw_input("How many fights to you want to simulate?")
	combats = int(combats)
	pc_dmg = d6.roll_one()
	npc_dmg = d6.roll_one()

	while combat_counts < combats:
		for meat in thefray:
			pcs_init = d6.roll_one()
			npcs_init = d6.roll_one()
			rounds = rounds + 1

			print "ROUND"  + "\t" + "C_INIT" + "\t" + "NAME" + "\t" + "HP" + "\t" + "M_INIT" + "\t"
			for meat in thefray:
				print str(rounds)  + "\t" + str(pcs_init) + "\t" + meat.NAME + "\t" + str(meat.HP) + "\t" + str(npcs_init) + "\t"
				print ""
				print(random.choice(thefray))
				print(random.choice(char_instances))
				print(random.choice(mon_instances))


		combat_counts = combat_counts + 1
main()

