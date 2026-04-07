import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import pyreadstat
from tqdm import tqdm

print("✅ Todas las librerías están instaladas y listas para el examen.")
print(f"✅ Versión de PyTorch: {torch.__version__}")
print(f"✅ Versión de Pandas: {pd.__version__}")

# Prueba rápida de tensor para confirmar que el motor matemático funciona
t = torch.tensor([1.2, 3.4])
print(f"✅ Prueba de Tensor exitosa: {t}")