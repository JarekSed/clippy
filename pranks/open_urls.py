import subprocess
import random

urls = [
    ("http://www.youtube.com/watch?v=wDajqW561KM", "Congratulations!"),
    ("http://www.youtube.com/watch?v=yzC4hFK5P3g", "PONPONPON"),
    ("http://www.youtube.com/watch?v=LkCNJRfSZBU", "LEEEEEEEEEROOOOOOOOOOOOY"),
    ("http://www.youtube.com/watch?v=wvsboPUjrGc", "DEVELOPERS DEVELOPERS DEVELOPERS"),
    ("https://www.smore.com/clippy-js", "Have some Clippy with your Clippy"),
    ("http://en.wikipedia.org/wiki/Special:Random", "Opening a random wikipedia page"),
    ("http://www.youtube.com/watch?v=xuPSIbABYVU", "Jazz hands!"),
    ("http://www.reddit.com/r/mylittlepony", "Do you like ponies?"),    
    ("http://www.youtube.com/watch?v=ZZ5LpwO-An4", "I feel a little peculier."),
    ("http://www.youtube.com/user/USClippyPaperclip", "Did you know I have a youtube channel?"),
    ("http://www.youtube.com/watch?v=NI2LVI4xgvs", "Episode.1 - Clippy Gets Clipped"),
    ("http://www.nyan.cat/", "nyan"),
    ("http://www.youtube.com/watch?v=8fvTxv46ano", "This is truely a classic."),
]

def run_prank():
    """Randomly opens funny urls, displays message"""

    url_command = "xdg-open {url}"

    url = random.choice(urls)

    url_p = subprocess.Popen(url_command.format(url=url[0]) , shell=True, stdout=subprocess.PIPE)

    return (True, url[1]) 
