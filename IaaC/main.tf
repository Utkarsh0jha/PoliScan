resource "aws_s3_bucket" "tf-script-bucket-uo" {
  bucket = var.tf-script-bucket-uo
}


resource "aws_s3_bucket" "tf-parquet-bucket-pc" {
  bucket = var.tf-parquet-bucket-pc
}


resource "aws_s3_bucket" "tf-cleaned-bucket-uo" {
  bucket = var.tf-cleaned-bucket-uo
}

resource "aws_glue_catalog_database" "tf_crawler_db" {
  name = "tf_crawler_db"
}



locals {
  glue_role_arn = "arn:aws:iam::968164097585:role/LabRole"
}


resource "aws_glue_job" "tf_ingestion_glue_job" {
  name     = var.tf_ingestion_glue_job
  role_arn = local.glue_role_arn

  command {
    name            = "glueetl"
    script_location = var.script_ingestion_path
    python_version  = "3"
  }

  glue_version      = "4.0"
  number_of_workers = 2
  worker_type       = "G.1X"
}

resource "aws_glue_job" "tf_transformation_glue_job" {
  name     = var.tf_transformation_glue_job
  role_arn = local.glue_role_arn

  command {
    name            = "glueetl"
    script_location = var.script_transformation_path
    python_version  = "3"
  }

  glue_version      = "4.0"
  number_of_workers = 2
  worker_type       = "G.1X"
}
resource "aws_glue_crawler" "tf_glue_crawler_name" {
  name          = var.glue_crawler_name
  role          = local.glue_role_arn
  database_name = aws_glue_catalog_database.pc

  s3_target {
    path = "s3://${aws_s3_bucket.tf-cleaned-bucket-uo.bucket}/final_master/"
  }
  depends_on = [
    aws_glue_job.tf_ingestion_glue_job,
    aws_glue_job.tf_transformation_glue_job
  ]
}



