import time
import random
#names of 300 something songs from 1980 seperated by 5 spaces
songNamesFile = open("songnames.txt", "r")

songNames = songNamesFile.read()
songNamesFile.close()
listOfSongNames = songNames.splitlines()
count = 0
for i in range(0,len(listOfSongNames)):
    listOfSongNames[i] = listOfSongNames[i].split("     ", 3)
    listOfSongNames[i] = listOfSongNames[i][1:3]

def bubble_sort(Classguylist):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(Classguylist) - 1):
            if Classguylist[i].score < Classguylist[i + 1].score:
                Classguylist[i], Classguylist[i + 1] = Classguylist[i + 1], Classguylist[i]
                swapped = True


#add genre if we have time
class NewSong:
    def __init__ (self, timeAdded, artist, name, likePattern, score):
        self.timeSinceAdding = 0
        self.likes = 0
        self.dislikes = 0
        self.artist = artist
        self.name = name
        self.likePattern = likePattern
        #how it's rated:
        self.score = score
    def ratio(self):
        if(self.dislikes != 0):
            return self.likes-self.dislikes
        else:
            return self.likes
#List of like patterns
#5 = loved (5/1)
#4 = liked (4/2)
#3 = middle (3/3)
#2 = disliked (2/4)
#1 = hated (1/5)
count2 = 0
currentSongList = []
counter3 = 0
while(True):
    time.sleep(1/30)
    if(random.randint(1,450)==2):
        x = random.randint(0,330)
        if(len(currentSongList)== 0):
            currentSongList.append(NewSong(time.time(),listOfSongNames[x][0],listOfSongNames[x][1], random.randint(1,5), time.time()))
        else:
            biggestScore = currentSongList[0].score
            for i in currentSongList:
                if i.score > biggestScore:
                    biggestScore = i.score
            currentSongList.append(NewSong(time.time(),listOfSongNames[x][0],listOfSongNames[x][1], random.randint(1,5), biggestScore+300))

        print("New Song In Library! It is: " + currentSongList[len(currentSongList)-1].name + " by " + currentSongList[len(currentSongList)-1].artist)

    for i in currentSongList:
        #adds like or dislike every 15 seconds
        if(random.randint(1,450)==3):
            if(random.randint(1,6)<=i.likePattern):
                i.likes+=1
            else:
                i.dislikes+=1
    count2+=1
        
    for i in currentSongList:
        i.timeSinceAdding+=1
        i.score = i.score+ i.timeSinceAdding * (i.ratio())
    bubble_sort(currentSongList)
    if(counter3>=900):
        print("here is the current order of songs:")
        for i in currentSongList:
            print( i.artist+ " - "+i.name + ". Likes: " + str(i.likes)+ ". Dislikes: " + str(i.dislikes) + ". Score " + str(i.score))
        counter3 = 0
    counter3+=1


print("done")