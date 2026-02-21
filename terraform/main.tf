resource "aws_cloudformation_stack" "jenkinsiac" {
  name          = "jenkins-iac"
  template_body = file("${path.module}/template.yaml")

  parameters = {
    BucketName = "jenkins-bucket"
    JenkinsECRRepositoryName = "ecr-repository"
  }

  tags = {
    Environment = "local"
    ManagedBy  = "terraform"
  }
}
