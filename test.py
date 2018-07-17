from Cleanify.Cleanify import *

clf = Cleanify()

auth = clf.auth('Toxic Language Bot-5a59bdbe5205.json', 'Copy of VULGARITY ENTITIES lexicon')
tx = clf.censor('this is شنق')

print(tx)