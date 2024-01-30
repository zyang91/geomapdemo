# Usage

Below is a list of some commonly used functions available in the **geomapdemo** Python package. Please check the [API Reference](https://zyang91.github.io/geomapdemo/geomapdemo/) for a complete list of all available functions.

To create an ipyleaflet-based interactive map:

```python
import geomapdemo
m = geomapdemo.Map(center=[40,-100], zoom= 4)
m
```


To create a folium-based interactive map:

```python
import geomapdemo.foliumap as geomapdemo
m = geomapdemo.Map(center= [40,-100], zoom = 4)
m
```


To add additional basemaps to the Map:

```python
Map.add_basemap('Esri.OceanBasemap')
Map.add_basemap('Esri.NatGeoWorldMap')
```

To generate random string

```python
geomapdemo.generate_random_string()
geomapdemo.generate_random_string(9, upper=True, digits=True)
```

To generate random number

```python
geomapdemo.generate_lucky_number()
geomapdemo.generate_lucky_number(10)
```