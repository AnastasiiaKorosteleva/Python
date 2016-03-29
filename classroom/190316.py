__author__ = 'anastasiiakorosteleva'

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "ptichka.sinichka1@gmail.com"
handle = Entrez.einfo()
result = handle.read()
print(result)
handle = Entrez.esearch(db="Gene",
term = "Homo sapiens (human)[Orgn] AND ASIC1[Gene]")
record = Entrez.read(handle)
record["Count"]
Id_List = record["IdList"]
handle = Entrez.efetch(db="Gene", id="41",
                      rettype="fasta", retmode="text")
print(handle.read())

