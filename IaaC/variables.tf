variable "region" {
  default = "us-east-1"
}

variable "raw_parquet_bucket" {
  default = "tf_ingestion_bucket"
}

variable "bucket_final" {
  default = "tf_transformation_bucket"
}

variable "ingestion_glue_job" {
  default = "tf_ingestion_glue_job"
}

variable "transformation_glue_job" {
  default = "tf_transformation_glue_job"
}


variable "glue_crawler_name" {
  default = "tf_automation_crawler"
}

#declare a script path
variable "script_ingestion_path" {
  default = "s3://tf_glue_automation/ingestion/ingestion_job.py"
}

#declare a script path
variable "script_transformation_path" {
  default = "s3://tf_glue_automation/transformation/transformation_job.py"
}