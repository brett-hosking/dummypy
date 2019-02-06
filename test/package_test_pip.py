''' 
    Test package after installing with pip
'''
import dummypy

print (dummypy.name)
print (dummypy.__version__)

dummypy.dummypytest.calltest()

# Nested
print (dummypy.packageA.__packageAname__) # from nested __init__.py

dummypy.packageA.Atest.calltest()
dummypy.packageB.Btest.calltest()
