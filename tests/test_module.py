#!/usr/bin/env python3
"""
Unit tests for the nf-core reportree module.
Verifies the module files are correctly structured and contain expected content.
"""
import os
import sys
import json
import yaml
from pathlib import Path


def find_module_root():
    """Find the reportree module root directory."""
    # Try common locations
    candidates = [
        Path("modules/nf-core/reportree"),
        Path("/home/hermes-agent/nfcore-reportree/modules/nf-core/reportree"),
        Path(__file__).parent / "nfcore-reportree" / "modules" / "nf-core" / "reportree",
    ]
    for candidate in candidates:
        if candidate.exists() and (candidate / "main.nf").exists():
            return candidate
    raise FileNotFoundError("Could not find reportree module directory")


def test_main_nf_exists():
    """Test that main.nf exists and contains required elements."""
    root = find_module_root()
    main_nf = root / "main.nf"
    assert main_nf.exists(), "main.nf does not exist"
    content = main_nf.read_text()
    assert "process REPORREE" in content, "Process definition not found"
    assert "conda" in content, "Conda directive not found"
    assert "container" in content, "Container directive not found"
    assert "input:" in content, "Input block not found"
    assert "output:" in content, "Output block not found"
    assert "when:" in content, "When condition not found"
    assert "script:" in content, "Script block not found"


def test_environment_yml_exists():
    """Test that environment.yml exists and has correct channels."""
    root = find_module_root()
    env_yml = root / "environment.yml"
    assert env_yml.exists(), "environment.yml does not exist"
    with open(env_yml) as f:
        data = yaml.safe_load(f)
    assert "channels" in data, "No channels defined"
    assert "conda-forge" in data["channels"], "conda-forge channel missing"
    assert "bioconda" in data["channels"], "bioconda channel missing"
    assert "dependencies" in data, "No dependencies defined"


def test_meta_yml_exists():
    """Test that meta.yml exists and has required fields."""
    root = find_module_root()
    meta_yml = root / "meta.yml"
    assert meta_yml.exists(), "meta.yml does not exist"
    with open(meta_yml) as f:
        data = yaml.safe_load(f)
    assert "name" in data, "No name field"
    assert "description" in data, "No description field"
    assert "tools" in data, "No tools field"
    assert "input" in data, "No input field"
    assert "output" in data, "No output field"
    assert "authors" in data, "No authors field"
    assert "maintainers" in data, "No maintainers field"


def test_dockerfile_exists():
    """Test that Dockerfile exists and has correct base image."""
    root = find_module_root()
    dockerfile = root / "Dockerfile"
    assert dockerfile.exists(), "Dockerfile does not exist"
    content = dockerfile.read_text()
    assert "FROM conda/miniconda3" in content, "Wrong base image"
    assert "reportree" in content.lower(), "ReporTree not installed"
    assert "PATH" in content, "PATH not set"


def test_modules_json_exists():
    """Test that modules.json exists and is valid."""
    root = find_module_root()
    modules_json = root / "modules.json"
    assert modules_json.exists(), "modules.json does not exist"
    with open(modules_json) as f:
        data = json.load(f)
    assert data["name"] == "nf-core/reportree", "Wrong module name"
    assert "description" in data, "No description"
    assert "version" in data, "No version"


def test_tests_directory():
    """Test that tests directory has required files."""
    root = find_module_root()
    tests_dir = root / "tests"
    assert tests_dir.exists(), "tests directory does not exist"
    assert (tests_dir / "main.nf.test").exists(), "main.nf.test missing"
    assert (tests_dir / "nextflow.config").exists(), "nextflow.config missing"
    assert (tests_dir / "test.yml").exists(), "test.yml missing"


def test_main_nf_container_config():
    """Test that main.nf has correct container configuration."""
    root = find_module_root()
    main_nf = root / "main.nf"
    content = main_nf.read_text()
    assert "docker.io/murphygargantua-agent/reportree" in content, "Wrong container image"
    assert "moduleDir" in content, "moduleDir not used"


def test_main_nf_has_stub():
    """Test that main.nf has a stub block."""
    root = find_module_root()
    main_nf = root / "main.nf"
    content = main_nf.read_text()
    assert "stub:" in content, "No stub block"


def test_meta_yml_citation():
    """Test that meta.yml has citation information."""
    root = find_module_root()
    meta_yml = root / "meta.yml"
    with open(meta_yml) as f:
        data = yaml.safe_load(f)
    tools = data.get("tools", [])
    assert len(tools) > 0, "No tools defined"
    for tool in tools:
        if "reportree" in tool:
            assert "homepage" in tool["reportree"], "No homepage"
            assert "tool_dev_url" in tool["reportree"], "No tool_dev_url"
            assert "licence" in tool["reportree"], "No licence"


def test_gitignore_exists():
    """Test that .gitignore exists."""
    root = find_module_root()
    gitignore = root / ".gitignore"
    assert gitignore.exists(), ".gitignore does not exist"


def test_readme_exists():
    """Test that README.md exists and has content."""
    root = find_module_root()
    readme = root / "README.md"
    assert readme.exists(), "README.md does not exist"
    content = readme.read_text()
    assert len(content) > 100, "README too short"


def test_github_workflow_exists():
    """Test that GitHub Actions workflow exists."""
    repo_root = Path(__file__).parent.parent
    workflow_dir = repo_root / ".github" / "workflows"
    workflow_file = workflow_dir / "nfcore-test.yml"
    assert workflow_dir.exists(), ".github/workflows does not exist"
    assert workflow_file.exists(), "nfcore-test.yml workflow missing"


if __name__ == "__main__":
    test_functions = [
        test_main_nf_exists,
        test_environment_yml_exists,
        test_meta_yml_exists,
        test_dockerfile_exists,
        test_modules_json_exists,
        test_tests_directory,
        test_main_nf_container_config,
        test_main_nf_has_stub,
        test_meta_yml_citation,
        test_gitignore_exists,
        test_readme_exists,
        test_github_workflow_exists,
    ]
    passed = 0
    failed = 0
    for test_fn in test_functions:
        try:
            test_fn()
            print(f"  PASS: {test_fn.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL: {test_fn.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {test_fn.__name__}: {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed, {len(test_functions)} total")
    sys.exit(0 if failed == 0 else 1)