#!/usr/bin/env pipenv run python

from simple_ffmpeg import Ffmpeg

clip1 = 'files/1.mp4'
clip2 = 'files/2.mp4'
clip3 = 'files/3.mp4'
clipA = 'files/A.mp4'
clipB = 'files/B.mp4'
clipC = 'files/C.mp4'
test1 = 'files/test1.mp4'
test2 = 'files/test2.mp4'

def everything():
    movie = Ffmpeg('out.avi')
    movie.append(clip1)
    movie.append(clipA)
    movie.append(clip2)
    movie.append(clipB)
    movie.append(clip3)
    movie.append(clipC)
    movie.write()

def select(filename):
    movie = Ffmpeg('out.mp4')
    movie.append(clip1)

    file = open(filename)
    line = file.read()

    for count in range(2):
        if "A" in line and count == 0:
            movie.append(clipA)
        if "B" in line and count == 1:
            movie.append(clipB)
        if count == 0:
            movie.append(clip2)
        if count == 1:
            movie.append(clip3)

    movie.write()

if __name__ == '__main__':
    # everything()
    select('ffmpeg-assembly-input.txt')
