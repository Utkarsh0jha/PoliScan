variable "region" {
  default = "us-east-1"
}


variable "tf-script-bucket-uo" {
  default = "tf-script-bucket-uo"
}
variable "tf-parquet-bucket-pc" {
  default = "tf-parquet-bucket-pc"
}

variable "tf-cleaned-bucket-uo" {
  default = "tf-cleaned-bucket-uo"
}

variable "tf_ingestion_glue_job" {
  default = "tf_ingestion_glue_job"
}

variable "tf_transformation_glue_job" {
  default = "tf_transformation_glue_job"
}
 

variable "glue_crawler_name" {
  default = "tf_automation_crawler"
}

#declare a script path
variable "script_ingestion_path" {
  default = "s3://tf-script-bucket-uo/ingestion/tf_ingestion_glue_job.py"
}

#declare a script path
variable "script_transformation_path" {
  default = "s3://tf-script-bucket-uo/transformed/tf_transformation_glue_job.py"
}