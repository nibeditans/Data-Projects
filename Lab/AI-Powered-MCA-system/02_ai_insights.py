def generate_ai_insight(summary: dict) -> tuple:
    import requests
    import os

    api_key = "YOUR_API_KEY" # Replace your own API Key, I've just given a placeholder.😅

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    models = [
        "google/gemma-4-26b-a4b-it:free",
        "openai/gpt-oss-120b:free",
        "inclusionai/ling-2.6-flash:free",
        "openrouter/elephant-alpha"
    ]

    prompt = f"""
    You are a senior marketing analyst.

    Analyze the campaign performance data and provide:

    1. Key performance insights
    2. Interpretation of customer behavior
    3. Strategic recommendations to improve campaign effectiveness

    Focus on:
    - Conversion efficiency
    - Engagement quality
    - ROI optimization

    Avoid generic statements. Be specific and business-oriented.

    Data:
    {summary}
    """

    for model in models:
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        try:
            res_json = response.json()
        except:
            print("Invalid JSON response:", response.text)
            continue

        if "choices" in res_json:
            return model, res_json["choices"][0]["message"]["content"]
        else:
            print(f"Model {model} failed:", res_json)

    return None, "All models failed. Try again later."
