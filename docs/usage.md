# Usage

Below is a list of some commonly used functions available in the **geomapdemo** Python package. Please check the [API Reference](https://zyang91.github.io/geomapdemo/geomapdemo/) for a complete list of all available functions.

To create an ipyleaflet-based interactive map:

```python
import geomapdemo
Map = geomapdemo.Map(center=[40,-100], zoom=4)
Map
```

To add additional basemaps to the Map:

```python
Map.add_basemap('Esri.OceanBasemap')
Map.add_basemap('Esri.NatGeoWorldMap')
```

