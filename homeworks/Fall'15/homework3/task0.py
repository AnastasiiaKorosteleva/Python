__author__ = 'anastasiiakorosteleva'
class Song:
    def __init__(self, name,  artist, name_of_album, position, year, duration):
        self.artist = artist
        self.name = name
        self.name_of_album = name_of_album
        self.position = position
        self.year = year
        self.duration = duration

    def __repr__(self):
        # song = "Song \"%s\" by %s" % (self.name, self.artist)
        song = self.name + "\t"+ self.artist + "\t" + self.name_of_album + "\t" + self.position + "\t" + self.year + "\t" + self.duration
        return song


songs = []
def import_songs():
    input_file = open("songs.txt", "r")
    for line in input_file:
        name, artist, name_of_album, position, year, duration = line.split("\t")
        songs.append(Song(name, artist, name_of_album, position, year, duration))


def export_songs(songs, export_file):
    file = open(export_file, 'w')
    file.write('\n'.join(str(song) for song in songs))
    file.close()

# artist
popular_artist = {} #dictionary key = artist_name, value = count
for song in songs:
    artist_name = song.artist
    if artist_name not in popular_artist:
        popular_artist[artist_name] = 1
    elif artist_name in popular_artist:
        popular_artist[artist_name] = popular_artist[artist_name] + 1
max_count = None
for artist_name, count in popular_artist.items():
    if max_count is None or count > max_count:
        popular = artist_name
        max_count = count
        print(popular)
#end artist

# longest song
longest_song = {} #dictionary key = name, value = duration
for i in songs:
    longest_song[i.name] = i.duration
max_duration = max(longest_song.values())
for line in songs:
    if max_duration in line.duration:
        print(line.name + "\t" + line.artist)
#print(max_duration)

#end longest song




#popular_album
popular_album = {} #dictionary key = album_name, value = count
for song in songs:
    album_name = song.name_of_album
    if album_name not in popular_album:
        popular_album[album_name] = 1
    elif album_name in popular_album:
        popular_album[album_name] = popular_album[album_name] + 1
max_count = None
for album_name, count in popular_album.items():
    if max_count is None or count > max_count:
        pop_alb = album_name
        max_count = count
for song in songs:
    if pop_alb == song.name_of_album:
        print(pop_alb + "\t" + song.artist)
        break
#end popular_album



#the_most frequent words

#frequency = {} # word = key, count = value
#for song in songs:

    #words = song.name.split()

    #for word in words:
     #   word_tmp = word.lower()
    #    if word_tmp not in frequency:
   #         frequency[word_tmp] = 1
  #      elif word in frequency:
 #           frequency[word_tmp] = frequency[word_tmp] + 1
#count = list(frequency.values())
#count.sort(reverse=True)
#print(count)
#i = 0
#for key, values in frequency.items():
 #   if values == count[i] :
  #      print(key)
        i = i + 1
#end


#the_most_hardworking_artist( biggest number of album)

album_counts = {}
for song in songs:
    album_counts[song.artist] = album_counts.get(song.artist, []) + [song.name_of_album]
max_count = None
for artist, albums in album_counts.items():
    albums = set(albums)
    if max_count is None or len(albums) > max_count:
        hardworking = artist
        max_count = len(albums)
print(hardworking)

#end
