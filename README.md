# Ontario Wildlife Sightings Pipeline

An end-to-end data engineering project that ingests public wildlife observation
data and weather data, models it in a lakehouse, and serves a dashboard.

## Problem statement
How do wildlife sightings in Ontario change by season, region, and weather,
and which species are showing unusual shifts?

## Architecture
_Diagram goes here (docs/architecture.png)._

Ingest (Python) -> Bronze (raw) -> Silver (cleaned) -> Gold (star schema) -> Power BI

## Data sources
- GBIF occurrence API (includes iNaturalist research-grade observations)
- Open-Meteo historical weather API
- eBird (planned)

## Tech stack
Python, SQL, Databricks, Power BI

## Project structure
- `ingestion/`      API clients and raw loads
- `transform/`      SQL / notebooks for silver and gold layers
- `tests/`          data quality checks
- `orchestration/`  scheduled workflow definitions
- `docs/`           diagrams, data dictionary, design decisions
- `dashboard/`      Power BI file and screenshots

## How to run
_To be filled in as the pipeline is built._

## Key design decisions
_Why this model, why incremental loads, what trade-offs were made._

## Results
_Dashboard screenshots and findings._
