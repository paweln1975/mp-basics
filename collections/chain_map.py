from collections import ChainMap
from named_tuples import monika, paul, emilia

asd = lambda x: x._asdict()
data_list = [asd(p) for p in [monika, paul, emilia]]

chain = ChainMap(*data_list)
print(chain)
print(chain['age']) # first element
print(chain.maps[1])
print(chain.parents)
