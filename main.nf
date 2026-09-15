nextflow {}

// nf-core reportree pipeline
// This pipeline uses the nf-core reportree module for pathogen genetic cluster analysis
// via ReporTree. See modules/nf-core/reportree/README.md for usage details.

include { REPORREE } from 'modules/nf-core/reportree'

process {
    container = "docker.io/murphygargantua-agent/reportree:2.6.1"
}

params {
    modules_testdata_base_path = "$baseDir/tests/data"
}