# Reliable, Observable Toxic Air Polution Details

## A Data Challenge for YourStake 

Author:  Gregg Lind
Date:  Sun, Jun 13, 2021

## 1. Using the language and libraries of your choice, write code to produce a CSV of company names, amount of toxic air pollution, and description of details (e.g. facility locations, purpose of facility, names of chemicals released…).

See code in [./jobs/](./jobs/) folder.  

Complications to discuss:
- data dictionaries
- csv as an output format (and output structures)
- clarification of downstream consumer (format)
- scraping

## 2. Describe the steps you'd take to make your script robust enough to run unsupervised on a regular basis.

| Need | Example Soution |
| -----------                  | ----------- |
| Job scheduling with retry    | Amazon Cloudwatch + AWS Lambda scraping jobs.  Example: https://stackoverflow.com/questions/54496692/best-solution-to-retry-aws-lambda-function-when-it-got-timeout  |
| Observability and Monitoring | Amazon Cloudwatch
| Completion, Correctness      | Within job testing (See Question 3)


## 3. List of quality checks you would want to write when putting into web app, and bullet point outline of how.
 
### Terms:
- dataset: expected location and contents for the last downloaded data
- alarm:  record to a logging file of "possible errors", for example using Cloudwatch.
- configuration:  JSON or Yaml Resource configuration listing expectations for each job around size, freshness etc. 

### Overall Operational Plan for Quality Checking:

- a cloudwatched running lambda that does checks of hygeine, using the CONFIGURATION for each EXPECTED RESOURCE.
- do the check for each trait below.  Alarm on failures.
- in general, log stats from "check runs", like number of rows, filesize, file hash.

### 5 Pillars of Observability (from Monte Carlo Data)
https://www.montecarlodata.com/product/  
https://www.montecarlodata.com/introducing-the-5-pillars-of-data-observability/)

1. Freshness (Recency)
- dataset older than X days.  HEAD dataset url, and check for timestamp / freshness.  Alarm if "too old". 

2. Volume (Right Size.  Non-zero.)
- size.  GET dataset.  Alarm if "too few" rows.  

3. Distribution (Existance and Access)
- existence.  HEAD dataset url.  Alarm if not there.
- accessible at a url: "user with right permissions", check resource url.

4. Schema (Shape and Sense)
- fields are the right shape using jsonschema for that file.

5. Lineage (All subparts are good)
- for combined / derived data, a DAG that reflects how it was constructed.  Update and log freshness or breakage for any "source" data.  Warn that dataset might be corrupted.










