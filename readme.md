### dbt profiles.yml
Ensure the `profiles.yml` file is configured to read/write the DuckDb file.

```yml
f1_analytics:
  outputs:
    dev:
      type: duckdb
      path: /path_here/f1-analytics/f1_analytics/f1.duckdb
      threads: 4
      schema: dev

    prod:
      type: duckdb
      path: /path_here/f1-analytics/f1_analytics/f1.duckdb
      threads: 4

  target: prod
```
