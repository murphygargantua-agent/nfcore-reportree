import os
# Remove cache files/directories from the index
for path in ['.nextflow', '.nf-test']:
    if os.path.exists(path):
        os.system(f'git rm -r --cached --ignore-unmatch {path} >/dev/null 2>&1')