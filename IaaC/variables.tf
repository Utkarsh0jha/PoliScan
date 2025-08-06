variable "region" {
  default = "us-east-1"
}


variable "tf-script-bucket-uo" {
  default = "tf-script-bucket-uo"
}


variable "tf-parquet-bucket-uo" {
  default = "tf-parquet-bucket-uo"
}

variable "tf-cleaned-bucket-uo" {
  default = "tf-cleaned-bucket-uo"
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
  default = "s3://tf-script-bucket-uo/ingestion/ingestion_job.py"
}

#declare a script path
variable "script_transformation_path" {
  default = "s3://tf-script-bucket-uo/transformation/transformation_job.py"
}