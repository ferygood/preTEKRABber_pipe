# preTEKRABber pipeline

## Intro
This pipeline is to generate genes and transposable elements (TEs) from `fastq.gz` paired-end files. Pipeline includes steps:
1. Use [fastp](https://github.com/OpenGene/fastp) to remove low quality reads and trimmed adapters
2. Use [STAR](https://github.com/alexdobin/STAR) to align reads to reference genome
3. Use [TEtranscripts](https://github.com/mhammell-laboratory/TEtranscripts) to quantify the expression of genes and transposable elements

The output will be saved inside a newly created folder `./results` after running the snakemake pipeline. The count table, which has the suffix `.cntTable` will be used for down-stream analysis using [TEKRABber](http://www.bioconductor.org/packages/release/bioc/html/TEKRABber.html).

## How to use
1. Install conda, and create a conda environment that can run snakemake (v7.25.0).
2. Clone this repository to your working directory
3. In this clone-repo, create a `data/` folder that you put all of your fastq.gz files in it
4. Use the `create_yaml.py` script to create a config file for snakemake to run
```python
python create_yaml.py -outdir <your_out_put_dir_path> -yaml <your_config_yaml_file_name>
```

5. If we want to execute snakemake in your command line, you can:
```bash
snakemake -s preTEKRABber.snake --configfile your-config.yaml -c 1
```
   
   If you prefer to run it in cluster, for example, using slurm, you can modified the `runSnake.sh` script and then:
```bash
sbatch runSnake.sh
```
6. The results will be saved inside a new create folder `./results` in this repo.

## Package version
A more detailed package version can be found in the yml files inside the `envs/` repo.
In brief:
```bash
snakemake==7.25.0
fastp==0.12.4
star==2.7.10b
tetranscripts==2.2.3
```

## Others
1. `envs` folder has the conda env setting for packages
2. `others` folder has some modified substracted snakefiles from the `preTEKRABber.snake` for certain usage. It is recommend that you start from the `preTEKRABber.snake`.

