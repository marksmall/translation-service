import os
import geopandas as gpd

def translate(input_filename, output_filename):
    print(f"Script called with: {input_filename} and {output_filename}", flush=True)


if __name__ == '__main__':
    translate('/opt/resources/stadiums.csv', '/opt/resources/stadiums.geojson')
