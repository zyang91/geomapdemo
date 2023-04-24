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