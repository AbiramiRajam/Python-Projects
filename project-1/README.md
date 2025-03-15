# Analyzing the Relationship Between GNI per Capita and Life Expectancy in selected Countries

## Overview
This project aims to analyze the relationship between GNI per capita, population, and life expectancy in selected countries, including Canada, China, Australia, Germany, Japan, South Africa, United States, United Kingdom, India, Brazil. By examining data over time, the project will identify trends and correlations between economic factors (GNI per capita) , population projections and life expectancy outcomes. 

---

---

## Table of Contents
1. [Data](#Data)
2. [Requirements](#Requirements) 
3. [Executive Summary](#Executive-summary)

---
## Data
data source (kaggle)

- '../data/gni_per_cap_atlas_method_con2021.csv'
- '../data/life_expectancy.csv'
- '../data/population.csv'
- '../data/cleaned_data.csv'



### Data Dictionary

|Feature|Type|Description|
|---|---|---|
|country|object|Country Name
|year|int|The specific calendar year 
|population|float|Total number of people in a country
|gni_per_capita|float|Average economic output per person in a country
|life_expectancy|float|Average lifespan of individuals in a country 



## Requirements

- A programming environment such as Jupyter Lab
- pandas
- numpy
- matplotlib.pyplot
- os

---

## Executive Summary

To analyze data over time for selected countries and to identify trends and correlations between economic factors (GNI per capita) , population projections and life expectancy outcomes. 

### Methods

To focus mainly on the last 30 years from 2001 to 2030 to understand the socio economic changes in major countries like Canada, China, Australia, Germany, Japan, South Africa, United States, United Kingdom, India, Brazil. These countries play a major role in population, Life expectancy and GDP. 

Years considered for Analysis - 2001 to 2030
Countries List - Canada, China, Australia, Germany, Japan, South Africa, United States, United Kingdom, India, Brazil. 

### Findings

Notable findings in this Analysis includes:

Deeper Analysis of Life expectancy,population and GNA Per Capita data shows over the years from 2001 to 2030 life expectancy increases and there is slight down fall in life expectancy in the year 2020,2021 and it shows life expectancy decreased due to COVID 19 breakdown irrespective of countries.

Similar trends can also be seen in GNI Per Capita as well and the reduction is due to the economic slowdown and major shut down. The graph highlights a steep increase in Australia GNI per Capita for the period between 2010 and 2014 and may be due to strong mining exports and global economic stabilization.

Population graph shows steep increase in population in India and China over last 30 years and India’s population will be projected to be top.

Finally when correlating between GNI Per Capita, Life Expectancy and Population there are few interested observations:

High population vs low GNI per capita shows negative correlation
High population vs low life expectancy shows negative life expectancy
Whereas the higher GNA Per capita corresponds to a higher life expectancy. In other words, there is a positive correlation.


