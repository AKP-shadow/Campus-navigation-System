
import json
import math
from points_tree import all_point_tree
def get_route_tree(path):
    route_tree = all_point_tree()
    root = None
    with open(path,"r") as file:
        data = json.load(file)  
    for keys in data:
        lat,lng = data[keys]['lat_lng'].split(',')
        label = data[keys]['label'].split(',')[0]
        adj = data[keys]['adj'].split(',')
        is_marker = bool(data[keys]['is_marker'])
        root = route_tree.insert_node(root,int(keys),(lat,lng),label,adj,is_marker)
        route_tree.root = root
    # route_tree.preorder(root)
    return route_tree

def get_route_dict(path):
    with open(path,"r") as file:
        data = json.load(file)
    return data

def find_distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance_bw_ori_desti = radius * c
    return round(distance_bw_ori_desti*1000,2)

def create_mat(path):
    routes = get_route_dict(path)
    mat = [[0 for _ in range(len(routes))] for _ in range(len(routes))]
    for markers in routes:
        lat1,lng1 = routes[markers]['lat_lng'].split(',') 
        for dest in routes[markers]['adj'].split(','):
            lat2,lng2 =   routes[dest]['lat_lng'].split(',')
            mat[int(markers)-1][int(dest)-1] = find_distance((float(lat1),float(lng1)), (float(lat2), float(lng2)))  # type: ignore
    return mat


# print(create_mat('all_points.json'))
# a = get_route_tree('./data/all_points.json')
# root = a.root
# node = a.search(a.root,15 )
# print(node.label)
# print(node.is_marker)
# print(node.lat_lng)
