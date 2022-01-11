# Rockspot Scraper

Status: POC, hacky

Example repo scraping the Brooklyn vital web counter to google sheets to track capacity over time.

This repo is deployed as a GCP Cloud Function, listening to a Pub/Sub topic. GCP Cloud Scheduler publishes to that topic, triggering a scrape. The scraper gets the data and uploads the new data to a specific google sheet. The scraper runs under a service account that has had the sheet shared with it.

Lots of this could be better and definitely isn't best practices, but it works for this use case. Also serves generally as a way to structure this type of pipeline.
