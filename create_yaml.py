import os
import re
import argparse
import yaml

def create_yaml_file(yaml_file, output_dir):

    # Get a list of all fastq.gz files in the directory
    fastq_files = [filename for filename in os.listdir("./data") if filename.endswith(".fastq.gz")]

    # Extract prefixes from the file names
    fastq_prefixes = [re.search(r"(.+?)\.r[12]\.fastq\.gz", filename).group(1) for filename in fastq_files]

    # Create YAML data
    yaml_data = {
        "output_dir": output_dir,
        "packages": {
            "fastp": {
                "version": "0.12.4",
                "envs": "fastp_star.yaml"
            },
            "star": {
                "version": "2.7.10b",
                "envs": "fastp_star.yaml",
                "genome_dir": "/data/scratch/yaochung/ref/star/hg38"
            },
            "tetranscripts": {
                "version": "2.2.3",
                "envs": "TEcount.yaml",
                "gtf":"/data/scratch/yaochung/ref/hg38.ensGene.gtf",
                "rmsk":"/data/scratch/yaochung/ref/hg38_rmsk_TE.gtf.ind"
            }
        },
        "fastq_prefixes": fastq_prefixes
    }

    # Write YAML data to a file
    with open(yaml_file, "w") as f:
        yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False, indent=2)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Create YAML file with fastq prefixes")
    parser.add_argument("-yaml", "--yaml_file", required=True, help="Output YAML file")
    parser.add_argument("-outdir", "--output_dir", required=True, help="Output folder for saving results")
    args = parser.parse_args()

    # Create YAML file
    create_yaml_file(args.yaml_file, args.output_dir)

