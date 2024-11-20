
N = int(input())
Playlist = list(map(int, input().split()))
maxivalue = max(Playlist)
num=max(Playlist,key=Playlist.count)
count=Playlist.count(num)
orgcount=0
for i in Playlist:
    m=Playlist.count(i)
    if m==count:
        orgcount+=1


print(int(orgcount/count))