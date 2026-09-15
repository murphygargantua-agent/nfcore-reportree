FROM conda/miniconda3:4.12.0

LABEL maintainer="Murphy Agent (murphygargantua-agent)"
LABEL description="ReporTree: pathogen genetic cluster analysis and epidemiological data linkage"

WORKDIR /app

# Install system dependencies and conda packages
RUN conda install -c etetoolkit -c anaconda -c bioconda -c conda-forge -c defaults \
    biopython=1.77 \
    cgmlst-dists=0.4.0 \
    ete3=3.1.2 \
    grapetree=2.1 \
    numba=0.55.1 \
    numpy=1.19.2 \
    numpy-base=1.19.2 \
    pandas=1.1.3 \
    python=3.8.18 \
    scikit-learn=1.0.2 \
    snp-sites=2.5.1 \
    treecluster=1.0.3 \
    zip=3.0 \
    pytest=7.4.4 \
    git=2.40.1 \
    --yes

# Clone and install ReporTree
RUN git clone -b v2.6.1 https://github.com/insapathogenomics/ReporTree /app/reporTree && \
    chmod 755 /app/reporTree/reportree.py && \
    chmod 755 /app/reporTree/scripts/partitioning_grapetree.py && \
    chmod 755 /app/reporTree/scripts/partitioning_HC.py && \
    chmod 755 /app/reporTree/scripts/partitioning_treecluster.py && \
    chmod 755 /app/reporTree/scripts/alignment_processing.py && \
    chmod 755 /app/reporTree/scripts/metadata_report.py && \
    cd /app/reporTree/scripts && \
    git clone https://github.com/insapathogenomics/ComparingPartitions.git && \
    git clone https://github.com/insapathogenomics/GrapeTree.git && \
    git clone https://github.com/insapathogenomics/vcf2mst.git && \
    chmod 755 /app/reporTree/scripts/ComparingPartitions/comparing_partitions_v2.py

# Set PATH to include ReporTree scripts
ENV PATH="/app/reporTree:/app/reporTree/scripts:/app/reporTree/scripts/ComparingPartitions:/app/reporTree/scripts/GrapeTree:/app/reporTree/scripts/vcf2mst:${PATH}"

# Verify installation
RUN reportree.py --version 2>&1 | head -1 || true

# Create working directory
RUN mkdir -p /app/work
WORKDIR /app/work