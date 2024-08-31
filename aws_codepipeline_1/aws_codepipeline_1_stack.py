from aws_cdk import (
    Stack,
    Stage,
    Environment,
    pipelines,
    aws_codepipeline as codepipeline
)
from constructs import Construct
from resource_stack.resource_stack import ResourceStack

class DeployStage(Stage):
    def __init__(self, scope: Construct, id = str, env = Environment, **kwargs):
        super().__init__(scope, id, env = env, **kwargs)
        ResourceStack(self, 'ResourceStack', env = env, stack_name = 'resource-stack-deploy')

class AwsCodePipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id : str, **kwargs)-> None:
        super().__init__(scope, construct_id, **kwargs)

        git_input = pipelines.CodePipelineSource.connection(
            repo_string = 'pathakch/aws-codepipeline-1',
            branch = 'main',
            connection_arn = 'arn:aws:codestar-connections:ap-south-1:189508241034:connection/ad84cea1-90d1-46db-ba65-e51d642f3af7'
        )
        code_pipeline = codepipeline.Pipeline(
            self, "git-pipeline-1",
            pipeline_name = 'git-pipeline-1',
            cross_account_keys = False
        )

        synth_step = pipelines.ShellStep(
            id = 'Synth',
            install_commands = ['pip install -r requirements.txt'],
            commands = ['npx cdk synth'],
            input = git_input

        )

        pipeline = pipelines.CodePipeline(
            self,
            'Codepipeline-1',
            self_mutation = True,
            code_pipeline = code_pipeline,
            synth = synth_step
        )

        deployment_wave = pipeline.add_wave("DeploymentWave")
        deployment_wave.add_stage(DeployStage(
            self,
            'DeployStage',
            env = (Environment(account = '189508241034', region = 'ap-south-1'))
        ))