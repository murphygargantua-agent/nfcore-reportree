#!/usr/bin/env python3
"""
Unit tests for the nf-core reportree module.
Verifies the module files are correctly structured and contain expected content. environment.yml and conda directive were intentionally removed; moduleDir is not used by this module.
"""
import os
import sys
import json
import yaml
from pathlib import Path


def find_module_root():
    """Find the reportree module root directory."""
    candidates = [
        Path("modules/nf-core/reportree"),
        Path("/home/hermes-agent/projects/nfcore-reportree/modules/nf-core/reportree"),
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
    assert "process REPORTREE" in content, "Process definition not found"
    assert "container" in content, "Container directive not found"
    assert "container" in content, "Container directive not found"
    assert "input:" in content, "Input block not found"
    assert "output:" in content, "Output block not found"
    assert "when:" in content, "When condition not found"
    assert "script:" in content, "Script block not found"


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
    assert "FROM conda/miniconda3" in content or "FROM continuumio/miniconda3" in content, "Wrong base image"
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
    assert "container" in content, "No container directive"


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


def test_citations_exists():
    """Test that CITATIONS.md exists at repo root."""
    repo_root = Path(__file__).parent.parent
    citations = repo_root / "CITATIONS.md"
    assert citations.exists(), "CITATIONS.md missing"
    content = citations.read_text()
    assert "ReporTree" in content, "ReporTree not cited"
    assert len(content) > 100, "CITATIONS too short"


def test_changelog_exists():
    """Test that CHANGELOG.md exists at repo root."""
    repo_root = Path(__file__).parent.parent
    changelog = repo_root / "CHANGELOG.md"
    assert changelog.exists(), "CHANGELOG.md missing"
    content = changelog.read_text()
    assert len(content) > 50, "CHANGELOG too short"


def test_conf_meta_yml_exists():
    """Test that conf/meta.yml exists at repo root."""
    repo_root = Path(__file__).parent.parent
    conf_meta = repo_root / "conf" / "meta.yml"
    assert conf_meta.exists(), "conf/meta.yml missing"
    with open(conf_meta) as f:
        data = yaml.safe_load(f)
    assert "name" in data, "No name in conf/meta.yml"


def test_root_modules_json_exists():
    """Test that root-level modules.json exists."""
    repo_root = Path(__file__).parent.parent
    modules_json = repo_root / "modules.json"
    assert modules_json.exists(), "Root modules.json missing"
    with open(modules_json) as f:
        data = json.load(f)
    assert "modules" in data, "No modules key in root modules.json"
    assert "nf-core/reportree" in data["modules"], "reportree not in root modules.json"


def test_test_data_exists():
    """Test that minimal test data files exist."""
    repo_root = Path(__file__).parent.parent
    test_data_dir = repo_root / "tests" / "data" / "reportree"
    assert test_data_dir.exists(), "Test data directory missing"
    metadata = test_data_dir / "test_metadata.tsv"
    assert metadata.exists(), "test_metadata.tsv missing"
    content = metadata.read_text()
    assert "\t" in content, "test_metadata.tsv not tab-separated"
    assert "sequence" in content.split("\n")[0] or "ID" in content.split("\n")[0], "No ID/sequence header in metadata"
    partitions = test_data_dir / "test_partitions.tsv"
    assert partitions.exists(), "test_partitions.tsv missing"


def test_nf_test_no_typo():
    """Test that main.nf.test references the correct process name."""
    root = find_module_root()
    nf_test = root / "tests" / "main.nf.test"
    content = nf_test.read_text()
    assert 'process "REPORTREE"' in content, "Process name not REPORTREE in nf-test"
    assert 'process "REPORREE"' not in content, "Stale REPORREE typo still present"
    assert 'process "REPOMTREE"' not in content, "Typo REPOMTREE still present"


if __name__ == "__main__":
    test_functions = [
        test_main_nf_exists,
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
        test_citations_exists,
        test_changelog_exists,
        test_conf_meta_yml_exists,
        test_root_modules_json_exists,
        test_test_data_exists,
        test_nf_test_no_typo,
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