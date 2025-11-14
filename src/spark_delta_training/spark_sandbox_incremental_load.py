from delta import *
from delta.tables import *
from pyspark.sql import functions as F


def main() -> None:
    spark_builder = (
        SparkSession.builder.master("local[4]")
        .appName("spark sandbox incremental load")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )
    spark = configure_spark_with_delta_pip(spark_builder).getOrCreate()

    df = spark.createDataFrame(
        [("account 1", "2025-03-01"), ("account 2", "2025-03-01")],
        schema="id STRING, modified STRING",
    )
    print("existing:")
    df.show()

    path = "../../target/output-delta-account/"
    (
        df.write.format("delta")
        # .partitionBy("modified")
        .save(path)
    )

    new_data_df = spark.createDataFrame(
        [
            ("account 1", "2025-03-05"),  # new account 1
            ("account 2", "2025-01-01"),  # new account 2, but out-of-date
        ],
        schema="id STRING, modified STRING",
    ).withColumn("modified", F.to_date("modified"))
    print("new:")
    new_data_df.show()

    delta_df = DeltaTable.forPath(spark, path)
    (
        delta_df.alias("existing")
        .merge(new_data_df.alias("new"), "new.id = existing.id")
        .whenMatchedUpdateAll("new.modified > existing.modified")
        .whenNotMatchedInsertAll()
        .execute()
    )

    (spark.read.format("delta").load(path).show())


if __name__ == "__main__":
    main()
