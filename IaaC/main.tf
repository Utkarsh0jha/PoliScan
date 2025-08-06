resource "aws_s3_bucket" "tf_ingestion_bucket" {
  bucket = var.raw_parquet_bucket
}

resource "aws_s3_bucket" "tf_transformation_bucket" {
  bucket = var.bucket_final
}

resource "aws_glue_catalog_database" "tf_crawler_db" {
  name = "tf_crawler_db"
}



locals {
  glue_role_arn = "arn:aws:iam::951764799690:role/LabRole"
}


resource "aws_glue_job" "ingestion_glue_job" {
  name     = var.ingestion_glue_job
  role_arn = local.glue_role_arn

  command {
    name            = "ingestion_glue_job"
    script_location = var.script_ingestion_path
    python_version  = "3"
  }

  glue_version      = "4.0"
  number_of_workers = 2
  worker_type       = "G.1X"
}

resource "aws_glue_job" "transformation_glue_job" {
  name     = var.transformation_glue_job
  role_arn = local.glue_role_arn

  command {
    name            = "transformation_glue_job"
    script_location = var.script_transformation_path
    python_version  = "3"
  }

  glue_version      = "4.0"
  number_of_workers = 2
  worker_type       = "G.1X"
}
resource "aws_glue_crawler" "glue_crawler_name" {
  name          = var.glue_crawler_name
  role          = local.glue_role_arn
  database_name = aws_glue_catalog_database.tf_crawler_db.name

  s3_target {
    path = "s3://${aws_s3_bucket.tf_ingestion_bucket.bucket}/tf_parquet_data/"
  }

  s3_target {
    path = "s3://${aws_s3_bucket.tf_transformation_bucket.bucket}/tf_cleaned_data/"
  }

  depends_on = [
    aws_glue_job.ingestion_glue_job,
    aws_glue_job.transformation_glue_job
  ]
}


