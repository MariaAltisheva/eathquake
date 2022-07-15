"""Основной файл."""
from plotly import offline
from plotly.graph_objs import Layout

from utils import get_questions_data_by_requests
# Получаем данные по ссылке в виде json
all_eq_data = get_questions_data_by_requests()
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
# Нанесение данных на карту
data = [{'type': 'scattergeo', 'lon': lons, 'lat': lats,
         'text': hover_texts,
         'marker': {'size': [5 * mag for mag in mags],
                    'color': mags, 'colorscale': 'Viridis',
                    'reversescale': True,
                    'colorbar': {'title': 'Magnitude'}}}]
my_layout = Layout(title='Global Eathquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_eathquakes.html')
