# fluxbalance-ecoli

**Flux Balance Analysis of *Escherichia coli* metabolism using Python and COBRApy.**  
This project provides a Python-based pipeline to perform and analyze Flux Balance Analysis (FBA) on *E. coli*, leveraging the COBRApy library and curated genome-scale models.

---

## 📌 Project Goals

- Load and explore *E. coli* genome-scale metabolic models (e.g., iJO1366, iML1515)
- Simulate wild-type growth on minimal media
- Perform gene/reaction knockouts and assess impact on biomass production
- Conduct Flux Variability Analysis (FVA)
- Interpret metabolic behavior using literature-based insights
- Enable future extension toward metabolic engineering and omics integration

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/flux_balance_analysis.git
cd flux_balance_analysis
```

### 🔧 Set up the environment (recommended)

Using conda (recommended on macOS and Linux):

```bash
conda env create -f environment.yml
conda activate fluxbalance
```

---

## 📁 Project Structure

```
flux_balance_analysis/
│
├── models/              # Genome-scale models (e.g., iJO1366.json)
├── notebooks/           # Jupyter notebooks and Python scripts
├── results/             # Output files (plots, flux maps, logs)
├── README.md            # This file
└── requirements.txt     # Optional pip environment
└── environment.yml      # Conda environment file
```

---

## 🚀 Getting Started

### 1. Download a Metabolic Model

Run the [download script](./notebooks/0_introductory_exploration/0_download_model.py) to fetch a genome-scale model from the BiGG database. You will be prompted to choose which model to download.

```bash
python notebooks/0_introductory_exploration/0_download_model.py
```

### 2. Explore the Model

The `notebooks/` directory contains examples for analysis. Start with `1_model_summary.ipynb` to load your downloaded model and view its properties.

```bash
jupyter notebook notebooks/0_introductory_exploration/1_model_summary.ipynb
```

---

## 📊 Example Results

- Biomass production on glucose minimal media
- Essential gene knockouts and their effect on growth
- Reaction flux ranges using FVA
- Visualization of central carbon metabolism

---

## 📚 References

- [Introduction into genome.scale metabolic modelling](https://www.ebi.ac.uk/training/materials/symbnet-materials/from-mags-to-metabolic-modelling/introduction-into-genome-scale-metabolic-modelling-fba/?utm_source=chatgpt.com)
- [COBRApy Documentation](https://cobrapy.readthedocs.io/)
- [BiGG Models Database](http://bigg.ucsd.edu/)
- [Orth et al., 2010. *A comprehensive genome-scale reconstruction of Escherichia coli metabolism.*](https://pubmed.ncbi.nlm.nih.gov/21988831/)

---

## Future Extensions

- Optimize for metabolite production (e.g., ethanol, succinate)
- Add transcriptomic constraints (e.g., with GIMME, iMAT)
- Explore machine learning applications in metabolic modeling

---

## Author

Developed by [Oumar Ndiaye](https://github.com/ndiayeoumar).

Feel free to open issues or submit pull requests to collaborate.

