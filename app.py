from flask import Flask, redirect, render_template, request, url_for
import json
from main import start, reset

app = Flask(__name__)

with open(u'./data/addall_points.json','r') as f:
    data = json.load(f)
    places = list(data.keys())
    sources, destinations = places.copy(), places.copy()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        src = request.form.get('source')
        dest = request.form.get('destination')

        # print(src)
        # print(dest)

        sources[0], sources[sources.index(src)] = sources[sources.index(src)], sources[0]
        destinations[0], destinations[destinations.index(dest)] = destinations[destinations.index(dest)], destinations[0]

        # print(sources)
        # print(destinations)

        start(src, dest)
        return render_template('home.html', sources=sources, destinations=destinations,to_html = '__map.html'))
    
    return render_template('home.html', sources=sources, destinations=destinations,to_html='__map.html')

@app.route('/check')
def check():
    return render_template('__map.html')
    

