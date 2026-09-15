process REPORTREE {
    tag "${meta.id}"
    label 'process_medium'

    container "docker.io/murphygargantua-agent/reportree:2.6.1"

    input:
    tuple val(meta), path(metadata), path(allele_profile), path(partitions), path(tree), path(alignment), path(vcf), path(variants), path(distance_matrix), path(sequences)

    output:
    tuple val(meta), path("${prefix}_metadata_w_partitions.tsv"), emit: metadata_w_partitions
    tuple val(meta), path("${prefix}_partitions_summary.tsv"),     emit: partitions_summary, optional: true
    tuple val(meta), path("${prefix}_variable_summary.tsv"),       emit: variable_summary, optional: true
    tuple val(meta), path("${prefix}_partitions.tsv"),             emit: partitions, optional: true
    tuple val("${task.process}"), val('reportree'), eval('reportree.py --version 2>/dev/null | head -1'), emit: versions_reportree, topic: versions

    when:
    task.ext.when == null || task.ext.when

    script:
    prefix = task.ext.prefix ?: (meta.id ? "${meta.id}" : 'reportree_output')
    def metadata_path = metadata.toString()

    def allele_profile_cmd = allele_profile && allele_profile.toFile().length() > 0 ? "-a ${allele_profile}" : ''
    def partitions_cmd     = partitions     && partitions.toFile().length() > 0 ? "-p ${partitions}" : ''
    def tree_cmd           = tree           && tree.toFile().length() > 0 ? "-t ${tree}" : ''
    def alignment_cmd      = alignment      && alignment.toFile().length() > 0 ? "-align ${alignment}" : ''
    def vcf_cmd            = vcf            && vcf.toFile().length() > 0 ? "-vcf ${vcf}" : ''
    def variants_cmd       = variants       && variants.toFile().length() > 0 ? "-var ${variants}" : ''
    def distance_matrix_cmd= distance_matrix && distance_matrix.toFile().length() > 0 ? "-d_mx ${distance_matrix}" : ''
    def sequences_cmd      = sequences      && sequences.toFile().length() > 0 ? "-align ${sequences}" : ''

    // When tree is provided, ReporTree can only use metadata + tree + distance_matrix.
    def has_tree = tree && tree.toFile().length() > 0
    def use_allele_profile = has_tree ? '' : allele_profile_cmd
    def use_partitions = has_tree ? '' : partitions_cmd
    def use_tree = has_tree ? tree_cmd : ''
    def use_alignment = has_tree ? '' : alignment_cmd
    def use_vcf = has_tree ? '' : vcf_cmd
    def use_variants = has_tree ? '' : variants_cmd
    def use_distance_matrix = has_tree ? '' : (distance_matrix && distance_matrix.toFile().length() > 0 && !vcf ? distance_matrix_cmd : '')
    def use_sequences = has_tree ? '' : sequences_cmd

    def cmd = [
        'reportree.py',
        '-m ' + metadata_path,
        use_allele_profile,
        use_partitions,
        use_tree,
        use_alignment,
        use_vcf,
        use_variants,
        use_distance_matrix,
        use_sequences,
        '-out ' + prefix
    ].join(' ')
    """
    ${cmd}
    """

    stub:
    prefix = task.ext.prefix ?: (meta.id ? "${meta.id}" : 'reportree_output')
    """
    touch ${prefix}_metadata_w_partitions.tsv
    touch ${prefix}_partitions_summary.tsv
    touch ${prefix}_variable_summary.tsv
    touch ${prefix}_partitions.tsv
    """
}
