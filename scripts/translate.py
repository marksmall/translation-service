import os
import geopandas as gpd

def translate(input_filename, output_filename):
    # Read the data file
    stadiums = gpd.read_file(input_filename)

    # Create a new data frame with an extra column `geometry`, using the
    # `Latitude` and `Longitude` column as values.
    gdf = gpd.GeoDataFrame(stadiums, geometry=gpd.points_from_xy(stadiums.Latitude, stadiums.Longitude))
    gdf.crs = 'epsg:4326'

    # Remove Latitude/Longitude columns as they are have now been combined
    # into the geometry column.
    gdf = gdf.drop(['Latitude', 'Longitude'], axis=1)

    # Output the data frame to GeoJsON.
    gdf.to_file(output_filename, driver='GeoJSON')


INPUT_FILENAME = os.environ.get('INPUT', 1)
OUTPUT_FILENAME = os.environ.get('OUTPUT', 1)
if __name__ == '__main__':
    translate('/opt/resources/stadiums.csv', '/opt/resources/stadiums.geojson')
