import os
from guessit import guessit
def test():

##    parser = argparse.ArgumentParser(description='Sort files by name')
##
##    parser.add_argument('bla', metavar='bla'
##                        , help='bla')
##    args = pareser.parse_args()
    
    destination = ('C:\Verkefni4\Sorted')
    downloads = ('C:\Verkefni4\downloads')
    TvShow = ('C:\Verkefni4\Sorted\Tv-Show')
    Movie = ('C:\Verkefni4\Sorted\Movies')
##    others = ('C:\Verkefni4\Sorted\Unsorted')
    
    vid_ext=('.mov','.mpg','.avi','.mp4','.wmv','.asf','.mpeg','.flv')


    if not os.path.exists(destination):
        os.makedirs(destination)
            
            
    for root, dirs, files in os.walk(downloads):
        for f in files:
            if f.endswith(vid_ext):
                guess = guessit(f)
                if 'season' in guess:
                    if not os.path.exists(TvShow):
                        os.makedirs(TvShow)
                    Season = str(guess['season'])
                    if 'title' in guess:
                        seasonName = str(guess['title'])
                        
                    showpath = os.path.join(TvShow, seasonName)
                    CopyFile(showpath, Season, f, root)
##                if not 'season' in guess or not 'episode_title' in guess:
##                    if not os.path.exists(Movie):
##                        os.makedirs(Movie)
##                    movieName = str(guess['title'])
##                    showpath = os.path.join(Movie, movieName)
##                    CopyFile(Movie, movieName, f, root)

                        
def CopyFile(showpath, Season, f, root):
    if not os.path.exists(showpath):
         os.makedirs(showpath)
    if not os.path.exists(os.path.join(showpath, Season)):
         os.makedirs(os.path.join(showpath, Season))
         os.rename(os.path.join(root, f), os.path.join(os.path.join(showpath, Season), f))
    else:
        if not os.path.exists(os.path.join(os.path.join(showpath, Season), f)):
            os.rename(os.path.join(root, f), os.path.join(os.path.join(showpath, Season), f))
            print(os.path.join(os.path.join(showpath, Season), f))

##def CopyFileMovies(showpath, Seas f, root):
##    if not os.path.exists(showpath):
##         os.makedirs(showpath)
##    if not os.path.exists(os.path.join(showpath, Season)):
##         os.makedirs(os.path.join(showpath, Season))
##         os.rename(os.path.join(root, f), os.path.join(os.path.join(showpath, Season), f))
##    else:
##        if not os.path.exists(os.path.join(os.path.join(showpath, Season), f)):
##            os.rename(os.path.join(root, f), os.path.join(os.path.join(showpath, Season), f))
##            print(os.path.join(os.path.join(showpath, Season), f))    
##                else:
##                    if not os.path.exists(others):
##                        os.makedirs(others)
##                        os.rename(os.path.join(root, f), os.path.join(others, f))
