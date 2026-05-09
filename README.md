# AlphaFold pLDDT Analysis

### Automated Extraction of Protein Confidence Scores from PDB Structures

---

## Features

- Batch extraction of pLDDT scores from PDB files
- Automated structural confidence analysis
- AlphaFold-compatible workflow
- CSV-based result generation
- Lightweight structural bioinformatics utility

---

## Project Overview

This project presents a Python-based workflow for extracting and summarizing **pLDDT (Predicted Local Distance Difference Test)** confidence scores from protein structure PDB files.

The script parses structural files generated from tools such as:

* AlphaFold
* ColabFold

and computes:

* Average pLDDT score per protein structure

This enables rapid assessment of predicted protein structure reliability.

---

## Workflow

### 1. Input Processing

* Reads `.pdb` files from a specified directory
* Parses atomic coordinate records (`ATOM`)

---

### 2. pLDDT Extraction

* Extracts pLDDT values from the B-factor column
* Computes average confidence score for each structure

---

### 3. Output Generation

Results exported as:

```bash id="1xg9me"
plddt_scores.csv
```

containing:

* Protein ID
* Average pLDDT score

---

## 🗂️ Project Structure

```bash id="0k7mbd"
alphafold-plddt-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── extract_plddt.py
│
├── data/
│   └── sample_pdb/
│
└── results/
```

---

## Usage

### Install dependencies

```bash id="v3z4hp"
pip install -r requirements.txt
```

---

### Run analysis

```bash id="3m8qvs"
python src/extract_plddt.py
```

---

## Output

Generated CSV:

```bash id="2d7nxy"
plddt_scores.csv
```

---

## Scientific Relevance

pLDDT scores are widely used for:

* Assessing AlphaFold prediction confidence
* Structural bioinformatics analysis
* Protein structure quality evaluation
* Prioritizing reliable predicted models

---

## Notes

* Compatible with AlphaFold-generated PDB files
* Requires valid `.pdb` structural files

---

## Author

**Vanathi Shanmugam**
Bioinformatics | Genomics | Machine Learning

🔗 LinkedIn: https://www.linkedin.com/in/vanathi-shanmugam-26127928a

---

## License

Academic and research use only
