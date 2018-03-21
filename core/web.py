from bottle import default_app, template, TEMPLATE_PATH, static_file
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

