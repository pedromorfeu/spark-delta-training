from datetime import date, datetime

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StringType

X = "xxx"


@pandas_udf(StringType())
def to_upper(a: pd.Series, c: pd.Series) -> pd.Series:
    return c.str.upper() + a.astype("string") + X


def main() -> None:
    spark = (
        SparkSession.builder.master("local[4]").appName("spark sandbox").getOrCreate()
    )

    df = spark.createDataFrame(
        [
            (1, 2.0, "string1", date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
            (2, 3.0, "string2", date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
            (3, 4.0, "string3", date(2000, 3, 1), datetime(2000, 1, 3, 12, 0)),
        ],
        schema="a long, b double, c string, d date, e timestamp",
    )
    df.show()

    (df.select("a", to_upper(F.col("a"), F.col("c"))).show())


if __name__ == "__main__":
    main()
