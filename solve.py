import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# def create_great_circles(start_ids, end_ids):
#     for index, start_id in enumerate(start_ids):
#         end_id = end_ids[index]
#         start_lon = longitudes[start_id]
#         end_lon = longitudes[end_id]
#         start_lat =  latitudes[start_id]
#         end_lat = latitudes[end_id]
#         # end_lat, start_lat = row['end_lat'], row['start_lat']
#         # end_lon, start_lon = row['end_lon'], row['start_lon']
        
#         if abs(end_lat - start_lat) < 180:
#             if abs(end_lon - start_lon) < 180:
#                 m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat)


with open ("data1.json","r") as f:
    data = json.load(f)
    airportsFields = data["airportsFields"]
    airlineFields = data["airlineFields"]
    airports = data["airports"]
    airlines = data["airlines"]
    routes = data["routes"]
    start_idx = [route[1] for route in routes]
    end_idx = [route[2] for route in routes]
    # print(airports)
    longitudes = [ float(airport[3]) for airport in airports if not airport[3] == None and not  airport[4] == None ]
    latitudes = [ float(airport[4])   for airport in airports if not airport[3] == None and not airport[4] == None ]
    # longitudes = longitudes[:20]
    # latitudes = latitudes[:20]
    # print("lenght of longitudes:",len(longitudes))
    # print("length of latitudes:",len(latitudes))
    
    # print("start_idx:",start_idx)
    # print("end_idx:",end_idx)
    # for airport in airports:
    #     if airport[4] == None:
    #         print("fuck")
    # print("longitudes:",longitudes)
    # print("latitudes:",latitudes)
    m = Basemap(projection = 'merc', 
            llcrnrlat = -80,
           urcrnrlat = 80,
           llcrnrlon = -180,
           urcrnrlon = 180)
    # draw coastlines.
    m.drawcoastlines()
    # draw a boundary around the map, fill the background.
    # this background will end up being the ocean color, since
    # the continents will be drawn on top.
    # m.drawmapboundary(fill_color='green')
    # fill continents, set lake color same as ocean color.
    # m.fillcontinents(color='coral',lake_color='aqua')
    x, y = m(longitudes, latitudes)
    # print("x:{0} y:{1}".format(x,y))
    m.scatter(x, y, s=1)
    
    for index, start_id in enumerate(start_idx):
        end_id = end_idx[index]
        start_lon = longitudes[start_id]
        end_lon = longitudes[end_id]
        start_lat =  latitudes[start_id]
        end_lat = latitudes[end_id]
        # end_lat, start_lat = row['end_lat'], row['start_lat']
        # end_lon, start_lon = row['end_lon'], row['start_lon']
        
        if abs(end_lat - start_lat) < 180:
            if abs(end_lon - start_lon) < 180:
                m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat)


    plt.show()