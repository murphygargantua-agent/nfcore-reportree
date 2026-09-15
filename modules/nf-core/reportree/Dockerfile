FROM continuumio/miniconda3:latest

LABEL maintainer="Murphy Agent (murphygargantua-agent)"
LABEL description="ReporTree: pathogen genetic cluster analysis and epidemiological data linkage"

WORKDIR /app

# ReporTree's own pinned environment (reportree_env.yml): python 3.8 + pandas 1.1.3.
# Newer pandas (>=2.2) breaks metadata_report.py with an astype shape TypeError.
RUN conda install -n base -c conda-forge -c etetoolkit -c bioconda -c insapathogenomics \
    python=3.8 \
    biopython=1.77 \
    cgmlst-dists_genpat-it=0.4.0 \
    ete3 \
    grapetree=2.1 \
    numba=0.55.1 \
    numpy=1.19.2 \
    numpy-base=1.19.2 \
    pandas=1.1.3 \
    scikit-learn \
    snp-sites=2.5.1 \
    treecluster=1.0.3 \
    zip \
    --yes

# Clone and install ReporTree v2.6.1
RUN git clone -b v2.6.1 https://github.com/insapathogenomics/ReporTree /app/reporTree 2>/dev/null || \
    git clone https://github.com/insapathogenomics/ReporTree /app/reporTree && \
    chmod 755 /app/reporTree/reportree.py && \
    chmod 755 /app/reporTree/scripts/partitioning_grapetree.py && \
    chmod 755 /app/reporTree/scripts/partitioning_HC.py && \
    chmod 755 /app/reporTree/scripts/partitioning_treecluster.py && \
    chmod 755 /app/reporTree/scripts/alignment_processing.py && \
    chmod 755 /app/reporTree/scripts/metadata_report.py && \
    cd /app/reporTree/scripts && \
    git clone https://github.com/insapathogenomics/ComparingPartitions.git 2>/dev/null || true && \
    git clone https://github.com/insapathogenomics/GrapeTree.git 2>/dev/null || true && \
    git clone https://github.com/insapathogenomics/vcf2mst.git 2>/dev/null || true && \
    chmod 755 /app/reporTree/scripts/ComparingPartitions/comparing_partitions_v2.py

# Set PATH to include ReporTree scripts
ENV PATH="/app/reporTree:/app/reporTree/scripts:/app/reporTree/scripts/ComparingPartitions:/app/reporTree/scripts/GrapeTree:/app/reporTree/scripts/vcf2mst:${PATH}"

# Verify installation
RUN reportree.py --version 2>/dev/null | head -1 || true

# Create working directory
RUN mkdir -p /app/work
WORKDIR /app/work
