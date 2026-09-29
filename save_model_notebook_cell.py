# ── SECTION 8.1 — SAVE MODEL ARTIFACTS ───────────────────────────────────────
# Run this cell in your notebook AFTER Section 7 completes.
# It saves the preprocessor pipeline and the best model to disk.
# Place the two .pkl files in the same folder as app.py before running Streamlit.

import joblib

# Save the fitted preprocessor pipeline (StandardScaler + OHE + TargetEncoder)
joblib.dump(preprocessor, "preprocessor.pkl")

# Save the best model — Gradient Boosting Regressor
joblib.dump(gb_best, "gbr_model.pkl")

print("Saved: preprocessor.pkl")
print("Saved: gbr_model.pkl")
print("\nCopy both files into the same folder as app.py")
print("Then run:  streamlit run app.py")
