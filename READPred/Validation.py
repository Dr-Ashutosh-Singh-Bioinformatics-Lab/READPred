# READ/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
     selected_genes = [
    'MUSK', 'NFE2L3', 'CDH3', 'GLP2R', 'NEBL', 'TESC', 'SALL4', 'CEMIP', 'GRIN2D', 'MDFI',
    'CEP72', 'COL7A1', 'TGFBI', 'SLC6A6', 'GPR12', 'HRK', 'STRA6', 'CGREF1', 'CBX8', 'TMEFF2',
    'NKD2', 'SST', 'SIM2', 'ESM1', 'FOXQ1', 'KRT80', 'KRT24', 'VSTM2A', 'FUT1', 'ETV4', 
    'CPNE7', 'NRXN1', 'OTOP3', 'OTOP2', 'DHRS7C', 'FAM180B', 'MIER1', 'PKHD1L1'
     ]

    # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"READ patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")

