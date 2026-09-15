# nf-core reportree

nf-core module wrapping [ReporTree](https://github.com/insapathogenomics/ReporTree), a surveillance-oriented tool for pathogen genetic cluster analysis and epidemiological data linkage.

## Overview

ReporTree is a flexible pipeline that facilitates the detection of genetic clusters and their linkage to epidemiological data. It obtains genetic clusters at any threshold level(s) of a tree, SNP or cg/wgMLST allele matrix, VCF files, sequence alignment, or distance matrix, and produces summary reports with statistics/trends for the derived genetic clusters.

This repository contains the nf-core module for ReporTree v2.6.1, including:
- Conda environment with all dependencies (biopython, cgmlst-dists, ete3, grapetree, numba, numpy, pandas, scikit-learn, snp-sites, treecluster, etc.)
- Docker container (`docker.io/murphygargantua-agent/reportree:2.6.1`)
- nf-core module process with proper input/output channels
- nf-test test files
- GitHub Actions workflow for automated testing
- Unit tests for module structure validation

## Usage

```groovy
include { REPORREE } from 'modules/nf-core/reportree'

reportree(
    meta: [ id: 'sample1', single_end: false ],
    metadata: file('data/metadata.tsv'),
    tree: file('data/tree.nwk'),
    output: 'reporTree_output'
)
```

## Repository structure

```
nfcore-reportree/
├── .github/
│   └── workflows/
│       └── nfcore-test.yml      # nf-core module tests on GitHub Actions
├── modules/
│   └── nf-core/
│       └── reportree/
│           ├── Dockerfile          # Custom Docker image with ReporTree
│           ├── environment.yml     # Conda environment
│           ├── main.nf             # Nextflow process definition
│           ├── meta.yml            # Module metadata (nf-core schema)
│           ├── modules.json        # Module metadata for nf-core tools
│           ├── .gitignore
│           ├── README.md           # Module documentation
│           └── tests/
│               ├── main.nf.test    # nf-test test cases
│               ├── nextflow.config # Test Nextflow config
│               └── test.yml        # Module test configuration
├── conf/
│   ├── base.config               # Base pipeline config
│   └── meta.yml                  # Pipeline metadata
├── tests/
│   ├── data/
│   │   └── reportree/
│   │       ├── test_metadata.tsv   # Minimal test metadata (from Lodhia et al. 2025, Zenodo:19120159)
│   │       ├── test_allele_profile.tsv  # Minimal test allele profile
│   │       └── test_partitions.tsv  # Minimal test partitions
│   └── test_module.py             # Unit tests for module structure
├── tests/config/nextflow.config    # nf-core test config
├── modules.json                  # Root-level module registry
├── CITATIONS.md
├── CHANGELOG.md
└── README.md
```

## Testing

### nf-core module tests
The GitHub Actions workflow at `.github/workflows/nfcore-test.yml` runs:
```bash
nf-core modules test reportree --dir .
```

### Unit tests
```bash
cd tests
python3 test_module.py
```
This validates the module structure, required files, and correct configuration.

## Test data

Minimal test data is provided under `tests/data/reportree/`. The metadata, allele profile, and partitions files are derived from the *Chlamydia trachomatis* cgMLST reference dataset (Lodhia et al. 2025, Zenodo: [10.5281/zenodo.19120159](https://doi.org/10.5281/zenodo.19120159)).

## Input types supported

- **metadata** (required): Metadata table in TSV format
- **tree** (optional): Newick tree for clustering
- **alignment** (optional): Sequence alignment for conversion to profile
- **vcf** (optional): VCF file for conversion to profile
- **variants** (optional): TSV with mutations per sample
- **distance_matrix** (optional): Pairwise distance matrix
- **partitions** (optional): Pre-computed partitions table
- **allele_profile** (optional): Allele/SNP profile matrix
- **sequences** (optional): Sequences for profile conversion

## Output files

- `metadata_w_partitions.tsv`: Metadata with cluster columns
- `partitions_summary.tsv`: Summary statistics for clusters
- `variable_summary.tsv`: Summary for grouping variables
- `partitions.tsv`: Genetic clusters at selected thresholds

## Citation

If you use ReporTree, please cite:
> Mixão V, Pinto M, Sobral D, Di Pasquale A, Gomes JP, Borges V (2023) ReporTree: a surveillance-oriented tool to strengthen the linkage between pathogen genetic clusters and epidemiological data. *Genome Medicine*. doi: [10.1186/s13073-023-01196-1](https://doi.org/10.1186/s13073-023-01196-1)

If you use the test data, please cite:
> Lodhia Z, et al. (2025) Advancing Chlamydia trachomatis genomic surveillance and research with a novel core-genome MLST (cgMLST) approach. Zenodo: [10.5281/zenodo.19120159](https://doi.org/10.5281/zenodo.19120159)

## License

GPL-3.0