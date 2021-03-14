import os
import sys
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parents[1]
os.chdir(PROJECT_PATH)
sys.path.insert(0, PROJECT_PATH)

from app import CONTEXTS


def test_build():
    expected = []
    actual = []

    for context in CONTEXTS.values():
        expected.extend(
            [
                str(path.relative_to(context.source_path).stem)
                for path in Path(context.source_path).glob("**/*")
            ]
        )
        actual.extend(
            [
                str(path.relative_to(context.content_dir).stem)
                for path in Path(context.content_dir).glob("**/*")
            ]
        )

    assert expected == actual
