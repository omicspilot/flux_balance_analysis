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

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/fluxbalance-ecoli.git
cd fluxbalance-ecoli
```

Install required Python packages:

```bash
pip install cobra optlang matplotlib seaborn
```

Optional tools (for visualization, benchmarking, etc.):

```bash
pip install escher pandas
```

---

## 📁 Project Structure

```
fluxbalance-ecoli/
│
├── models/              # Genome-scale models (e.g., iJO1366.json)
├── notebooks/           # Jupyter notebooks for simulations and analyses
├── scripts/             # Python scripts for reusable code
├── results/             # Output files (plots, flux maps, logs)
├── README.md            # This file
└── requirements.txt     # Optional pip environment
```

---

## 🚀 Getting Started

### 1. Load a metabolic model

Example in Python:

```python
import cobra
model = cobra.io.load_json_model('models/iJO1366.json')
```

### 2. Run basic FBA

```python
solution = model.optimize()
print("Growth rate:", solution.objective_value)
```

### 3. Visualize fluxes (optional)

```python
import escher
from escher import Builder

builder = Builder(model=model, map_name='e_coli_core.Core metabolism')
builder.display_in_notebook()
```

---

## 📊 Example Results

- Biomass production on glucose minimal media
- Essential gene knockouts and their effect on growth
- Reaction flux ranges using FVA
- Visualization of central carbon metabolism

---

## 📚 References

- [COBRApy Documentation](https://cobrapy.readthedocs.io/)
- [BiGG Models Database](http://bigg.ucsd.edu/)
- [Orth et al., 2010. *A comprehensive genome-scale reconstruction of Escherichia coli metabolism.*](https://pubmed.ncbi.nlm.nih.gov/21988831/)

---

## 🧪 Future Extensions

- Optimize for metabolite production (e.g., ethanol, succinate)
- Add transcriptomic constraints (e.g., with GIMME, iMAT)
- Explore machine learning applications in metabolic modeling

---

## 👩‍🔬 Author

Developed by [Oumar Ndiaye](https://github.com/ndiayeoumar).

Feel free to open issues or submit pull requests to collaborate.
