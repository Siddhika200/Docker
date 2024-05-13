provider "aws" {
  region = "us-east-2"
}

# S3 Bucket
resource "aws_s3_bucket" "bucket" {
  bucket = "siddhi-bucket"  # Use the actual name of your bucket
}

# RDS Instance
resource "aws_db_instance" "demo_instance" {
  identifier        = "my-rds-instance"
  allocated_storage = 20
  storage_type      = "gp2"
  engine            = "mysql"
  engine_version    = "5.7"
  instance_class    = "db.t3.micro"
  username          = "user"
  password          = "user123"
}

# ECR Repository
resource "aws_ecr_repository" "demo_repository" {
  name = "my-ecr-repository"
}
