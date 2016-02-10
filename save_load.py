import pickle
#from os.path import join as pjoin (I honestly have no idea what purpost this serves, but the program runs without it)
character_dict = {'max_health' : '100', 'current_health' : '80', 'level' : '1', 'current_quest' : 'whatever', 'location' : 'hometown',' weapon' : 'sword_dict', 'tile location' : 'idk', 'map' : 'location'}
#^ random dictionary I put into test it

#you care about this stuff below here:

def save_data(stored_info, file_name): #this can save a dictionary into whatever type of file you want. pass in (dictionary_name, save_name)
	output = open(file_name, 'wb')
	pickle.dump(stored_info, output)
	output.close()

def load_data(save_name): #this retreives the dictionary from the file that you pass into it
	pickled_file = open(save_name, 'rb')
	stored_info = pickle.load(pickled_file)
	return stored_info

	#just a test run
save_data(character_dict, 'omega.py')
character_dict_1 = load_data('omega.py')
print(character_dict_1)
