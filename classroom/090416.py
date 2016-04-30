__author__ = 'anastasiiakorosteleva'
from Bio import Entrez
Entrez.email = "korosteleva-a@mail.ru"
handle = Entrez.einfo()
#print(handle.read())


query = "asic1[Item Name] AND Homo Sapiens[organism]"
handle = Entrez.esearch("protein", query)
#смотрим ссылки айдишников
# print(handle.read())
#теперь смотрим список айдишников
query_data = Entrez.read(handle)
ids = query_data["IdList"]
# print(type(handle))
for protein_id in ids:
    handle = Entrez.esummary(db = "protein", id = protein_id)
    protein_data = Entrez.read(handle)[0]
    # print(protein_data.keys())
    # print("\t".join([protein_data["Status"], protein_data["Title"]]))
# print(query_data.keys())
ids = query_data["IdList"]
handle = Entrez.epost(db = "protein", id = ",".join(ids))
post_data = Entrez.read(handle)
key = post_data["QueryKey"]
webenv = post_data["WebEnv"]
# print(key)
# print(webenv)
handle = Entrez.esummary(db = "proteins",
                         webenv = webenv,
                         query_key = key)
# print(handle.read())

print(key)
print(webenv)

import csv
f = open("sc_rnaseq.tsv")
tsvin = csv.reader(f, delimiter = "\t")
for row in tsvin:
    print(row)
f.close()
f = open(" ", w)
tsvout = csv.writer(f,delimiter = "\t" )
