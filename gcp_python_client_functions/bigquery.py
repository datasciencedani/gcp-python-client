# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_bigquery.ipynb.

# %% auto 0
__all__ = ['query_to_df']

# %% ../nbs/00_bigquery.ipynb 8
from google.cloud import bigquery

# %% ../nbs/00_bigquery.ipynb 9
def query_to_df(
    project_id: str, # GCP project ID
    query_str: str, # String variable containing SQL Query
):
    """
    Perform a SQL query to BigQuery and save the results in a dataframe (gcloud authentication needed).
    """
    client = bigquery.Client(project_id)

    df = client.query(
        query_str,
    ).to_dataframe(create_bqstorage_client = True)

    return df
