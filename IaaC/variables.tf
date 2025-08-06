variable "region" {
  default = "us-east-1"
}


variable "tf_script_bucket" {
  default = "tf-script-bucket"
}


variable "tf_parquet_bucket" {
  default = "tf-parquet-bucket"
}

variable "tf_cleaned_bucket" {
  default = "tf-cleaned-bucket"
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
  default = "s3://tf-script-bucket/ingestion/ingestion_job.py"
}

#declare a script path
variable "script_transformation_path" {
  default = "s3://tf-script-bucket/transformation/transformation_job.py"
}