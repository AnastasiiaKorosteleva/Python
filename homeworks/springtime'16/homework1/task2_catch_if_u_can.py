__author__ = 'anastasiiakorosteleva'

try:
    foo()
except (AssertionError):
     print("Caught AssertionError")
except (MemoryError):
    print("Caught MemoryError")
except (RuntimeError):
    print("Caught RuntimeError")


# try:
#     foo()
# except (AssertionError, MemoryError, RuntimeError) as err:
#      print("Caught", err)