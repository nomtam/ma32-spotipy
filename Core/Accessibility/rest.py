from flask import Flask

app = Flask(__name__)


@app.route("/artists")
def get_all_artists(username):
    from Core.music_structures.search import get_all_artists
    return get_all_artists(username)
