from gmusicapi import Webclient
wc = Webclient()

username = raw_input("U: ")
password = raw_input("P: ")

wc.login(username, password)

print "Getting Songs... (This may take some time)"
library = wc.get_all_songs()
notFound = True

while notFound:
  songName = raw_input("Name of song to change: ")
  song = [track for track in library if track['title'] == songName]
  if song is None:
    print "Song not found."
  else:
    notFound = False

playCount = input("New play count: ")
song[0]['playCount'] = playCount
wc.change_song_metadata(song)
print "Done!"

