import numpy as np
import pandas as pd
import os

def generate_campaign_data(n_users=5000, random_state=42):
    np.random.seed(random_state)

    # -----------------------------
    # 1. User IDs
    # -----------------------------
    user_ids = np.arange(1, n_users + 1)

    # -----------------------------
    # 2. Customer Segments
    # -----------------------------
    segments = np.random.choice(
        ["high", "medium", "low"],
        size=n_users,
        p=[0.2, 0.5, 0.3]
    )

    # -----------------------------
    # 3. Engagement Score (based on segment)
    # -----------------------------
    engagement_score = []

    for seg in segments:
        if seg == "high":
            engagement_score.append(np.random.uniform(0.6, 1.0))
        elif seg == "medium":
            engagement_score.append(np.random.uniform(0.3, 0.7))
        else:
            engagement_score.append(np.random.uniform(0.0, 0.5))

    engagement_score = np.array(engagement_score)

    # -----------------------------
    # 4. Past Behavior
    # -----------------------------
    past_purchase_count = np.random.poisson(lam=3, size=n_users)

    avg_order_value = np.random.normal(loc=500, scale=100, size=n_users)
    avg_order_value = np.clip(avg_order_value, 100, None)  # no negative/too small values

    # -----------------------------
    # 5. Funnel Simulation
    # -----------------------------

    # Email Opened
    open_prob = engagement_score * 0.8
    email_opened = np.random.binomial(1, open_prob)

    # Clicked (only if opened)
    click_prob = engagement_score * 0.6
    clicked = np.random.binomial(1, click_prob) * email_opened

    # Converted (only if clicked)
    convert_prob = engagement_score * 0.5
    converted = np.random.binomial(1, convert_prob) * clicked

    # -----------------------------
    # 6. Revenue
    # -----------------------------
    revenue_multiplier = np.random.uniform(0.8, 1.2, size=n_users)
    revenue = converted * avg_order_value * revenue_multiplier

    # -----------------------------
    # 7. Campaign Cost
    # -----------------------------
    campaign_cost = np.full(n_users, 10)

    # -----------------------------
    # 8. Create DataFrame
    # -----------------------------
    df = pd.DataFrame({
        "user_id": user_ids,
        "segment": segments,
        "engagement_score": engagement_score,
        "past_purchase_count": past_purchase_count,
        "avg_order_value": avg_order_value,
        "email_opened": email_opened,
        "clicked": clicked,
        "converted": converted,
        "campaign_cost": campaign_cost,
        "revenue": revenue
    })

    return df


if __name__ == "__main__":
    df = generate_campaign_data()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(BASE_DIR, "data", "campaign_data.csv")
    df.to_csv(output_path, index=False)
