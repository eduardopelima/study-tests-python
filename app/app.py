from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

class Incremental:

    def __init__(self):
        print("servico iniciado")

    def execute_service(self):
        spark: SparkSession = SparkSession.builder \
            .appName("Sample Spark DataFrame") \
            .getOrCreate()

        data = [
            ("Alice", 25, "F"),
            ("Bob", 30, "M"),
            ("Cathy", 28, "F"),
            ("David", 35, "M")
        ]
        columns = ["Name", "Age", "Gender"]

        df: DataFrame = spark.createDataFrame(data, columns)

        df: DataFrame = df.select("Name").distinct()

        df_count: int = df.count()

        print(df_count)

        if df_count > 1:
            print("erro")
