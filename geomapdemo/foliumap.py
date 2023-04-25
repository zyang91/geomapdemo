'''Folium module for creating a map.'''


import folium

class Map(folium.Map):
    '''Create a folium map object.'''

    def __init__(self, center= [20,0], zoom=10, **kwargs) -> None:
        '''Initialize the map objects.
        Args:
            center (list, optional): The center of the map. Defaults to [20,0].
            zoom (int, optional): Zoom level. Defaults to 10.
            **kwargs: Keyword arguments.
        '''

        super().__init__(location=center, zoom_start=zoom, **kwargs)

    def add_tile_layer(self, url, name, attribution=" ", **kwargs):
        """Adds a tile layer to the map
        Args:
            url (str): The url of the tile layer.
            name (str): The name of the tile layer.
            attribution (str, optional): The attribution of the tile layer. Defaults to "".
            **kwargs: Keyword arguments to be passed to the tile layer.
        """        
        tile_layer= folium.TileLayer(
            tiles= url, 
            name=name, 
            attr=attribution, 
            **kwargs)
        self.add_child(tile_layer)
    
    def add_marker(self, location, popup, **kwargs):
        """Adds a marker to the map
        Args:
            location (list): The location of the marker.
            popup (str): The popup text of the marker.
            **kwargs: Keyword arguments to be passed to the marker.
        """        
        marker= folium.Marker(
            location=location, 
            popup=popup, 
            **kwargs)
        self.add_child(marker)
    
    def add_circle_marker(self, location, radius= 10, popup = "", fill= True, **kwargs):
        """Adds a circle marker to the map
        Args:
            location (list): The location of the marker.
            radius (int): The radius of the circle marker.Defaults to 10.
            popup (str): The popup text of the marker.
            fill (bool): Whether to fill the circle marker. Defaults to False.
            **kwargs: Keyword arguments to be passed to the marker.
        """        
        marker= folium.CircleMarker(
            location=location, 
            radius=radius, 
            popup=popup,
            fill=fill, 
            **kwargs)
        self.add_child(marker)

    def add_circle(self, location, radius = 10, popup ="", fill = False, **kwargs):
        """Adds a circle to the map
        Args:
            location (list): The location of the circle.
            radius (int): The radius of the circle marker.Defaults to 10.
            popup (str): The popup text of the marker.
            fill (bool): Whether to fill the circle marker. Defaults to False.
            **kwargs: Keyword arguments to be passed to the marker.
        """
        marker= folium.Circle(
            location=location,
            radius=radius,
            popup=popup,
            fill=fill,
            **kwargs)
        self.add_child(marker)
    
    def click_for_marker(self, popup="click Point"):
        """Adds a click listener to the map to add markers.
        Args:
            popup (str): The popup text of the marker. Defaults to "click Point".
        """        
        self.add_child(folium.ClickForMarker(popup=popup))
    
    def add_polylines(self, locations, popup="", **kwargs):
        """Adds a polyline to the map
        Args:
            locations (list): The locations of the polyline.
            popup (str): The popup text of the polyline.
            **kwargs: Keyword arguments to be passed to the polyline.
        """        
        polyline= folium.PolyLine(
            locations=locations,
            popup=popup,
            **kwargs)
        self.add_child(polyline)

    def add_polygon(self, locations, popup="", **kwargs):
        """Adds a polygon to the map
        Args:
            locations (list): The locations of the polygon.
            popup (str): The popup text of the polygon.
            **kwargs: Keyword arguments to be passed to the polygon.
        """        
        polygon= folium.Polygon(
            locations=locations,
            popup=popup,
            **kwargs)
        self.add_child(polygon)
    
    def set_center(self, lat, lon, zoom=10):
        """Sets the center of the map
        Args:
            lat (float): The latitude of the center.
            lon (float): The longitude of the center.
            zoom (int): The zoom level. Defaults to 10.
        """        
        self.fit_bounds([[lat, lon], [lat, lon]], max_zoom=zoom)
    
    def add_geojson(
        self,
        in_geojson,
        layer_name="Untitled",
        encoding="utf-8",
        **kwargs,
    ):
        """Adds a GeoJSON file to the map.

        Args:
            in_geojson (str): The input file path to the GeoJSON.
            layer_name (str, optional): The layer name to be used. Defaults to "Untitled".
            encoding (str, optional): The encoding of the GeoJSON file. Defaults to "utf-8".

        Raises:
            FileNotFoundError: The provided GeoJSON file could not be found.
        """
        import json
        import requests

        if in_geojson.startswith("http"):
            response = requests.get(in_geojson)
            data = response.json()
        else:
            try:
                with open(in_geojson, encoding=encoding) as f:
                    data = json.load(f)
            except FileNotFoundError:
                raise FileNotFoundError(
                    "The provided GeoJSON file could not be found."
                )

        # interchangeable parameters between ipyleaflet and folium.
        style_dict = {}
        if "style_function" not in kwargs:
            if "style" not in kwargs:
                style_dict = {
                    # "stroke": True,
                    "color": "#3388ff",
                    "weight": 2,
                    "opacity": 1,
                    #"fill": True,
                    #"fillColor": "#ffffff",
                    "fillOpacity": 0,
                    # "dashArray": "9"
                    # "clickable": True,
                }
                kwargs["style_function"] = lambda x: style_dict
            else:
                style_dict = kwargs["style"]
                kwargs["style_function"] = lambda x: style_dict


        geojson = folium.GeoJson(
            data=data, name=layer_name, **kwargs
        )
        self.add_child(geojson)
        
