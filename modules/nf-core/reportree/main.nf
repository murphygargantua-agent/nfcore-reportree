process REPORTREE {
    tag "${meta.id}"
    label 'process_medium'

    container "docker.io/murphygargantua-agent/reportree:2.6.1"

    input:
    tuple val(meta), path(metadata), path(allele_profile), path(partitions), path(tree), path(alignment), path(vcf), path(variants), path(distance_matrix), path(sequences)

    output:
    tuple val(meta), path("reporTree_output/**"), emit: output
    tuple val("${task.process}"), val('reporree'), eval('reporree --version 2>&1 | head -1'), emit: versions_reporree, topic: versions

    when:
    task.ext.when == null || task.ext.when

    script:
    """
    reportree.py \\
        -m "${metadata}" \\
        ${allele_profile ? '-P "${allele_profile:-}"' : ''} \\
        ${partitions ? '-p "${partitions:-}"' : ''} \\
        ${tree ? '-t "${tree:-}"' : ''} \\
        ${alignment ? '-a "${alignment:-}"' : ''} \\
        ${vcf ? '-v "${vcf:-}"' : ''} \\
        ${variants ? '-V "${variants:-}"' : ''} \\
        ${distance_matrix ? '-d "${distance_matrix:-}"' : ''} \\
        ${sequences ? '-s "${sequences:-}"' : ''} \\
        -o "reporTree_output" \\
        --dist 1 \\
        --method-threshold "all" \\
        --HCmethod-threshold "all" \\
        --threshold 10 \\
        --HCthreshold 10 \\
        --n-obs 1000 \\
        --AdjustedWallace 0 \\
        --partitions2report "all" \\
        --grep-cluster-id false \\
        --clusters "all" \\
        --subsets false \\
        --subset-by "" \\
        --filter-column "" \\
        --columns-summary-report "all" \\
        --frequency-matrix false \\
        --count-matrix false \\
        --pivot false \\
        --mx-transpose false \\
        --update-cluster-names false \\
        --keep-redundants false \\
        --stability false \\
        --unzip false
    """

    stub:
    """
    mkdir -p reporTree_output
    touch reporTree_output/metadata_w_partitions.tsv
    touch reporTree_output/partitions_summary.tsv
    touch reporTree_output/variable_summary.tsv
    touch reporTree_output/partitions.tsv
    """
}