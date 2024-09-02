from aws_cdk import(
    Stack,
    aws_lambda,
    aws_s3
)

from constructs import Construct

class ResourceStackOne(Stack):
    def __init__(self, scope : Construct, construct_id = str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # creating a lambda function resource
        # here aws_lambda is a module and Function is a class inside it which creates a lambda function for us.
        # And that's why we need to pass self while using this class.
        lambda_fn_resource = aws_lambda.Function(
            self,
            'lambda_fn_cdk_resource',
            function_name = 'lambda_fn_pipeline_1',
            runtime = aws_lambda.Runtime.PYTHON_3_12,
            code = aws_lambda.Code.from_asset('./lambda_code'),
            handler = "lambda_fn.lambda_fn"
        )
        # creating a s3 bucket as source bucket
        source_bucket = aws_s3.Bucket(
            self, 'my_source_bucket',
            versioned = True,
            bucket_name = 'source-bucket-git-cdk-pipeline-1',
            block_public_access = aws_s3.BlockPublicAccess.BLOCK_ALL
        )
