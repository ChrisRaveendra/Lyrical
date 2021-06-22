from flask import Flask, render_template, request
from lyrics import scrapeLyricsForArtist
from markov import MarkovLyrics

app = Flask(__name__)

def generateArtistLyrics(name):
    songs = scrapeLyricsForArtist(name)
    m = MarkovLyrics()

    for song in songs:
        m.populateMarkovChain(song)
    return m.generateLyrics()

@app.route('/', methods=['GET', 'POST'])
def lyricsGenerator():
    lyrics = ""
    if request.method == "POST":
        artist = request.form['search']
        lyrics = generateArtistLyrics(artist)
    return render_template('home.html', lyrics=lyrics)


if __name__ == '__main__':
    app.run(debug=True)
