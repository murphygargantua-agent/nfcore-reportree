#!/usr/bin/env python3
"""Stub reportree.py for nf-test local profile.

Simulates ReporTree output file generation so that nf-test can verify
the nf-core module wiring without needing the full ReporTree installation
or a Docker container.
"""
import os
import sys

def main():
    args = sys.argv[1:]
    metadata = None
    out_prefix = "reporTree_output"
    params = {}

    i = 0
    while i < len(args):
        a = args[i]
        if a in ("-m", "--metadata"):
            metadata = args[i+1]
            i += 2
        elif a in ("-out", "--out"):
            out_prefix = args[i+1]
            i += 2
        elif a.startswith("--"):
            # Handle params like --loci-called, --analysis, etc.
            key = a.replace("--", "").replace("-", "_")
            params[key] = True
            i += 1
        else:
            i += 1

    out_dir = os.path.dirname(out_prefix) or "."
    base = os.path.basename(out_prefix)

    os.makedirs(out_dir, exist_ok=True)

    # Write metadata_w_partitions
    with open(os.path.join(out_dir, f"{base}_metadata_w_partitions.tsv"), "w") as f:
        f.write("sequence\tcluster_1\tcluster_2\tcluster_3\n")
        if metadata:
            with open(metadata) as mf:
                for line in mf:
                    parts = line.rstrip("\n").split("\t")
                    if parts and parts[0] != "sequence":
                        f.write(f"{parts[0]}\tcluster_1\tcluster_2\tcluster_3\n")
        else:
            f.write("A_2497\tcluster_1\tcluster_2\tcluster_3\n")

    # Write partitions_summary
    with open(os.path.join(out_dir, f"{base}_partitions_summary.tsv"), "w") as f:
        f.write("cluster\tnum_members\tmin_dist\tmax_dist\n")
        f.write("cluster_1\t2\t0.0\t1.0\n")

    # Write variable_summary
    with open(os.path.join(out_dir, f"{base}_variable_summary.tsv"), "w") as f:
        f.write("variable\tcategory\tcluster_counts\n")

    # Write partitions
    with open(os.path.join(out_dir, f"{base}_partitions.tsv"), "w") as f:
        f.write("sequence\tcluster_1\tcluster_2\tcluster_3\n")
        f.write("A_2497\tcluster_1\tcluster_2\tcluster_3\n")

if __name__ == "__main__":
    main()
