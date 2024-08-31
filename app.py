import aws_cdk as cdk
from aws_codepipeline_1.aws_codepipeline_1_stack import AwsCodePipelineStack

app = cdk.App()
AwsCodePipelineStack(
    app,
    'AwsCodePipelineStack_1',
    env = cdk.Environment(account = '189508241034', region = 'ap-south-1'),
    stack_name = 'github-codepipeline-stack-1'
)
app.synth()