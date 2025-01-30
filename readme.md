### dbt profiles.yml
Ensure the `profiles.yml` file is configured to read/write the DuckDb file.

```yml
f1_analytics:
  outputs:
    prod:
      type: duckdb
      path: ~/Documents/code/f1-analytics/f1.db
      threads: 4

  target: prod
```
### Source Data
Credit to [f1db](https://github.com/f1db/f1db) for the source data of this project. Thanks!
