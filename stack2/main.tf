provider "aws" {
  region = "us-west-2"
}

module "bedrock_kb" {
  source = "../modules/bedrock_kb"

  knowledge_base_name        = "my-bedrock-kb"
  knowledge_base_description = "Knowledge base connected to Aurora Serverless database"

  # Aurora Serverless connection details
  aurora_arn        = "arn:aws:rds:us-west-2:376004512398:cluster:my-aurora-serverless" 
  aurora_db_name    = "myapp"
  aurora_endpoint   = "my-aurora-serverless.cluster-chbxsixfstos.us-west-2.rds.amazonaws.com"
  aurora_table_name = "bedrock_integration.bedrock_kb"
  aurora_primary_key_field = "id"
  aurora_metadata_field    = "metadata"
  aurora_text_field        = "chunks"
  aurora_verctor_field     = "embedding"
  aurora_username   = "dbadmin"
  aurora_secret_arn = "arn:aws:secretsmanager:us-west-2:376004512398:secret:rds!cluster-c6cc2c3c-c1d4-4931-b268-4425ac736fcf-2qEAsj"

  # S3 bucket
  s3_bucket_arn = "arn:aws:s3:::bedrock-kb-376004512398"
}
