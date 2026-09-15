#!/bin/bash
# Remove cache files from git history
git rm -r --cached --ignore-unmatch .nextflow .nf-test .nextflow.log 2>/dev/null || true
