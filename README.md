# Illinois PJM Territory Map

This repository creates a map visualization of PJM's territory within Illinois using Python and GeoPandas.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/illinois-pjm-map.git
cd illinois-pjm-map
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required data:
   - Download the PJM shapefile from [EIA's website](https://www.eia.gov/maps/layer_info-m.php) and place it in the `data` directory
   - The script will automatically download the required Census boundary files

## Usage

Run the mapping script:
```bash
python src/create_map.py
```

This will generate a map showing the PJM territory within Illinois's boundaries.

## Data Sources
- PJM Territory Shapefile: U.S. Energy Information Administration (EIA)
- Illinois State Boundary: U.S. Census Bureau Cartographic Boundary Files

## Requirements
- Python 3.8+
- See requirements.txt for full dependencies

## License
MIT License
