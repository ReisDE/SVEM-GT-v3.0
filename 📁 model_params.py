# --- SVEM-GT v3.0 Final Model Parameters ---
# Estes são os coeficientes finais da Regressão Ridge (alpha=0.52) obtidos da análise LOFO-CV completa.
# O modelo generalizado é: Tc_pred = b0 + b1*eps_pct + b2*delta + b3*F_G_norm + b4*kappa_norm
# Features: [eps_pct, delta, F_G_norm, kappa_norm]

# Intercepto (b0) do modelo
INTERCEPT = 19.53

# Coeficientes do modelo (b1, b2, b3, b4)
COEFFICIENTS = {
    'eps_pct': -1.27,      # Coeficiente para Strain (eps_pct)
    'delta': 0.85,         # Coeficiente para Doping (delta)
    'F_G_norm': 12.45,     # Coeficiente para Geometria Quântica (F_G_norm)
    'kappa_norm': 5.11     # Coeficiente para Kappa (kappa_norm)
}

# Alpha de Regularização Ridge
RIDGE_ALPHA = 0.52
