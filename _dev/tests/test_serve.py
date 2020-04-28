import os
import sys
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parents[1]
os.chdir(PROJECT_PATH)
sys.path.insert(0, PROJECT_PATH)
from app import app
from staticpy import Context

with open("configs/base.yaml") as file:
    config = yaml.safe_load(file)

context = Context(**config["contexts"]["notes"])
print(context.page_content_map)


def test_serve():
    expected = {
        "/": 200,
        "/notes": 200,
        "/posts": 200,
    }
    actual = {}

    for url in expected.keys():
        with app.test_client() as c:
            response = c.get(url)
            actual[url] = response.status_code
    assert expected == actual
