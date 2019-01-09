# -*- coding: utf-8 -*-

import folium
import pandas

data = pandas.read_csv('coord.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['POPULATION'])


def set_color(population):
    if population < 1000000:
        return 'green'
    else:
        return 'red'


map = folium.Map(location=[49.441908, 30.527949], zoom_start=7, tiles='Mapbox Bright')

fg_m = folium.FeatureGroup(name='My map')

for lt, ln, el in zip(lat, lon, elev):
    fg_m.add_child(folium.CircleMarker(location=[lt, ln],
                                       radius=6,
                                       popup='Population: ' + str(el),
                                       fill_color=set_color(el),
                                       color='grey',
                                       fill_opacity=0.7))

fg_p = folium.FeatureGroup(name='Population')

fg_p.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange'
    if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg_m)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save('map.html')
