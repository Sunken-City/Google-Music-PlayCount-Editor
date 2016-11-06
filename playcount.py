from gmusicapi import Mobileclient
mc = Mobileclient()

username = input("U: ")
password = input("P: ")
androidid = mc.FROM_MAC_ADDRESS

mc.login(username, password, androidid)

print("Getting Songs... (This may take some time)")
library = mc.get_all_songs()
notFound = True

while notFound:
  songName = input("Name of song to change: ")
  song = [track for track in library if track['title'] == songName]
  if song is None:
    print("Song not found.")
  else:
    notFound = False

songID = song[0]['id']
playCount = eval(input("New play count: "))
mc.increment_song_playcount(songID, plays=playCount)
print("Done!")

