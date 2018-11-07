import os
from os.path import dirname as uf

print(
    os.path.join(uf(uf(__file__)),'public/resource.txt')
)