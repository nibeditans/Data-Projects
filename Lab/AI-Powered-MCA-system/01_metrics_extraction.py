import pandas as pd

def extract_campaign_metrics(df: pd.DataFrame) -> dict:

    # 1. Campaign Performance
    total_users = len(df)

    open_rate = df["email_opened"].mean()
    click_rate = df["clicked"].mean()
    conversion_rate = df["converted"].mean()

    # 2. Customer Behavior
    avg_engagement = df["engagement_score"].mean()

    high_engagement_users = (df["engagement_score"] > 0.6).sum()
    low_engagement_users = (df["engagement_score"] < 0.3).sum()

    # 3. Financial Performance
    total_revenue = df["revenue"].sum()
    total_cost = df["campaign_cost"].sum()

    roi = (total_revenue - total_cost) / total_cost if total_cost != 0 else 0

    # 4. Build Summary Dict
    summary_dict = {
        "campaign_overview": {
            "total_users_targeted": total_users,
            "open_rate": round(open_rate, 3),
            "click_through_rate": round(click_rate, 3),
            "conversion_rate": round(conversion_rate, 3)
        },

        "customer_behavior": {
            "avg_engagement_score": round(avg_engagement, 3),
            "high_engagement_users": int(high_engagement_users),
            "low_engagement_users": int(low_engagement_users)
        },

        "financial_performance": {
            "total_revenue": round(total_revenue, 0),
            "revenue_per_user": total_revenue / total_users,
            "campaign_cost": round(total_cost, 0),
            "roi": round(roi, 2)
        }
    }

    return summary_dict


if __name__ == "__main__":

    from data_simulation import generate_campaign_data

    df = generate_campaign_data()
    summary = extract_campaign_metrics(df)
    print(summary)
