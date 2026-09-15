# Citations

## nf-core

If you use this nf-core module, please cite:

- The nf-core framework: [Ewels et al., 2020](https://doi.org/10.1038/s41592-019-0686-9)
  > Ewels P, Peltzer A, Fillinger S, et al. The nf-core framework for community-curated bioinformatics pipelines. *Nature Biotechnology* 2020;38:276-278.

## ReporTree

If you use ReporTree, please cite:

- Mixão V, Pinto M, Sobral D, Di Pasquale A, Gomes JP, Borges V (2023) ReporTree: a surveillance-oriented tool to strengthen the linkage between pathogen genetic clusters and epidemiological data. *Genome Medicine*. doi: [10.1186/s13073-023-01196-1](https://doi.org/10.1186/s13073-023-01196-1)

## Test data

The test data in `tests/data/reportree/` is derived from:

- Lodhia Z, Mixão V, Isidro J, Ferreira R, Cordeiro D, Correia C, João I, Gomes JP, Borrego MJ, Borges V (2025) Chlamydia trachomatis cgMLST schema and necessary resources for its implementation. Zenodo: [10.5281/zenodo.19120159](https://doi.org/10.5281/zenodo.19120159)

## Related tools

ReporTree relies on several external tools. Depending on which functionalities you use, you should also cite:

1. Grapetree: [http://www.genome.org/cgi/doi/10.1101/gr.232397.117](https://doi.org/10.1101/gr.232397.117) (if you requested a grapetree analysis)
2. TreeCluster: [Nandapati et al., 2020](https://doi.org/10.1016/j.crm.2020.02.007) (if you provided a newick tree)
3. vcf2mst: [Gusmao et al., 2021](https://doi.org/10.1186/s12864-021-08112-0) (if you provided a vcf or a list of variants)
4. ComparingPartitions: [Pinto et al., 2021](https://doi.org/10.1128/jcm.02536-05) (if you requested "stability_regions")
5. Ete3: [Herrera et al., 2016](https://doi.org/10.1093/molbev/msw046) (if you provided a newick tree)
6. cgmlst-dists: [Tseemann et al.](https://github.com/tseemann/cgmlst-dists) and [Gusmao et al.](https://github.com/genpat-it/cgmlst-dists)
7. snp-sites: [Turkisch et al., 2020](https://doi.org/10.1099/mgen.0.000056) (if you provided a multi-sequence alignment)
8. bioconda: [Bioconda](https://bioconda.github.io)