# Splitting images into RGB channels

This is a simple script that takes the input images of eyes and splits them into three channels, namely Red, Green & Blue.

## Directory Structure

```text

├── Datasets
│   ├── Input
│   │   ├── MILD-DR
│   │   │   └── 20051020_43832_0100_PP.tif
│   │   └── NO-DR
│   │       └── 20051214_51211_0100_PP.tif
│   └── Output
├── README.md
└── src
    └── main.py
```

- There are two sample images in the input directory. The script will create the `Output` directory if it does not already exists.
- The images are also scaled down to `337 × 224 px` preserving the aspect ratio.

## Usage

### Create a virtual environment

> Assuming [`conda`](https://www.anaconda.com/products/individual#Downloads) is preinstalled and this repository is cloned / downloaded.

- Create an environment

```bash
conda create -n eye-defect python
```

- Install the dependencies

```bash
conda install --file requirements.txt
```

## Run the script

Run the following command from the project's root.

```bash
python src/main.py
```

## Outcome

### Input Image

![input_image](https://i.stack.imgur.com/hZlr9.jpg)

### Output Images

| Red | Green | Blue |
| :---: | :---: | :---: |
| ![op1](https://i.stack.imgur.com/0odOf.jpg) | ![op2](https://i.stack.imgur.com/G3SSB.jpg) | ![op3](https://i.stack.imgur.com/ZQ2NR.jpg) |
