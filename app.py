import ee
import geemap.foliumap as geemap
import geopandas as gpd
import streamlit as st

st.markdown("""
## Country Border            
""")

Map = geemap.Map()
# Load the FeatureCollection
all_nations = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')

# Function to convert FeatureCollection to list of country names
def get_country_names():
    # Retrieve the list of country names
    countries = all_nations.aggregate_array('country_na').getInfo()
    countries.sort()
    countries.insert(0, "Select")
    return countries

# Get the list of all countries
all_countries = get_country_names()

st.sidebar.title("All the contries")

option = st.sidebar.selectbox(
    "Select Your country",
    all_countries,
    placeholder="Select"
)

# Map
if option == "Select":
    Map.to_streamlit(width=800, height=500)
elif option != "Select":
# else:
    country = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017').filter(
    ee.Filter.eq('country_na', option)
    )
    style = {'color': 'black', 'fillColor': 'D3D3D3'}
    Map.addLayer(country.style(**style), {}, option)
    Map.centerObject(country)

    # # Save the country data as a shapefile
    # ext = ".shp"
    # geemap.ee_to_shp(country, option + ext)

    Map.to_streamlit(width=800, height=500)

