from flask import Flask, redirect, render_template, request, url_for
import json
from main import start, reset
from data import junk
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

        # sources[0], sources[sources.index(src)] = sources[sources.index(src)], sources[0]
        # destinations[0], destinations[destinations.index(dest)] = destinations[destinations.index(dest)], destinations[0]

        # print(sources)
        # print(destinations)
        # start(src, dest)
        # Passed the string as it is
        return render_template('home.html', sources=sources, destinations=destinations,to_html = (start(src,dest)) ) # Tried to read pass the string as argument to the include tag in home.html
#         return render_template('home.html', sources=sources, destinations=destinations,to_html = '__map.html' )
    # made another html file called 'def.html' which uses the include command to render the __map.html
    return render_template('def.html', sources=sources, destinations=destinations,to_html = '__map.html')

@app.route('/check')
def check():
    return render_template('__map.html')
    

app.run(debug=True)
