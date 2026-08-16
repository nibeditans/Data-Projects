# Airline Payment Fraud Decision Intelligence System

Airlines process a large number of payment transactions every day. A payment system needs to balance two problems:
1. Approving fraudulent transactions
2. Interrupting legitimate customers unnecessarily

I built this project to estimate the probability that an airline payment transaction is fraudulent and use that risk score to support a practical payment decision.

The project goes beyond a simple fraud classification model. I built a complete workflow:

> Data → Fraud Risk Prediction → Model Interpretation → Risk Assessment → Payment Decision

The final system can be used through a Streamlit application where a user can enter transaction details, receive a fraud probability, see the risk level, and understand the factors influencing the prediction.

For more details, refer to the original repo: [Airline Payment Fraud Decision Intelligence System](https://github.com/nibeditans/Airline-Payment-Fraud-Decision-Intelligence-System)

Also check out the article I have written on this Project:

Complete Project Walkthrough: [How I Built an Airline Payment Fraud Detection System with Machine Learning and Explainable AI](https://nsdsda.medium.com/how-i-built-an-airline-payment-fraud-detection-system-with-machine-learning-and-explainable-ai-d8d87f1448c7)

If you wanna explore the model, it's published in Hugging Face, check it out here: [nibeditans/Airline-Payment-Fraud-XGBoost](https://huggingface.co/nibeditans/Airline-Payment-Fraud-XGBoost)

If you find this project helpful, feel free to start and fork the repo.😉
