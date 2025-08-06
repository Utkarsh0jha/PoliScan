output "ingestion_glue_job" {
  value = aws_glue_job.tf_ingestion_glue_job.name
}

output "transformation_glue_job" {
  value = aws_glue_job.tf_transformation_glue_job.name
}

output "glue_crawler_name" {
  value = aws_glue_crawler.tf_glue_crawler_name.name
}