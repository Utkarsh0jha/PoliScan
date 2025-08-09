import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, when, upper, substring, to_date, trim, regexp_replace
)
from pyspark.sql.types import DoubleType

# Initialize Spark and Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Schemas
contribution_paths = ["s3://tf-parquet-bucket-uo/CI_CD(CSV+TO+PARQUET)/contribution/"]
committee_paths = ["s3://tf-parquet-bucket-uo/CI_CD(CSV+TO+PARQUET)/committee/"]
candidate_paths = ["s3://tf-parquet-bucket-uo/CI_CD(CSV+TO+PARQUET)/candidate/"]

# Read Parquet Files
df_contribution = spark.read.parquet(*contribution_paths)
df_committee = spark.read.parquet(*committee_paths)
df_candidate = spark.read.parquet(*candidate_paths)

# Deduplicate on Primary Keys
df_committee = df_committee.dropDuplicates(["CMTE_ID"])
df_candidate = df_candidate.dropDuplicates(["CAND_ID"])

# Join DataFrames
contrib_committee_df = df_contribution.join(
    df_committee,
    df_contribution["CMTE_ID"] == df_committee["CMTE_ID"],
    "inner"
)

final_master_df = contrib_committee_df.join(
    df_candidate,
    contrib_committee_df["CAND_ID"] == df_candidate["CAND_ID"],
    "inner"
)

final_master_df = final_master_df.select(
    df_contribution["*"],
    df_committee["CMTE_PTY_AFFILIATION"].alias("committee_party_affiliation"),
    df_candidate["CAND_PTY_AFFILIATION"].alias("CAND_PARTY_AFFILIATION")
)

# Fill and transform columns
df = final_master_df.withColumn(
    "MEMO_CD",
    when(col("MEMO_CD").isNull(), "I").otherwise(col("MEMO_CD"))
).withColumn(
    "OTHER_ID",
    when(col("OTHER_ID").isNull(), "Individual").otherwise(col("OTHER_ID"))
).withColumn(
    "MEMO_TEXT",
    when(col("MEMO_TEXT").isNull(), "Unknown").otherwise(col("MEMO_TEXT"))
).fillna({
    "EMPLOYER": "Unknown",
    "OCCUPATION": "Unknown"
})

df_all = df.withColumn(
    "AMNDT_IND",
    when(col("AMNDT_IND") == "N", "NEW")
    .when(col("AMNDT_IND") == "A", "AMENDMENTED")
    .when(col("AMNDT_IND") == "T", "TERMINATE")
    .otherwise(col("AMNDT_IND"))
).withColumn(
    "ENTITY_TP",
    when(col("ENTITY_TP") == "CCM", "CANDIDATE COMMITTEE")
    .when(col("ENTITY_TP") == "COM", "COMMITTEE")
    .when(col("ENTITY_TP") == "IND", "INDIVIDUAL")
    .when(col("ENTITY_TP") == "ORG", "ORGANIZATION")
    .when(col("ENTITY_TP") == "PAC", "POLITICAL ACTION COMMITTEE")
    .when(col("ENTITY_TP") == "PTY", "PARTY ORGANIZATION")
    .when(col("ENTITY_TP") == "CAN", "CANDIDATE")
    .when(col("ENTITY_TP").isNull(), "UNDISCOVERED")
    .otherwise(col("ENTITY_TP"))
)

df_all = df_all.withColumn("ENTITY_TP", upper(col("ENTITY_TP")))

# Correct parentheses in STATE mapping
df_all = df_all.withColumn(
    "STATE",
    upper(
        when(col("STATE") == "AL", "Alabama")
        .when(col("STATE") == "AK", "Alaska")
        .when(col("STATE") == "AZ", "Arizona")
        .when(col("STATE") == "AR", "Arkansas")
        .when(col("STATE") == "CA", "California")
        .when(col("STATE") == "CO", "Colorado")
        .when(col("STATE") == "CT", "Connecticut")
        .when(col("STATE") == "DE", "Delaware")
        .when(col("STATE") == "FL", "Florida")
        .when(col("STATE") == "GA", "Georgia")
        .when(col("STATE") == "HI", "Hawaii")
        .when(col("STATE") == "ID", "Idaho")
        .when(col("STATE") == "IL", "Illinois")
        .when(col("STATE") == "IN", "Indiana")
        .when(col("STATE") == "IA", "Iowa")
        .when(col("STATE") == "KS", "Kansas")
        .when(col("STATE") == "KY", "Kentucky")
        .when(col("STATE") == "LA", "Louisiana")
        .when(col("STATE") == "ME", "Maine")
        .when(col("STATE") == "MD", "Maryland")
        .when(col("STATE") == "MA", "Massachusetts")
        .when(col("STATE") == "MI", "Michigan")
        .when(col("STATE") == "MN", "Minnesota")
        .when(col("STATE") == "MS", "Mississippi")
        .when(col("STATE") == "MO", "Missouri")
        .when(col("STATE") == "MT", "Montana")
        .when(col("STATE") == "NE", "Nebraska")
        .when(col("STATE") == "NV", "Nevada")
        .when(col("STATE") == "NH", "New Hampshire")
        .when(col("STATE") == "NJ", "New Jersey")
        .when(col("STATE") == "NM", "New Mexico")
        .when(col("STATE") == "NY", "New York")
        .when(col("STATE") == "NC", "North Carolina")
        .when(col("STATE") == "ND", "North Dakota")
        .when(col("STATE") == "OH", "Ohio")
        .when(col("STATE") == "OK", "Oklahoma")
        .when(col("STATE") == "OR", "Oregon")
        .when(col("STATE") == "PA", "Pennsylvania")
        .when(col("STATE") == "RI", "Rhode Island")
        .when(col("STATE") == "SC", "South Carolina")
        .when(col("STATE") == "SD", "South Dakota")
        .when(col("STATE") == "TN", "Tennessee")
        .when(col("STATE") == "TX", "Texas")
        .when(col("STATE") == "UT", "Utah")
        .when(col("STATE") == "VT", "Vermont")
        .when(col("STATE") == "VA", "Virginia")
        .when(col("STATE") == "WA", "Washington")
        .when(col("STATE") == "WV", "West Virginia")
        .when(col("STATE") == "WI", "Wisconsin")
        .when(col("STATE") == "WY", "Wyoming")
        .when(col("STATE") == "DC", "District of Columbia")
        .when(col("STATE") == "PR", "Puerto Rico")
        .when(col("STATE") == "VI", "U.S. Virgin Islands")
        .when(col("STATE") == "GU", "Guam")
        .when(col("STATE") == "AS", "American Samoa")
        .when(col("STATE") == "MP", "Northern Mariana Islands")
        .when(col("STATE") == "UM", "U.S. Minor Outlying Islands")
        .when(col("STATE") == "FM", "Federated States of Micronesia")
        .when(col("STATE") == "MH", "Marshall Islands")
        .when(col("STATE") == "PW", "Palau")
        .when(col("STATE") == "AA", "Armed Forces Americas")
        .when(col("STATE") == "AE", "Armed Forces Europe")
        .when(col("STATE") == "AP", "Armed Forces Pacific")
        .when(col("STATE") == "ZZ", "Unknown / Foreign")
        .when(col("STATE") == "XX", "Unknown")
        .when(col("STATE") == "U*", "Unknown U.S. State")
        .otherwise("Other / Unknown")
    )
)
 
# Fill remaining nulls
df_all = df_all \
    .withColumn("ZIP_CODE", when(col("ZIP_CODE").isNull(), "ANONYMOUS").otherwise(col("ZIP_CODE"))) \
    .withColumn("committee_party_affiliation",
                when(col("committee_party_affiliation").isNull(), "UNRECOGNIZE").otherwise(
                    col("committee_party_affiliation"))) \
    .withColumn("MEMO_CD", when(col("MEMO_CD").isNull(), "I").otherwise(col("MEMO_CD"))) \
    .withColumn("OTHER_ID", when(col("OTHER_ID").isNull(), "INDIVIDUAL").otherwise(col("OTHER_ID")))

df_all = df_all.fillna({
    "EMPLOYER": "UNKNOWN",
    "OCCUPATION": "UNKNOWN",
    "CITY": "UNIDENTIFIED",
    "MEMO_TEXT": "ANONYMOUS",
    "NAME": "UNIDENTIFIED"
})

df_clean = df_all.filter(
    (col("TRANSACTION_DT").isNotNull()) & (trim(col("TRANSACTION_DT")) != "")
).withColumn(
    "committee_party_affiliation",
    when(col("committee_party_affiliation") == ".", "UNDEFINED")
    .otherwise(col("committee_party_affiliation"))
).withColumn(
    "CAND_PARTY_AFFILIATION",
    when(col("CAND_PARTY_AFFILIATION").isNull(), "UNDEFINED").otherwise(col("CAND_PARTY_AFFILIATION"))
)

dataf = df_clean.withColumn("RPT_TP",
                            when(col("RPT_TP").isin("12P", "12G", "12C", "12R", "12S"), "PRE-ELECTION")
                            .when(col("RPT_TP").isin("30G", "30P", "30D", "30R", "30S", "60D"), "POST-ELECTION")
                            .otherwise("OTHER")
                            ).withColumn(
    "ELECTION_TP",
    when(substring("TRANSACTION_PGI", 1, 1) == "P", "Primary")
    .when(substring("TRANSACTION_PGI", 1, 1) == "G", "General")
    .when(substring("TRANSACTION_PGI", 1, 1) == "R", "Runoff")
    .when(substring("TRANSACTION_PGI", 1, 1) == "S", "Special")
    .when(substring("TRANSACTION_PGI", 1, 1) == "C", "Convention")
    .when(substring("TRANSACTION_PGI", 1, 1) == "E", "Recount")
    .when(substring("TRANSACTION_PGI", 1, 1) == "O", "Other")
    .otherwise("Unknown")
).withColumn("ELECTION_YEAR", substring("TRANSACTION_PGI", 2, 4))

df_final = dataf.drop("TRANSACTION_PGI").withColumn(
    "ELECTION_YEAR",
    when(
        col("ELECTION_YEAR").isNull() | (trim(col("ELECTION_YEAR")) == ""),
        "UNKNOWN"
    ).otherwise(col("ELECTION_YEAR"))
).withColumn(
    "TRANSACTION_DT",
    to_date("TRANSACTION_DT", "MMddyyyy")
)

# Ensure type cast for year filter
df_final = df_final.filter(
    (year(col("TRANSACTION_DT")) >= 2013) & (year(col("TRANSACTION_DT")) <= 2025)
).drop("MEMO_TEXT").filter(col("TRANSACTION_DT").isNotNull()).withColumn(
    "transaction_amt", col("transaction_amt").cast("double")
).withColumn(
    "CONTRIBUTION_AMT",
    when(col("transaction_amt") > 0, col("transaction_amt")).otherwise(None)
).withColumn(
    "REFUND_AMT",
    when(col("transaction_amt") < 0, -col("transaction_amt")).otherwise(None)
).na.fill({"CONTRIBUTION_AMT": 0, "REFUND_AMT": 0}).drop("transaction_amt")

df_final = df_final.withColumn(
    "committee_party_affiliation",
    regexp_replace(
        regexp_replace("committee_party_affiliation", r"\(I\)", "UNDEFINED"),
        r"\.", "UNDEFINED"
    )
).withColumnRenamed("committee_party_affiliation", "COMMITTEE_PARTY_AFFILIATION")

# Cast ELECTION_YEAR before comparing
filtered_df = df_final.filter(
    (col("ELECTION_YEAR").cast("int") >= 2013) & (col("ELECTION_YEAR").cast("int") <= 2025)
)

df_with_unknown = filtered_df.withColumn(
    "ELECTION_YEAR",
    when((col("ELECTION_YEAR").cast("int") >= 2000) & (col("ELECTION_YEAR").cast("int") <= 2012), "UNKNOWN")
    .when((col("ELECTION_YEAR").cast("int") >= 2026) & (col("ELECTION_YEAR").cast("int") <= 2030), "UNKNOWN")
    .otherwise(col("ELECTION_YEAR"))
)

final_df = df_with_unknown.filter(
    (col("ELECTION_YEAR") == "UNKNOWN") |
    ((col("ELECTION_YEAR").cast("int") >= 2013) & (col("ELECTION_YEAR").cast("int") <= 2025))
)

df = final_df.withColumn(
    "COMMITTEE_PARTY_AFFILIATION",
    when(col("COMMITTEE_PARTY_AFFILIATION").isin("REP", "DEM", "IND", "DFL"),
         col("COMMITTEE_PARTY_AFFILIATION"))
    .otherwise("OTHERS")
).withColumn(
    "ENTITY_TP",
    when(col("ENTITY_TP").isin("INDIVIDUAL", "CANDIDATE", "POLITICAL ACTION COMMITTEE"),
         col("ENTITY_TP"))
    .otherwise("OTHERS")
).withColumn(
    "ELECTION_TP",
    when(col("ELECTION_TP").isin("Primary", "General", "Runoff", "Special"),
         col("ELECTION_TP"))
    .otherwise("OTHERS")
)

# Write output
df.coalesce(1).write.option("compression", "snappy").mode("overwrite").parquet("s3://tf-cleaned-bucket-uo/final_master/") 
