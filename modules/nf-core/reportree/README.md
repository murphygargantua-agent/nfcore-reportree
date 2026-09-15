# nf-core reportree module

nf-core module wrapping [ReporTree](https://github.com/insapathogenomics/ReporTree), a surveillance-oriented tool for pathogen genetic cluster analysis and epidemiological data linkage.

## Overview

ReporTree is a flexible pipeline that facilitates the detection of genetic clusters and their linkage to epidemiological data. It obtains genetic clusters at any threshold level(s) of a tree, SNP or cg/wgMLST allele matrix, VCF files, sequence alignment, or distance matrix, and produces summary reports with statistics/trends for the derived genetic clusters.

This module packages ReporTree v2.6.1 as an nf-core module, providing:
- Conda environment with all dependencies (biopython, cgmlst-dists, ete3, grapetree, numba, numpy, pandas, scikit-learn, snp-sites, treecluster, etc.)
- Docker container (`docker.io/murphygargantua-agent/reportree:2.6.1`)
- nf-core module process with proper input/output channels
- nf-test test files

## Usage

```groovy
include { REPORTREE } from 'modules/nf-core/reportree'

reportree(
    meta: [ id: 'sample1', single_end: false ],
    metadata: file('data/metadata.tsv'),
    tree: file('data/tree.nwk'),
    output: 'reporTree_output'
)
```

## Module structure

```
modules/nf-core/reportree/
├── Dockerfile          # Custom Docker image with ReporTree and all dependencies
├── environment.yml     # Conda environment (bioconda::reportree=2.6.1)
├── main.nf             # Nextflow process definition
├── meta.yml            # Module metadata (inputs, outputs, tool info)
├── modules.json        # nf-core modules metadata
├── .gitignore
└── tests/
    ├── main.nf.test    # nf-test test cases
    ├── nextflow.config # Test Nextflow config
    └── test.yml        # Module test configuration
```

## Citation

If you use ReporTree, please cite:
> Mixão V, Pinto M, Sobral D, Di Pasquale A, Gomes JP, Borges V (2023) ReporTree: a surveillance-oriented tool to strengthen the linkage between pathogen genetic clusters and epidemiological data. Genome Medicine. doi: 10.1186/s13073-023-01196-1

## License

GPL-3.0