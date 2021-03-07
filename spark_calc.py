from pyspark import SparkContext, Row, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, DoubleType, IntegerType, DateType

# convert to internal mapping
schema = StructType().add("uid", StringType(), False).add("price", IntegerType(), False).add("transfer_date", DateType(), False)

price_file = "./tmp/pp-full.csv"

sc = SparkContext("local", "Simple App")
sc.setLogLevel("INFO")
ss = SparkSession(sc)
sqlc = SQLContext(sc)

df = sqlc.read.csv(price_file, schema=schema)
print(df.dtypes)

# file = sc.textFile(price_file)
# df = file.map(lambda r: Row(r))

print(df.groupby('transfer_date').count().show())

sc.stop()