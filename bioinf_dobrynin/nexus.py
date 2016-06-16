__author__ = 'anastasiiakorosteleva'
from Bio.Nexus import Nexus
# the combine function takes a list of tuples [(name, nexus instance)...],
#if we provide the file names in a list we can use a list comprehension to
# create these tuples

file_list = ['apoa1.nex', 'apoe.nex', 'cyt450.nex', 'ace.nex', 'ABO.nex', "apoa5.nex", 'apod.nex', 'cdk6.nex', 'CETP.nex',
             'ETV6.nex', 'Gckr.nex', 'gdf5.nex','LDLR.nex', 'lpl.nex', 'NAT2.nex', 'park2.nex', 'SLC22A5.nex', 'UGT1A9.nex',
             'HMGA2.nex', 'apoc1.nex']
nexuses = [(fname, Nexus.Nexus(fname)) for fname in file_list]

combined = Nexus.combine(nexuses)
combined.write_nexus_data(filename=open('combo.nex', 'w'))