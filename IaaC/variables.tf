variable "region" {
  default = "us-east-1"
}


variable "tf-script-bucket-yc" {
  default = "tf-script-bucket-yc"
}


variable "tf-parquet-bucket-yc" {
  default = "tf-parquet-bucket-yc"
}

variable "tf-cleaned-bucket-yc" {
  default = "tf-cleaned-bucket-yc"
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
  default = "s3://tf-script-bucket-yc/ingestion/tf_ingestion_glue_job.py"
}

#declare a script path
variable "script_transformation_path" {
  default = "s3://tf-script-bucket-yc/transformed/tf_transformation_glue_job.py"
}