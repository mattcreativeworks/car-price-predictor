# Car Price Predictor — Section 8 Deployment

## Setup (3 steps)

### Step 1 — Save model from notebook
Copy the code in `save_model_notebook_cell.py` into a new cell
at the end of your notebook and run it. It creates two files:
- `preprocessor.pkl`
- `gbr_model.pkl`

### Step 2 — Folder structure
Make sure all four files are in the same folder:
```
your_folder/
├── app.py
├── preprocessor.pkl
├── gbr_model.pkl
└── requirements.txt
```

### Step 3 — Run the app
Open a terminal in that folder and run:
```bash
pip install -r requirements.txt
streamlit run app.py
```
The app will open automatically at http://localhost:8501
