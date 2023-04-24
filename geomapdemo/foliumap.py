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
    

