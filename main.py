
import csv
import time

import folium
from folium.plugins import MousePosition, LocateControl
from get_locations import get_route_dict, get_route_tree
from short_module import shortest_path
# import requests
import json
# import geocoder
path = './data/all_points.json'
global time_all
time_all = []
def decorator_time_taken(fnc):
    def inner(*args):
        start = time.process_time()
        ret = fnc(*args)
        end = time.process_time()
        print("{} took {} seconds".format(fnc, (end - start)))
        time_all.append(end-start)
        return ret
    return inner

def show_all_markers(map,mode = 'j'):
    routes = get_route_dict(path)
    for markers in routes:
        lat,lng = get_coordinates(markers,mode)
        folium.Marker([lat,lng],popup=markers).add_to(map)

# def test():
#     m = folium.Map()
# @decorator_time_taken
def get_coordinates(id,mode ='j'):
    if mode=='j':
        routes = get_route_dict(path)
        coords = routes[id]['lat_lng'].split(',')
        return (float(coords[0]), float(coords[1]))
    else:
        routes = get_route_tree(path)
        coords = routes.search(routes.root,int(id)).lat_lng
        return (float(coords[0]), float(coords[1]))

# @decorator_time_taken
def show_all_routes(map,mode='j'):
    routes = get_route_dict(path)
    for markers in routes:
        # lat1,lng1 = get_coordinates(markers)
        for dest in routes[markers]['adj'].split(','):
            # lat2,lng2 =   get_coordinates(dest)
            folium.PolyLine(locations = [(get_coordinates(markers,mode)), (get_coordinates(dest,mode))],
                line_opacity = 0.5, color = 'green').add_to(map)


def draw_route(src,dest,map):
    short_route = shortest_path(src,dest)
    for id in range(len(short_route['path'])-1):
        folium.PolyLine(locations= [(get_coordinates(str(short_route['path'][id]))), (get_coordinates(str(short_route['path'][id+1])))],popup=str(short_route['dist'])+" metres").add_to(map)


def mark_source_dest(src,dest,map):
    routes = get_route_dict(path)
    src_latlng = get_coordinates(str(src))
    dest_latlng =  get_coordinates(str(dest))
    folium.Marker(src_latlng,popup= routes[str(src)]['label'].split(',')[0],icon=folium.Icon(color='blue')).add_to(map)
    folium.Marker(dest_latlng,popup= routes[str(dest)]['label'].split(',')[0],icon=folium.Icon(color='red')).add_to(map)
# def choose_points(src,dest):
#     if src is 
def start(src,dest):
    src_pt = 0
    dest_pt = 0
    with open('./data/addall_points.json','r') as f:
        data = json.load(f)
        src_pt = int(data[src])
        dest_pt = int(data[dest])

    lat,lng = get_coordinates(str(src_pt))
    m = folium.Map(location = [lat, lng],zoom_start = 20,zoom_control=False,)
    LocateControl().add_to(m)
    LocateControl(
        auto_start=True
    )


    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)
    # show_all_markers(m)
    # show_all_routes(m)
    mark_source_dest(src_pt,dest_pt,m)
    draw_route(src_pt,dest_pt,m)
    
    m.get_root().render()
#     print('sdas')
#     m.save("./templates/__map.html")

def reset():
    m = folium.Map(location = [12.752812133105126, 80.19658495347934],zoom_start = 20,zoom_control=False,)
    LocateControl().add_to(m)
    LocateControl(
        auto_start=True
    )

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)
    # show_all_markers(m,'j')
    # show_all_routes(m,'t')

    m.save("./templates/__map.html")

# m = folium.Map()


# @decorator_time_taken
# def test_inner(limit,mode='j'):
#     for i in range(limit):
#         show_all_routes(m,mode)

# def test(mode='j'):
#     for i in range(150):
#         test_inner(i+1,mode)

# def results():
#     test(mode='j')
#     with open('./data/hash.csv','w') as f:
#         writer = csv.writer(f)
#         writer.writerow(time_all)
#     time_all.clear()
#     print('DONE')
#     test(mode='t')
#     with open('./data/tree.csv','w') as f:
#         writer = csv.writer(f)
#         writer.writerow(time_all)        



# reset()
start("SSN Main Entrance","Library")
