import argparse
from databricks.sdk.runtime import spark
from spark_delta_training import taxis


def main():
    # Process command-line arguments
    parser = argparse.ArgumentParser(description="Databricks job with catalog and schema parameters")
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--schema", required=True)
    args = parser.parse_args()

    # Example: just find all taxis from a sample catalog
    taxis.find_all_taxis().show(5)


if __name__ == "__main__":
    main()
