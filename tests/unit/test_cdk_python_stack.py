import json
import pytest

from aws_cdk import core
from cdk-python.cdk_python_stack import CdkPythonStack


def get_template():
    app = core.App()
    CdkPythonStack(app, "cdk-python")
    return json.dumps(app.synth().get_stack("cdk-python").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
