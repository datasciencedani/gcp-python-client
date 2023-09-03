# GCP Python Client Reusable Functions

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install gcp_python_client_functions
```

## How to use

Example of `bigquery` methods:

``` python
from gcp_python_client_functions.bigquery import *

PROJECT = 'dz-learning-d'
QUERY = """
        SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = "TX"
        LIMIT 100
        """
df = query_to_df(PROJECT, QUERY)
df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | name       |
|-----|------------|
| 0   | Mary       |
| 1   | Roberta    |
| 2   | Marguerite |
| 3   | Katie      |
| 4   | Eunice     |
| ... | ...        |
| 95  | Rita       |
| 96  | Elida      |
| 97  | Billie     |
| 98  | Ida        |
| 99  | Elizabeth  |

<p>100 rows × 1 columns</p>
</div>
