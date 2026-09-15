process REPORREE {
    tag "${meta.id}"
    label 'process_medium'

    conda "${moduleDir}/environment.yml"
    container "docker.io/murphygargantua-agent/reportree:2.6.1"

    input:
    tuple val(meta), path(metadata)
    tuple val(meta), path(tree)            , optional: true
    tuple val(meta), path(alignment)       , optional: true
    tuple val(meta), path(vcf)             , optional: true
    tuple val(meta), path(variants)        , optional: true
    tuple val(meta), path(distance_matrix) , optional: true
    tuple val(meta), path(partitions)      , optional: true
    tuple val(meta), path(allele_profile)  , optional: true
    tuple val(meta), path(sequences)       , optional: true
    val output             := "reporTree_output"
    val dist               := 1
    val method_threshold   := "all"
    val HCmethod_threshold := "all"
    val threshold          := 10
    val HCthreshold        := 10
    val n_obs              := 1000
    val AdjustedWallace    := 0
    val partitions2report  := "all"
    val grep_cluster_id    := false
    val clusters           := "all"
    val subsets            := false
    val subset_by          := ""
    val filter_column      := ""
    val columns_summary_report := "all"
    val frequency_matrix   := false
    val count_matrix       := false
    val pivot              := false
    val mx_transpose       := false
    val update_cluster_names := false
    val keep_redundants    := false
    val stability          := false
    val unzip              := false

    output:
    tuple val(meta), path("${output}/**"), emit: output
    tuple val("${task.process}"), val('reporree'), eval('reporree --version 2>&1 | head -1'), emit: versions_reporree, topic: versions

    when:
    task.ext.when == null || task.ext.when

    script:
    def args = task.ext.args ?: ''

    """
    reportree.py \\\\
        -m \"${metadata}\" \\\\
        -o \"${output}\" \\\\
        ${tree ? '-t "${tree}"' : ''} \\\\
        ${alignment ? '-a "${alignment}"' : ''} \\\\
        ${vcf ? '-v "${vcf}"' : ''} \\\\
        ${variants ? '-V "${variants}"' : ''} \\\\
        ${distance_matrix ? '-d "${distance_matrix}"' : ''} \\\\
        ${partitions ? '-p "${partitions}"' : ''} \\\\
        ${allele_profile ? '-P "${allele_profile}"' : ''} \\\\
        ${sequences ? '-s "${sequences}"' : ''} \\\\
        --dist "${dist}" \\\\
        --method-threshold "${method_threshold}" \\\\
        --HCmethod-threshold "${HCmethod_threshold}" \\\\
        --threshold "${threshold}" \\\\
        --HCthreshold "${HCthreshold}" \\\\
        --n-obs ${n_obs} \\\\
        --AdjustedWallace ${AdjustedWallace} \\\\
        --partitions2report "${partitions2report}" \\\\
        --grep-cluster-id ${grep_cluster_id} \\\\
        --clusters "${clusters}" \\\\
        --subsets ${subsets} \\\\
        --subset-by "${subset_by}" \\\\
        --filter-column "${filter_column}" \\\\
        --columns-summary-report "${columns_summary_report}" \\\\
        --frequency-matrix ${frequency_matrix} \\\\
        --count-matrix ${count_matrix} \\\\
        --pivot ${pivot} \\\\
        --mx-transpose ${mx_transpose} \\\\
        --update-cluster-names ${update_cluster_names} \\\\
        --keep-redundants ${keep_redundants} \\\\
        --stability ${stability} \\\\
        --unzip ${unzip} \\\\
        ${args}
    """

    stub:
    """
    mkdir -p ${output}
    touch ${output}/metadata_w_partitions.tsv
    touch ${output}/partitions_summary.tsv
    touch ${output}/variable_summary.tsv
    touch ${output}/partitions.tsv
    """
}