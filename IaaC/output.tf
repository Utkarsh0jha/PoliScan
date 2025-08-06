output "ingestion_glue_job" {
  value = aws_glue_job.ingestion_glue_job.name
}

output "transformation_glue_job" {
  value = aws_glue_job.transformation_glue_job.name
}

output "glue_crawler_name" {
  value = aws_glue_crawler.glue_crawler_name.name
}