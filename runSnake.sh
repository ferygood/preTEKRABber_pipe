#!/bin/bash
#SBATCH -J analysis
#SBATCH -D .
#SBATCH -o analysis.%j.out
#SBATCH --partition=<your-partition>
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=750M
#SBATCH --time=10-00:00:00
#SBATCH --mail-type=end
#SBATCH --mail-user=<your-email>

date
hostname

snakemake -s preTEKRABber.snake --configfile config.yaml --use-conda --cores 2
