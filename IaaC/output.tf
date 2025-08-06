output "ingestion_glue_job" {
  value = aws_glue_job.etl_job.name
}

output "transformation_glue_job" {
  value = aws_glue_job.etl_job.name
}

output "glue_crawler_name" {
  value = aws_glue_crawler.etl_crawler.name
}