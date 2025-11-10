import numpy as np
import pandas as pd
# Importa os coeficientes finais do modelo
from model_params import INTERCEPT, COEFFICIENTS

def calculate_tc_svem_gt(eps_pct, delta, F_G_norm, kappa_norm):
    """
    Calcula a Tc (Temperatura Crítica) usando o modelo SVEM-GT v3.0.
    """
    
    # 1. Monta os features na ordem definida: [eps_pct, delta, F_G_norm, kappa_norm]
    features = np.array([eps_pct, delta, F_G_norm, kappa_norm])
    
    # 2. Monta os pesos (coeficientes) na ordem correta
    weights = np.array([
        COEFFICIENTS['eps_pct'], 
        COEFFICIENTS['delta'], 
        COEFFICIENTS['F_G_norm'], 
        COEFFICIENTS['kappa_norm']
    ])
    
    # 3. CÁLCULO DA TC (A Lei SVEM-GT v3.0)
    Tc_predicted = INTERCEPT + np.dot(features, weights)
    
    return Tc_predicted

# --- EXEMPLO RÁPIDO PARA DEMONSTRAÇÃO ---

# Dados do YBCO (Cuprato, Tc_obs = 92 K) - Material de Referência
material_example = {
    "name": "Exemplo: YBCO (Cuprato)",
    "Tc_obs": 92.0,
    # Valores extraídos do zenodo_v3.0_data_final.csv
    "eps_pct": -0.8, 
    "delta": 0.07, 
    "F_G_norm": 1.117647,
    "kappa_norm": 1.145631 
}

# 1. Extrai os features
eps = material_example['eps_pct']
dop = material_example['delta']
fg = material_example['F_G_norm']
k = material_example['kappa_norm']

# 2. Calcula a Tc
Tc_pred = calculate_tc_svem_gt(eps, dop, fg, k)

# Imprime o resultado para o revisor
print(f"--- SVEM-GT v3.0 Quick Predictor ---")
print(f"Material: {material_example['name']}")
print(f"Tc Observada (K): {material_example['Tc_obs']:.2f} K")
print(f"Features: Strain={eps}%, Doping={dop}, F(G)={fg:.4f}, Kappa={k:.4f}")
print(f"Tc Prevista (K): {Tc_pred:.2f} K")
print(f"Erro (Previsão - Observada): {Tc_pred - material_example['Tc_obs']:.2f} K")
