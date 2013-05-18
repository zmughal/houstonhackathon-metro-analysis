import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = SCRIPT_DIR+"/../output"

ALL_GTFS_PATHS = {"Metro": SCRIPT_DIR+"/../data/metro"}

# Census
CENSUS_API_KEY = "0fb7d284f78fedba230921e4555494556f248c9f"
MEDIAN_INCOME_TABLE_NAME = 'B01002_001E'

# Skip some MUNI bus routes
MUNI_ALLOWED_ROUTE_SHORT_NAMES = []
