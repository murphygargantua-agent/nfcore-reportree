FROM continuumio/miniconda3:latest

LABEL maintainer="Murphy Agent (murphygargantua-agent)"
LABEL description="ReporTree: pathogen genetic cluster analysis and epidemiological data linkage"

WORKDIR /app

# Install system dependencies and ReporTree via pip/conda in parallel
RUN conda install -c etetoolkit -c bioconda -c conda-forge -c defaults \
    biopython \
    cgmlst-dists \
    ete3 \
    grapetree \
    numba \
    numpy \
    pandas \
    scikit-learn \
    snp-sites \
    treecluster \
    zip \
    git \
    --yes

# Clone and install ReporTree
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
RUN reportree.py --version 2>&1 | head -1 || true

# Create working directory
RUN mkdir -p /app/work
WORKDIR /app/work