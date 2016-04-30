# __author__ = 'anastasiiakorosteleva'
# from wand.image import Image
# from wand.display import display
# from wand.color import Color
#
# with Image(filename='mona-lisa.jpeg') as img:
#     print(img.size)
#     for r in 1, 2, 3:
#         with img.clone() as i:
#             i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
#             i.rotate(90 * r)
#
#             i.save(filename='mona-lisa-{0}.png'.format(r))
#             display(i)
#
#     img.background_color = Color("white")
#     img.save(filename="mona-lisa1.jpeg")
#     img.alpha_channel = False
#     img.save(filename="pic2.png")
# from Bio import SeqIO
#
# short_sequences = [] # Setup an empty list
# for record in SeqIO.parse(open("cor6_6.gb", "rU"), "genbank") :
#     if len(record.seq) < 300 :
#         # Add this record to our list
#         short_sequences.append(record)
#
# print ("Found %i short sequences" )% len(short_sequences)
#
# output_handle = open("short_seqs.fasta", "w")
# SeqIO.write(short_sequences, output_handle, "fasta")
# output_handle.close()

from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

