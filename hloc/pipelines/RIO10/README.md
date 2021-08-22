###  RIO10 dataset

## Installation

# IMPORTANT: in order to download RIO10, get download.py from the RIO10 website and put it into this directory
Example for Scene03
```bash
export dataset=datasets/rio10
python3 download.py -o dataset --type=kapture --id 3
tar -xvf $dataset/scene03/RIO10_scene03_mapping.tar.gz
tar -xvf $dataset/scene03/RIO10_scene03_validation.tar.gz
tar -xvf $dataset/scene03/RIO10_scene03_testing.tar.gz
```

## Pipeline

```bash
python3 -m hloc.pipelines.RIO10.pipeline
```
 master
