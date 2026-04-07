# README - Statlog (Australian Credit Approval)

## Descripcion del dataset
Este dataset se usa para predecir si una solicitud de credito sera aprobada (`1`) o rechazada (`0`).
Incluye variables financieras y personales del solicitante.

## Objetivo del trabajo
Aplicar preprocesamiento y entrenar modelos para:
- minimizar el error,
- maximizar la precision,
- justificar resultados con metricas y graficos.

## Flujo realizado en el cuaderno
1. Carga y revision del dataset.
2. Division 75/25 (train/test).
3. Manejo de nulos (media/moda).
4. Normalizacion con `featureNormalize`.
5. Balanceo del conjunto de entrenamiento.
6. Entrenamiento de modelos:
   - Regresion lineal (referencia)
   - Clasificacion logistica (modelo principal)
7. Evaluacion con metricas y visualizaciones.

## Metricas usadas
- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusion
- AUC (curva ROC)

## Visualizaciones incluidas
- Convergencia del costo
- Comparacion de accuracy train/test
- Matriz de confusion
- Histograma de probabilidades
- Curva ROC

## Conclusion corta
En este problema binario, la clasificacion logistica es la opcion mas adecuada.
Da probabilidades interpretables y mejor rendimiento para decidir aprobacion o rechazo de credito.

---
SIS420 - Primer Parcial
