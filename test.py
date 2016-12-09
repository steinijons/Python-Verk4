
import os
from guessit import guessit
def test():

##    parser = argparse.ArgumentParser(description='Sort files by name')
##
##    parser.add_argument('bla', metavar='bla'
##                        , help='bla')
##    args = pareser.parse_args()
    
    destination = ('C:\Python-Verk4\Sorted')
    downloads = ('C:\Python-Verk4\downloads')
    TvShow = ('C:\Python-Verk4\Sorted\Tv-Show')
    TvShowUnknown = ('C:\Python-Verk4\Sorted\Tv-Show-Unknown')
    Movie = ('C:\Python-Verk4\Sorted\Movies')
    
    vid_ext = ('.mov','.mpg','.avi','.mp4','.wmv','.asf','.mpeg','.flv','mkv')
    Rmv_files = ('.nfo', '.sfv', '.torrent', '.txt', '.mta', 'rar', '.part', '.dat', '.srt', '.DS_Store', '.lnk')
    
    if not os.path.exists(destination):
        os.makedirs(destination)            
            
    for root, dirs, files in os.walk(downloads):
        for f in files:
            if f.endswith(vid_ext):
                guess = guessit(f)
                if guess['type'] == 'episode':                 
                    if not os.path.exists(TvShow):
                        os.makedirs(TvShow)
                    if 'season' in guess and 'title'in guess:
                        Season = str(guess['season'])
                        SeasonName = str(guess['title'])
                        showpath = os.path.join(TvShow, SeasonName)
                        CopyTvShow(showpath, Season, f, root)
                    elif 'season' in guess and not 'title' in guess:
                        Season = str(guess['season'])
                        SeasonName = 'Season-Name-Unknown'
                        showpath = os.path.join(TvShowUnknown, SeasonName)
                        CopyTvShow(showpath, Season, f, root)
                    elif 'title' in guess and not 'season' in guess:
                        Season = 'Unknown'
                        SeasonName = str(guess['title'])
                        showpath = os.path.join(TvShow, SeasonName)
                        CopyTvShow(showpath, Season, f, root)
                    else:
                        Season = 'Season-Unknown'
                        SeasonName = 'Season-Name-Unknown'
                        showpath = os.path.join(TvShowUnknown, SeasonName)
                        CopyTvShow(showpath, Season, f, root)                    
                elif guess['type'] == 'movie' and guess['title'] != 'sample':
                    if not os.path.exists(Movie):
                        os.makedirs(Movie)
                    movieName = str(guess['title'])
                    showpath = os.path.join(Movie, movieName)
                    CopyMovies(showpath, f, root)
            elif f.endswith(Rmv_files):
                os.remove(os.path.join(root, f))
                
        #Eftir eina keyrslu eru 680 folders eftir. En ef maður keyrir 2x þá eru ekki nema 250 folderar eftir
        for d in dirs:    
            if not os.listdir(os.path.join(root, d)):
                os.removedirs(os.path.join(root, d))
                       
                
def CopyTvShow(showpath, Season, f, root):
    if not os.path.exists(showpath):
         os.makedirs(showpath)
    if not os.path.exists(os.path.join(showpath, Season)):
         os.makedirs(os.path.join(showpath, Season))
         os.rename(os.path.join(root, f), os.path.join(os.path.join(showpath, Season), f))
    else:
        if not os.path.exists(os.path.join(os.path.join(showpath, Season), f)):
            os.rename(os.path.join(root, f), os.path.join(os.path.join(showpath, Season), f))
            print(os.path.join(os.path.join(showpath, Season), f))

def CopyMovies(showpath, f, root):
    if not os.path.exists(showpath):
         os.makedirs(showpath)
    if not os.path.exists(showpath):
         os.makedirs(showpath)
         os.rename(os.path.join(root, f), os.path.join(showpath, f))
    else:
        if not os.path.exists(os.path.join(showpath, f)):
            os.rename(os.path.join(root, f), os.path.join(showpath, f))
            print(os.path.join(showpath, f))
