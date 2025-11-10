# SVEM-GT v3.0

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17571608.svg)](https://doi.org/10.5281/zenodo.17571608)

Quick Tc predictor for superconductors using SVEM-GT v3.0 model.

##  Model Equation

Tc ≈ 19.53 − 1.27·ε_pct + 0.85·δ + 12.45·F(G)_norm + 5.11·κ_norm

Where:
- ε_pct: strain (%)
- δ: doping level
- F(G)_norm: normalized quantum geometry descriptor
- κ_norm: normalized kappa descriptor

##  Files

- `model_params.py`: Stores the final Ridge regression coefficients.
- `calculate_Tc.py`: A 3-line function to compute Tc from descriptors.
- `README.md`: This file.
- `LICENSE`: MIT License for open use and citation.

##  Validation

- R² = 0.81  
- RMSE (LOFO-CV) = 42.1 ± 8.5 K

##  Citation

If you use SVEM-GT v3.0 in your research, please cite:

Reis, D. E. dos R. (2025). *SVEM-GT: Strain-Vacancy Quantum-Geometric Law Unifying Five Superconducting Families via Multiplicative Strain-Vacancy Coupling*. Zenodo. https://doi.org/10.5281/zenodo.17571608

Full dataset, figures, and analysis available at Zenodo:  
[DOI 10.5281/zenodo.17567732](https://doi.org/10.5281/zenodo.17567732)

##  Suggested Use

```python
from calculate_Tc import calculate_Tc

Tc = calculate_Tc(strain_pct=1.2, doping=0.03, quantum_geometry=0.85, kappa=0.67)
print(f"Predicted Tc: {Tc:.2f} K")
