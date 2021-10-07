import os
import geopandas as gpd

COLUMNS = ['Longitude', 'Latitude', ]

def translate(input_filename, output_filename):
    # Read the data file
    df = gpd.read_file(input_filename)

    # Verify `Longitude` and `Latitude` columns exist.
    for column in COLUMNS:
        assert (column in df.columns), f"{column} must be a column in the CSV file."

    # Create a new data frame with an extra column `geometry`, using the
    # `Latitude` and `Longitude` column as values.
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Latitude, df.Longitude))
    gdf.crs = 'epsg:4326'

    # Remove Latitude/Longitude columns as they are have now been combined
    # into the geometry column.
    gdf = gdf.drop(['Latitude', 'Longitude'], axis=1)

    # Output the data frame to GeoJsON.
    gdf.to_file(output_filename, driver='GeoJSON')


INPUT_FILENAME = os.environ.get('INPUT', 1)
OUTPUT_FILENAME = os.environ.get('OUTPUT', 1)
if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    translate('/opt/resources/stadiums.csv', '/opt/resources/stadiums.geojson')
    # translate(INPUT_FILENAME, OUTPUT_FILENAME)