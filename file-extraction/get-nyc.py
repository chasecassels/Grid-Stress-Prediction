#Downloads NYC station CSVs from CHUWD-H v1.0 project (from Open Science Foundation)

import re
import requests
import os
from osfclient.api import OSF
import geopandas as gpd
from shapely.geometry import Point

nyc_boundary = gpd.read_file("nybb_25c/nybb.shp")
nyc_boundary = nyc_boundary.to_crs(epsg=4326)

#connect to OSF project
osf = OSF()
project = osf.project("5dp8e")

storage_url = project._storages_url
response = requests.get(storage_url)
storages = response.json()

print(f"Listing files in project {project}:")
print("Title:", project.title) 
print(vars(project))

#all_components = project.children()
target_folder = "../source-data"
nyc_files = []

children_url = project._links['relationships']['children']['href']
children_response = requests.get(children_url)
children_data = children_response.json()

print(f"\nSubprojects found: {len(children_data.get('data', []))}")

# Iterate over subprojects
for child in children_data.get('data', []):
    child_name = child['attributes']['title']
    print(f"\nChecking subproject: {child_name}")

# Iterate over top-level folders (years)
for storage in storages.get('data', []):
    
    files_url = storage['relationships']['files']['links']['related']['href']
    files_response = requests.get(files_url)
    files_data = files_response.json()

    for file_object in files_data.get('data', []):
        fname = file_object['attributes']['name']
        print(f"Checking file: {fname}")
        if fname.endswith(".csv"):
            """# Extract lat/lon from filename
            match = re.search(r"Lat_([0-9\.-]+)_Lon_([0-9\.-]+)", fname)
            if match:
                lat, lon = float(match.group(1)), float(match.group(2))
                point = Point(lon, lat)
                if nyc_boundary.contains(point).any():"""
            nyc_files.append(file_object)

print(f"Found {len(nyc_files)} NYC station CSVs.")

# Download the matching CSVs
for f in nyc_files:
    print(f"Downloading {f.name}...")
    f.download(path=target_folder)

print(f"Done! All files saved to {target_folder}")
