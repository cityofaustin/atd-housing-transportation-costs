#!/usr/bin/env python
# coding: utf-8

[General]

    ##### Census API#####
    census_api = abc123

    ##### TIGER/LINE Shapefile: the links below can be updated on an annual basis based on your needs: https://www2.census.gov/geo/tiger/#####
    # Access shapefile of Texas state
    tx_state = https://www2.census.gov/geo/tiger/TIGER2019/STATE/tl_2019_us_state.zip

    # Access shapefile of Texas county
    tx_county = https://www2.census.gov/geo/tiger/TIGER2019/COUNTY/tl_2019_us_county.zip

    # Access shapefile of Texas census block groups
    tx_bgs = https://www2.census.gov/geo/tiger/TIGER2019/BG/tl_2019_48_bg.zip

    # Access shapefile of Texas cities
    tx_city = https://www2.census.gov/geo/tiger/TIGER2019/PLACE/tl_2019_48_place.zip

[Transit]

    ##### load CapMetro GTFS zipfile data #####
    capmetro_gtfs = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/capmetro_gtfs.zip

    ##### load CARTS stops information (Note: you need to enter your own directory path)#####
    carts_stops = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/carts_stops.txt


[Auto]

    ##### Read Production-Attaction (PA) Data #####
    HOV2PA = campo-pa/2015_HOV2PA.xlsx
    HOV3PA = campo-pa/2015_HOV3PA.xlsx
    SOV = campo-pa/2015_SOV_Trips.xlsx

    ##### Read CAMPO-TAZ shapefile #####
    taz = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/TAZ2045/TAZ2045.shp

    ##### Read the number of households at TAZ level #####
    hh = 2015_CAMPO_TAZ_HH.csv

    # Read the file of the distance between each production-attraction pair 
    distance = distance_taz.csv

    #####Read CES Interview Data #####
    ces= C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/intrvw19

    ##### Load state-level weights with the CES public-use microdata (PUMD)#####
    tx_wgt = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/txwgt19.xlsx

    ##### Load CAMPO all-purpose VMT/hh file (this one is calculated by "3.1 VMT for auto use" )#####
    vmt = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/VMT.csv

    
[HTcosts]

    #####import each dataframe created by previous notebooks (housing, transit, auto-use)#####
    housing =C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/housing.csv
    transit =C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/transit_cost.csv
    auto = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/autoexp.csv

    ##### Read COA H_T index #####
    coa_ht_costs =C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/H_Tcost.csv

    ##### Read CNT H_T index #####
    cnt_ht_costs = C:/Users/minyu/OneDrive - The University of Texas at Austin/Desktop/Jupyter/htaindex_data_blkgrps_48.csv
