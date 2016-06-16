__author__ = 'anastasiiakorosteleva'

import requests
from bs4 import BeautifulSoup
from Bio import Entrez
Entrez.email = 'ptichka.sinichka1@gmail.com'

def makelink(db, indexes):
    index = [i for i in indexes]
    list_of_ref = []
    if db.lower() == "protein":
        for i in index:
            list_of_ref.append("http://www.ncbi.nlm.nih.gov/protein/" + str(i))
    elif db.lower() == "nucleotide":
        for i in index:
            list_of_ref.append("http://www.ncbi.nlm.nih.gov/nuccore/" + str(i))
    else:
        print("Wrong database! Enter 'protein' or 'nucleotide'")
    return list_of_ref

def fastafind(link):
    list_of_inputlinks = [inputlink for inputlink in link]
    list_of_links_output = []
    for inputlink in list_of_inputlinks:
        r = requests.get(inputlink)
        soup = BeautifulSoup(r.content, "html.parser")
        if "?report=fasta" not in str(soup.find_all("a")):
            list_of_links_output.append("Broken url")
        else:
            for link in soup.find_all("a"):
                if "?report=fasta" in str(link):
                    list_of_links_output.append("http://www.ncbi.nlm.nih.gov" + link.get("href"))
    return list_of_links_output


filename = input("Enter name of file with indexes: ")
db = input("Enter database (protein or nucleotide): ")
rettype = input("Eter data type (gb or FASTA): ")
of_name = input("Enter output file name.format: ")
find_url = input("Find url's for FASTA files? (Yes/No): ")

i_file = open(filename, 'r')
list_of_indexes = i_file.readlines()
i_file.close()


if find_url == "Yes":
    of_name_ = input("Enter output file name.format: ")
    list_of_ref = makelink(db, indexes = [i.strip() for i in list_of_indexes])
    list_of_links = fastafind(list_of_ref)

    out = ''
    j = 0
    i = 0
    while j < len(list_of_indexes) and i < len(list_of_links):
        out += (list_of_indexes[j].strip() + '\t' + list_of_links[i] + '\n')
        j += 1
        i += 1
    of_file = open(of_name_, "a")
    of_file.write(out)
    of_file.close()

id = [i.strip() for i in list_of_indexes]

handle = Entrez.efetch(db = db, id = id, rettype = rettype, retmode="text")
out = handle.read()
of_file = open(of_name, "a")
of_file.write(out)
of_file.close()