import json
from bottle import default_app, template, TEMPLATE_PATH, static_file, request
from mpd_api import MPD

app = default_app()

TEMPLATE_PATH.insert(0,'./core/views')

mpd = MPD()


@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./core/static')


@app.route('/')
def index():
    return template('index.tpl')


@app.route('/get_curr_playlist')
def get_curr_playlist():
    playlist = mpd.get_playlist()
    return json.dumps(playlist)


@app.route('/set_playlist', method="POST")
def set_playlist():
    playlist = json.loads(request.body.buf)
    mpd.set_playlist(playlist)
    return 'ok'

