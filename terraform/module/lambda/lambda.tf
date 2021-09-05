# NOTE: Steps of deployment
# STEP1 - zip src directory.
# STEP2 - If zip file is updated (= has another hash), execute shell script which makes package for upload that contains third-party libraries.
# STEP3 - zip the package for upload.
# STEP4 - If zip file is updated (= has another hash), update a lambda function.
data "archive_file" "sample_without_third_party_packages" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/upload/lambda_without_third_party_packages.zip"
}

resource "null_resource" "prepare_package" {
  provisioner "local-exec" {
    command = "source ${path.module}/prepare_lambda_package.sh ${path.module}"
  }

  triggers = {
    src_updated = data.archive_file.sample_without_third_party_packages.output_base64sha256
  }
}

data "archive_file" "sample" {
  type        = "zip"
  source_dir  = "${path.module}/upload/prepare"
  output_path = "${path.module}/upload/lambda.zip"

  depends_on = [
    null_resource.prepare_package
  ]
}

resource "aws_lambda_function" "sample" {
  filename      = data.archive_file.sample.output_path
  function_name = "SampleFunction"
  role          = aws_iam_role.lambda_sample.arn
  handler       = "main.lambda_handler"

  source_code_hash = data.archive_file.sample.output_base64sha256

  runtime = "python3.9"

  environment {
    variables = {
      LOG_LEVEL = "INFO"
    }
  }

  timeout = 29
  publish = true
}
