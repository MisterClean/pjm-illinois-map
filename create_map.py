import geopandas as gpd
import matplotlib.pyplot as plt
import os
from pathlib import Path

def create_illinois_pjm_map():
    # Ensure data directory exists
    data_dir = Path(__file__).parent.parent / 'data'
    data_dir.mkdir(exist_ok=True)
    
    # Load the Independent System Operators shapefile
    iso_shapefile = data_dir / 'Independent_System_Operators.shp'
    if not iso_shapefile.exists():
        raise FileNotFoundError(
            f"PJM shapefile not found at {iso_shapefile}. "
            "Please download the shapefile from EIA and place it in the data directory."
        )
    
    gdf = gpd.read_file(iso_shapefile)

    # Load Illinois boundary from Census Cartographic Boundary Files (500k resolution)
    illinois_url = 'https://www2.census.gov/geo/tiger/GENZ2022/shp/cb_2022_us_state_500k.zip'
    states = gpd.read_file(illinois_url)
    gdf_illinois_boundary = states[states['STUSPS'] == 'IL']

    # Filter the data to include only features within Illinois' boundary
    gdf_illinois = gdf[gdf.geometry.intersects(gdf_illinois_boundary.unary_union)]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the Illinois boundary
    gdf_illinois_boundary.boundary.plot(ax=ax, color='black', linestyle='-', linewidth=1.5)

    # Plot the filtered data
    gdf_illinois.plot(ax=ax, alpha=0.5, color='blue')

    # Remove axis labels, ticks, and frame
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Set title
    plt.title('Outline of Illinois with PJM Territory Overlay')

    # Set the extent to match Illinois boundaries with minimal padding
    bounds = gdf_illinois_boundary.total_bounds
    plt.xlim(bounds[0] - 0.05, bounds[2] + 0.05)
    plt.ylim(bounds[1] - 0.05, bounds[3] + 0.05)

    plt.tight_layout()
    
    # Save the plot
    output_dir = Path(__file__).parent.parent / 'output'
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / 'illinois_pjm_map.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_illinois_pjm_map()
