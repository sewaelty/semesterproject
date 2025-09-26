import pandas as pd
import geopandas as gpd


def getCFs():
    """
    Reads the file for characterization factors (CFs) by ecoregion,
    prepares the data, and returns a pandas DataFrame.
    """

    filepath = "data/PDF/CF.csv"
    df_CF = pd.read_csv(filepath, delimiter=",", encoding="latin1")

    return df_CF


def getEcoregions():
    """
    Loads the ecoregions shapefile and performs basic inspections.
    """

    file_path = "data/ecoregions/official/wwf_terr_ecos.shp"
    df_ecoregions = gpd.read_file(file_path)

    return df_ecoregions


def getPolygonDatasetDescription():
    """
    Loads the polygon dataset description and prints its content.
    """

    file_path = "data/mining/maus/Maus-etal_2022_V2.tab"

    with open(file_path, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            print(f"Line {i + 1}: {line.strip()}")


def getMiningPolygons():
    """
    Loads the global mining polygons shapefile and performs basic inspections.
    """

    file_path = "data/mining/maus/global_mining_polygons_v2.gpkg"
    df_mining_polygons = gpd.read_file(file_path)

    return df_mining_polygons


def getMiningFacilities():
    """
    Loads the facilities GeoPackage and performs basic inspections.
    """

    gpkg_path = "data/mining/jasansky/data/facilities.gpkg"
    df_facilities = gpd.read_file(gpkg_path)

    return df_facilities


def getMiningMinerals():
    """
    Loads the minerals dataset and performs basic inspections.
    """

    minerals_path = "data/mining/jasansky/data/minerals.csv"
    df_minerals = pd.read_csv(minerals_path)

    return df_minerals


def getMiningCommodities():
    """
    Loads the commodities dataset and performs basic inspections.
    """

    commodities_path = "data/mining/jasansky/data/commodities.csv"
    df_commodities = pd.read_csv(commodities_path)

    return df_commodities


def getMaterialIDs():
    """
    Loads the material IDs dataset and performs basic inspections.
    """

    material_ids_path = "data/mining/jasansky/data/material_ids.csv"
    df_material_ids = pd.read_csv(material_ids_path)

    return df_material_ids


def getSourceIDs():
    """
    Loads the source IDs dataset and performs basic inspections.
    """

    source_ids_path = "data/mining/jasansky/data/source_ids.csv"
    df_source_ids = pd.read_csv(source_ids_path)

    return df_source_ids
