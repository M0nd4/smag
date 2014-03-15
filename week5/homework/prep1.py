Names = {}
Names['Albert'] = 'Einstein'
Names['Satyendra'] = 'Bose'
Names['Richard'] = 'Feynman'
Names['Ludwig'] = 'Boltzmann'
pp = lambda: [print( name, Names[name]) for name in Names] 
# checkpoint 1
print("checkpoint 1")
pp()
a = Names.pop('Albert')
# checkpoint 2
print("checkpoint 2")
pp()
del Names['Richard']
# checkpoint 3
print("checkpoint 3")
pp()
L = Names.keys()
M = Names.values()
#checkpoint 4
print("checkpoint 4")
pp()
b = 'Wolfgang' in Names
#checkpoint 5
print("checkpoint 5")
pp()
