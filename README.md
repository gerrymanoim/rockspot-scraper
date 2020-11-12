# Rockspot Scraper

Status: POC, hacky

Example repo scraping the Boston rockspot web counter to google sheets to track capacity over time.

This repo is deployed as a GCP Cloud Function, listening to a Pub/Sub topic. GCP Cloud Scheduler publishes to that topic, triggering a scrape. The scraper gets the data and uploads the new data to a specific google sheet.

Lots of this could be better and definitely isn't best practices, but it works for this use case. Also serves generally as a way to structure this type of pipeline.
