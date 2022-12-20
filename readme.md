# Austin Comprehensive Housing and Transportation Cost Analysis Tool

Created for ATD By:
- Alex Karner, PhD
- Minyu Situ
- Gian-Claudia Sciara, PhD

Graduate Program in Community & Regional Planning
School of Architecture
The University of Texas at Austin

***

## Introduction

This series of python notebooks and datasets are intended to support the city's calculation of two main performance indicators categorizes as part of _Strategic Direction 2023_.

1. (EOA.C) Cost of living compared to income
2. (M.B) Transportation cost

## Data Sources

- American Community Survey 2015-2019 5-Year Estimates (2019 ACS)
- U.S. Census TIGER/Line and shapefiles
- Consumer Expenditure Surveys 
- Public Use Microdata (CES-PUMD) provides a variety of expenditures related to household income for auto ownership each year.
- General Transit Feed Specification data (GTFS) of the Capital Metropolitan Transportation Authority (CapMetro) contains transit route and schedule information for all fixed-route service (MetroBus lines, and MetroRail) in the CapMetro service region. 
- Capital Area Rural Transportation System (CARTS) transit stops: CARTS official website provides the particular addresses of bus stops in non-urbanized areas.
- National Transit Database (2019 NTD): NTD data is the repository of data in terms of the financial, asset, and operating conditions of transit systems across the United States. It provides yearly transit revenue of each transit agency nationwide.
- 2015 CAMPO trip data: CAMPO provides internal data on all-purpose trips at the Traffic Analysis Zone (TAZ) level. 

## Running these scripts

- Clone this repo
- Download the [CAMPO production-attraction files](https://atd-housing-transportation-costs.s3.amazonaws.com/campo-pa.zip) and extract the folder into your directory
- Download the [CES Interview Data](https://atd-housing-transportation-costs.s3.amazonaws.com/intrvw19.zip) and extract the folder into your directory
- Install [Jupyter Notebook](https://jupyter.org/install)
- Then, install the required packages in `requirement.txt` or you can run the provided `Install Package [first time user].ipynb` notebook to install the correct packages.
- Update `Config.py` to provide your [Census API key](https://api.census.gov/data/key_signup.html) and make appropriate changes so all directory paths are correct.
- Then, run the Jupyter notebooks in the correct order (labeled 1 through 6).