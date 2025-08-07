from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Initialize the job with a static name
job = Job(glueContext)
job.init('ingestion_glue_job')
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, IntegerType


contribution_schema = StructType([
    StructField("CMTE_ID", StringType(), True),
    StructField("AMNDT_IND", StringType(), True),
    StructField("RPT_TP", StringType(), True),
    StructField("TRANSACTION_PGI", StringType(), True),
    StructField("IMAGE_NUM", StringType(), True),
    StructField("TRANSACTION_TP", StringType(), True),
    StructField("ENTITY_TP", StringType(), True),
    StructField("NAME", StringType(), True),
    StructField("CITY", StringType(), True),
    StructField("STATE", StringType(), True),
    StructField("ZIP_CODE", StringType(), True),
    StructField("EMPLOYER", StringType(), True),
    StructField("OCCUPATION", StringType(), True),
    StructField("TRANSACTION_DT", StringType(), True),
    StructField("TRANSACTION_AMT", DoubleType(), True),
    StructField("OTHER_ID", StringType(), True),
    StructField("TRAN_ID", StringType(), True),
    StructField("FILE_NUM", LongType(), True),
    StructField("MEMO_CD", StringType(), True),
    StructField("MEMO_TEXT", StringType(), True),
    StructField("SUB_ID", LongType(), False)
])

committee_schema = StructType([
    StructField("CMTE_ID", StringType(), True),
    StructField("CMTE_NAME", StringType(), True),
    StructField("CMTE_TRES_NM", StringType(), True),
    StructField("CMTE_ST1", StringType(), True),
    StructField("CMTE_ST2", StringType(), True),
    StructField("CMTE_CITY", StringType(), True),
    StructField("CMTE_ST", StringType(), True),
    StructField("CMTE_ZIP", StringType(), True),
    StructField("CMTE_DSGN", StringType(), True),
    StructField("CMTE_TP", StringType(), True),
    StructField("CMTE_PTY_AFFILIATION", StringType(), True),
    StructField("CMTE_FILING_FREQ", StringType(), True),
    StructField("ORG_TP", StringType(), True),
    StructField("CONNECTED_ORG_NM", StringType(), True),
    StructField("CAND_ID", StringType(), True)
])

candidate_schema = StructType([
    StructField("CAND_ID", StringType(), False),
    StructField("CAND_NAME", StringType(), True),
    StructField("CAND_PTY_AFFILIATION", StringType(), True),
    StructField("CAND_ELECTION_YR", IntegerType(), True),
    StructField("CAND_OFFICE_ST", StringType(), True),
    StructField("CAND_OFFICE", StringType(), True),
    StructField("CAND_OFFICE_DISTRICT", StringType(), True),
    StructField("CAND_ICI", StringType(), True),
    StructField("CAND_STATUS", StringType(), True),
    StructField("CAND_PCC", StringType(), True),
    StructField("CAND_ST1", StringType(), True),
    StructField("CAND_ST2", StringType(), True),
    StructField("CAND_CITY", StringType(), True),
    StructField("CAND_ST", StringType(), True),
    StructField("CAND_ZIP", StringType(), True)
])

input_path_contribution = ["s3://poliscandata/Contribution By Ind. Data/part-00000-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv",
                           "s3://poliscandata/Contribution By Ind. Data/part-00001-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv",
                           "s3://poliscandata/Contribution By Ind. Data/part-00002-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv",
                           "s3://poliscandata/Contribution By Ind. Data/part-00003-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv",
                           "s3://poliscandata/Contribution By Ind. Data/part-00004-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv",
                           "s3://poliscandata/Contribution By Ind. Data/part-00005-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv",
                           "s3://poliscandata/Contribution By Ind. Data/part-00006-1890e79d-5e29-4109-b09f-5787abe0d43d-c000.csv"]
input_path_committee    = ["s3://transformationpratham/commitie master/cm-13-14.txt",
                           "s3://transformationpratham/commitie master/cm-21-22.txt",
                           "s3://transformationpratham/commitie master/cm-23-24.txt",
                           "s3://transformationpratham/commitie master/cm15-16.txt",
                           "s3://transformationpratham/commitie master/cm17-18.txt",
                           "s3://transformationpratham/commitie master/cm19-20.txt",
                           "s3://transformationpratham/commitie master/cm25-26.txt"]
input_path_candidate    = ["s3://candidatemaster/cm/cn14.txt",
                           "s3://candidatemaster/cm/cn16.txt",
                           "s3://candidatemaster/cm/cn18.txt",
                           "s3://candidatemaster/cm/cn20.txt",
                           "s3://candidatemaster/cm/cn22.txt",
                           "s3://candidatemaster/cm/cn24.txt",
                           "s3://candidatemaster/cm/cn26.txt"]

df_contribution = spark.read.option("delimiter", "|").schema(contribution_schema).csv(*input_path_contribution)
df_committee    = spark.read.option("delimiter", "|").schema(committee_schema).csv(*input_path_committee)
df_candidate    = spark.read.option("delimiter", "|").schema(candidate_schema).csv(*input_path_candidate)

df_contribution.write.mode("overwrite").parquet("s3://tf-parquet-bucket-uo/CI_CD(CSV+TO+PARQUET)/contribution/")
df_committee.write.mode("overwrite").parquet("s3://tf-parquet-bucket-uo/CI_CD(CSV+TO+PARQUET)/committee/")
df_candidate.write.mode("overwrite").parquet("s3://tf-parquet-bucket-uo/CI_CD(CSV+TO+PARQUET)/candidate/")

 
# Finish the job 
job.commit()
print("✅ Glue job completed successfully.")
 