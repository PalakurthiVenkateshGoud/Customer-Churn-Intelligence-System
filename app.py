import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Retention Intelligence Dashboard",
    layout="wide"
)

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
risk_df = pd.read_csv("outputs/risk_segmentation.csv")
model_df = pd.read_csv("outputs/model_results.csv")

total_customers = len(df)
churn_count = len(df[df["Churn"] == "Yes"])
churn_rate = round((churn_count / total_customers) * 100, 2)

avg_tenure = round(df["tenure"].mean(), 1)
avg_monthly = round(df["MonthlyCharges"].mean(), 2)

high_risk = risk_df[risk_df["Risk_Tier"] == "High Risk"]

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "Customer Analytics",
        "Model Performance",
        "Risk Intelligence",
        "Feature Insights",
        "Recommendations"
    ]
)

if page == "Overview":

    st.title("Customer Retention Intelligence Dashboard")

    st.markdown("""
    ### Business Objective
    Analyze customer churn behavior, identify churn drivers, evaluate predictive models, and generate actionable retention strategies.
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", total_customers)
    col2.metric("Churn Rate", f"{churn_rate}%")
    col3.metric("Avg Tenure", avg_tenure)
    col4.metric("High Risk Customers", len(high_risk))

    st.divider()

    st.subheader("Dataset Summary")

    st.write(f"Total Records: {total_customers}")
    st.write("Dataset: Telco Customer Churn")
    st.write("Objective: Customer Retention Analytics")

    st.info(
        f"{churn_rate}% of customers are at risk of churn."
    )

    st.warning(
        "High-risk customers should be prioritized for retention campaigns."
    )

elif page == "Customer Analytics":

    st.title("Customer Behavior Analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.image("charts/churn_distribution.png")

    with col2:
        st.image("charts/churn_by_contract.png")

    col3, col4 = st.columns(2)

    with col3:
        st.image("charts/tenure_distribution.png")

    with col4:
        st.image("charts/correlation_heatmap.png")

elif page == "Model Performance":

    st.title("Predictive Model Evaluation")

    col1, col2 = st.columns(2)

    with col1:
        st.image("charts/model_comparison.png")

    with col2:
        st.image("charts/confusion_matrix_comparison.png")

    st.subheader("Model Performance Metrics")

    st.dataframe(model_df)

    best_model = model_df.loc[
        model_df["ROC-AUC"].idxmax()
    ]

    st.success(
        f"Best Performing Model: {best_model.iloc[0]}"
    )

elif page == "Risk Intelligence":

    st.title("Risk Segmentation Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        st.image("charts/risk_tier_distribution.png")

    with col2:
        st.image("charts/risk_tier_comparison.png")

    st.subheader("High Risk Customers")

    st.metric(
        "High Risk Customers",
        len(high_risk)
    )

    st.dataframe(
        high_risk.head(10)
    )

elif page == "Feature Insights":

    st.title("Primary Churn Drivers")

    st.image("charts/feature_importance.png")

    st.markdown("""
### Key Drivers

- Contract Type significantly impacts churn probability.
- Customers with shorter tenure are more likely to churn.
- Monthly Charges influence customer retention behavior.
- Service usage patterns provide strong predictive signals.
""")

elif page == "Recommendations":

    st.title("Executive Recommendations")

    st.markdown("""
### Strategic Recommendations

1. Target high-risk customers with personalized retention campaigns.

2. Encourage customers to adopt longer-term contracts.

3. Improve onboarding experiences for new customers.

4. Monitor customers with increasing monthly charges.

5. Build proactive churn monitoring systems.

6. Use predictive analytics to intervene before churn occurs.
""")

    st.success(
        "Predictive retention strategies can significantly reduce customer attrition and improve lifetime value."
    )