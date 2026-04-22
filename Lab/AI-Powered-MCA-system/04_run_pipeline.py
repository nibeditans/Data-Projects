from data_simulation import generate_campaign_data
from metrics_extraction import extract_campaign_metrics
from ai_insights import generate_ai_insight
from fallback import generate_fallback_insight

import os

# 1. Generate Data
df = generate_campaign_data()

# 2. Extract Metrics
summary = extract_campaign_metrics(df)

# 3. Generate AI Insight
model_used, ai_output = generate_ai_insight(summary)

# 4. Fallback Handling
if model_used is None:
    ai_output = generate_fallback_insight(summary)
    model_used = "Fallback"

# 5. Print Output
print(f"\nModel used: {model_used}\n")
print(ai_output)

# 6. Save Output
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(BASE_DIR, "outputs", "sample_insight.txt")

with open("outputs/sample_insight.txt", "w", encoding="utf-8") as f:
    f.write(f"Model used: {model_used}\n\n")
    f.write(ai_output)

print("\nInsight saved to outputs/sample_insight.txt")
