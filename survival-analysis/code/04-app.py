import pandas as pd
import streamlit as st
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Setting Streamlit page config
st.set_page_config(layout="wide")

# Loading data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/modeling_dataset_full.csv")
    df['dba_start_date'] = pd.to_datetime(df['dba_start_date'], errors='coerce')
    df['dba_end_date'] = pd.to_datetime(df['dba_end_date'], errors='coerce')
    # Convert column to int
    if 'administratively_closed' in df.columns:
        df['administratively_closed'] = df['administratively_closed'].fillna(0).astype(int)
    else:
        st.error("'administratively_closed' column is missing in the dataset")
    return df

# Load data into sfo_df
sfo_df = load_data()
# Calculate business age
sfo_df['business_age'] = (pd.to_datetime(sfo_df['dba_end_date'], errors='coerce') -
                           pd.to_datetime(sfo_df['dba_start_date'], errors='coerce')).dt.days / 365
sfo_df['business_age'] = sfo_df['business_age'].fillna(0)  # Handle any NaN values
# Streamlit app layout for the second tab
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧭 Project Overview, Goal and Objective", "📊 Exploratory Data Analysis", "📈 Modeling Visuals", "📊 Deep Survival Analysis", "🔎 Summary"])


with tab1:
    st.title("📍 Business Survival Analysis - Supervisor District 3")

    st.markdown("""
    **Executive Summary**  
    Predictive analytics on business registration trends can inform the prioritization of neighborhoods within San Francisco Supervisor District 3 for development funds by understanding business emergence and density evolution. This project specifically analyzes factors influencing business survival within Supervisor District 3, aiming to predict administrative closure using survival analysis to support targeted funding decisions.

    **Why Model Business Survival for District 3 Funding Decisions?**  
    Understanding why some businesses in San Francisco Supervisor District 3 are more likely to close administratively than others offers valuable insights specifically for the funding team. This analysis can help:

    - Targeted resource allocation: Identify specific business segments or geographic pockets within District 3 that exhibit higher closure rates, allowing for the strategic allocation of development funds and support programs to the most vulnerable areas.
    - Informed funding strategies: Understand the factors contributing to business instability within the district, enabling the funding team to design more effective and tailored interventions to promote business longevity.
    - Performance measurement: Establish a baseline understanding of business survival in District 3 against which the impact of funding initiatives can be measured over time.
    - Prioritization of investment: Inform decisions about where and what types of businesses within Supervisor District 3 would benefit most from development funds to maximize economic impact and sustainability.

    **Goal**  
    Predict the likelihood of a business being administratively closed over time specifically within San Francisco Supervisor District 3 using survival analysis to inform funding decisions.
    """)


with tab2:
    # Set Seaborn and Matplotlib styling
    sns.set(style="whitegrid")

    # Set consistent font style and size globally
    plt.rcParams.update({
        "figure.figsize": (12, 6),
        "font.family": "Arial",
        "font.size": 12,
        "axes.titlesize": 12,
        "axes.labelsize": 12,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 12
    })

    # Streamlit page settings
    st.title("📊 San Francisco , District 3 : Business Registration Dashboard")
    st.markdown("Explore Business Patterns By **Neighborhood**, **License**, **ZIP Codes**, AND **NAIC Descriptions**.")

    # To Load data (with caching)
    @st.cache_data
    def load_cleaned_data():
        df = pd.read_csv("../data/modeling_dataset_full.csv", parse_dates=["dba_start_date"])
        df = df.dropna(subset=["neighborhoods_analysis_boundaries"])
        df["year"] = df["dba_start_date"].dt.year
        return df

    # Loading Claned Data
    df_cleaned = load_cleaned_data()

    # Sidebar: Neighborhood selector
    neighborhoods = sorted(df_cleaned["neighborhoods_analysis_boundaries"].dropna().unique())
    selected_neigh = st.sidebar.selectbox("🏙️ Select Neighborhood:", neighborhoods)

    # Filter data based on neighborhood
    filtered_df = df_cleaned[df_cleaned["neighborhoods_analysis_boundaries"] == selected_neigh]

    # Show filtered data preview
    st.markdown(f"### 📌 Showing Data For: **{selected_neigh}**")
    st.dataframe(filtered_df.head(10), use_container_width=True)

    # --- Visual 1: License Description ---

    st.markdown("### 📋 Number of Business By License Description")
    lic_counts = filtered_df["lic_code_description"].value_counts().nlargest(10)
    lic_counts.index = lic_counts.index.str.title()
    colors = sns.color_palette("Set2", len(lic_counts))
    fig1, ax1 = plt.subplots()
    lic_counts.plot(kind='barh', ax=ax1, color=colors)
    ax1.set_xlabel("Number of Businesses")
    ax1.set_ylabel("License Description")
    ax1.set_title(f"Top 10 License Descriptions In {selected_neigh}")
    ax1.grid(axis='x', linestyle='--', alpha=0.5)
    ax1.grid(axis='y', visible=False)
    plt.subplots_adjust(left=0.3, right=0.95)
    st.pyplot(fig1)


    # --- Visual 2: ZIP Code ---
    st.markdown("### 🏷️ Number of Business By ZIP Codes")
    zip_counts = filtered_df["business_zip"].value_counts().nlargest(10)
    colors = sns.color_palette("Pastel1", len(zip_counts))
    fig2, ax2 = plt.subplots()
    zip_counts.plot(kind='barh', ax=ax2, color=colors)
    ax2.set_xlabel("Number of Businesses")
    ax2.set_ylabel("ZIP Codes")
    ax2.set_title(f"Top 10 ZIP Codes In {selected_neigh}")
    ax2.grid(axis='x', linestyle='--', alpha=0.4)
    ax2.grid(axis='y', visible=False)
    plt.subplots_adjust(left=0.25, right=0.95)
    st.pyplot(fig2)


    # --- Visual 3: Business Registrations Over Time ---
    st.markdown("### 📆 Business Registrations Over Time")
    filtered_df_1950 = filtered_df[filtered_df["year"] >= 2015]
    year_counts = filtered_df_1950["year"].value_counts().sort_index()
    fig4, ax4 = plt.subplots()
    sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o", ax=ax4, color="purple")
    ax4.set_ylabel("Number of Registrations")
    ax4.set_xlabel("Year")
    ax4.set_title(f"Registration Trends In {selected_neigh} (FROM 2015 Onwards)")
    ax4.legend()
    ax4.grid(True, axis='x') 
    ax4.grid(False, axis='y')
    ax4.tick_params(axis='x', rotation=90)
    ax4.set_xticklabels(year_counts.index, ha='center')
    plt.subplots_adjust(bottom=0.5)
    st.pyplot(fig4)

    # --- Visual 4: Openings vs Closures ---
    st.markdown("### 🔒 Observed Business Openings and Administrative Closures Over Time")
    if 'location_end_date' in df_cleaned.columns:
        df_cleaned['location_end_date'] = pd.to_datetime(df_cleaned['location_end_date'], errors='coerce')
        df_cleaned['closure_year'] = df_cleaned['location_end_date'].dt.year
    else:
        st.warning("⚠️ Column Location_End_Date Not Found in the Dataset.")
        st.stop()
    if df_cleaned['administratively_closed'].dtype == object:
        df_cleaned['administratively_closed'] = df_cleaned['administratively_closed'].apply(
            lambda x: 1 if str(x).strip().lower() == '***administratively closed' else 0
        )
    eda_df = df_cleaned[df_cleaned["neighborhoods_analysis_boundaries"] == selected_neigh]

    # Filter data from 2015 onwards
    eda_df = eda_df[eda_df['closure_year'] >= 2015]
    open_counts = eda_df[eda_df['administratively_closed'] == 0]
    open_counts = open_counts['closure_year'].value_counts().sort_index()
    closed_counts = eda_df[eda_df['administratively_closed'] == 1]
    closed_counts = closed_counts['closure_year'].value_counts().sort_index()
    fig5, ax5 = plt.subplots()
    ax5.plot(open_counts.index, open_counts.values, label='Business Openings', marker='o', color='green')
    ax5.plot(closed_counts.index, closed_counts.values, label='Administrative Closures', marker='x', linestyle='--', color='red')
    ax5.set_title(f"Openings vs Administrative Closures in {selected_neigh} (From 2015)")
    ax5.set_xlabel("Year")
    ax5.set_ylabel("Number of Business")
    ax5.legend()
    ax5.grid(True, axis='x')  
    ax5.grid(False, axis='y')
    ax5.tick_params(axis='x', rotation=90)
    plt.tight_layout()
    st.pyplot(fig5)

with tab3:
    st.title("🔒 Survival Analysis")
    # Filter dataset
    sfo_df_filtered = sfo_df.dropna(subset=['lic_code_description', 'business_age'])
    top_5_license_types = sfo_df_filtered['lic_code_description'].value_counts().nlargest(5).index
    df_top = sfo_df_filtered[sfo_df_filtered['lic_code_description'].isin(top_5_license_types)]

    # --- Kaplan-Meier Curves by License Type ---
    st.subheader("📍 Survival Curves by License Type")
    kmf = KaplanMeierFitter()
    palette = sns.color_palette("Set1", len(top_5_license_types))
    fig, ax = plt.subplots(figsize=(8, 6))
    for (name, group), color in zip(df_top.groupby('lic_code_description'), palette):
        kmf.fit(group['business_age'], group['administratively_closed'], label=name.title())
        kmf.plot(ci_show=False, color=color, linestyle='-', linewidth=2, ax=ax)

    ax.set_title("Survival by License Type")
    ax.set_xlim(right=60)
    ax.set_ylim(0.0, 0.2)
    ax.set_yticks(np.arange(0.0, 0.21, 0.05))
    ax.set_xlabel("Business Age (Years)")
    ax.set_ylabel("Survival Probability")
    ax.legend(title='License Type', loc='upper right', frameon=False)
    ax.grid(True, axis='x') 
    ax.grid(False, axis='y')
    plt.tight_layout()
    st.pyplot(fig)

    # --- Curves by Neighborhood ---
    st.subheader("📍 Survival Curves by Neighborhood")
    palette = sns.color_palette("tab20", n_colors=len(df_top['neighborhoods_analysis_boundaries'].unique()))
    fig, ax = plt.subplots(figsize=(8,6)) 
    for (name, group), color in zip(df_top.groupby('neighborhoods_analysis_boundaries'), palette):
        if len(group) >= 10:
            kmf.fit(group['business_age'], group['administratively_closed'], label=name)
            kmf.plot(ci_show=False, color=color, linestyle='-', linewidth=2, ax=ax)

    ax.set_title("Survival by Neighborhood")
    ax.set_xlim(right=60)
    ax.set_ylim(0.0, 0.2)
    ax.set_yticks(np.arange(0.0, 0.21, 0.05))
    ax.set_xlabel("Business Age (Years)")
    ax.set_ylabel("Survival Probability")
    ax.legend(title='Neighborhood', loc='upper right', frameon=False)
    ax.grid(True, axis='x')  
    ax.grid(False, axis='y')
    plt.tight_layout()
    st.pyplot(fig)


with tab4:
    st.header("📈 Business Survival Analysis by Neighborhood and License Type")
    time_point = st.slider("Select Survival Time Point (Years):", 1, 60, 60)

    # --- Kaplan-Meier by Neighborhood ---
    kmf = KaplanMeierFitter()
    survival_probs = {}
    for name, group in df_top.groupby('neighborhoods_analysis_boundaries'):
        if len(group) >= 10:
            kmf.fit(group['business_age'], group['administratively_closed'])
            survival_probs[name] = kmf.predict(time_point)

    survival_df = pd.DataFrame.from_dict(survival_probs, orient='index', columns=['Survival Probability'])
    survival_df = survival_df.sort_values(by='Survival Probability', ascending=False)
    st.subheader(f"🔎 Survival Probability at {time_point} Years by Neighborhood")
    
    fig, ax = plt.subplots(figsize=(10,8))
    sns.barplot(y=survival_df.index, x='Survival Probability', data=survival_df, palette='Set2', ax=ax, width=0.2)
    plt.xlabel('Survival Probability')
    plt.ylabel('Neighborhood')
    plt.title(f'Survival Probability by Neighborhood at {time_point} Years')
    plt.tight_layout()
    st.pyplot(fig)

    # --- Kaplan-Meier by License Type ---
    kmf = KaplanMeierFitter()
    license_survival_probs = {}

    for name, group in df_top.groupby('lic_code_description'):
        if len(group) >= 10:
            kmf.fit(group['business_age'], group['administratively_closed'])
            license_survival_probs[name] = kmf.predict(time_point)

    license_survival_df = pd.DataFrame.from_dict(license_survival_probs, orient='index', columns=['Survival Probability'])
    license_survival_df = license_survival_df.sort_values(by='Survival Probability', ascending=False)
    license_survival_df.index = license_survival_df.index.str.title()

    st.subheader(f"🔒 Survival Probability at {time_point} Years by License Type")
    fig2, ax2 = plt.subplots(figsize=(10,8))  
    sns.barplot(y=license_survival_df.index, x='Survival Probability', data=license_survival_df, palette='Set1', ax=ax2, width=0.2)
    plt.xlabel('Survival Probability')
    plt.ylabel('License Type')
    plt.title(f'Survival Probability by License Type at {time_point} Years')
    plt.tight_layout()
    st.pyplot(fig2)

with tab5:
    # Tab 5: Summary
    st.title("📑 Summary of Business Survival Trends")

    # Kaplan-Meier trends summary
    neighborhood_trends = []
    for name, group in df_top.groupby('neighborhoods_analysis_boundaries'):
        if len(group) >= 10:
            kmf.fit(group['business_age'], group['administratively_closed'])
            survival_at_5 = kmf.predict(5) * 100  
            survival_at_10 = kmf.predict(10) * 100 
            neighborhood_trends.append({
                "Neighborhood": name,
                "5-Year Survival (%)": round(survival_at_5, 2),
                "10-Year Survival (%)": round(survival_at_10, 2)
            })

    summary_df = pd.DataFrame(neighborhood_trends)
    sorted_summary_df = summary_df.sort_values(by="5-Year Survival (%)", ascending=False)  
    st.markdown("### 📊 Business Survival by Neighborhood (5 and 10 Years)")
    st.dataframe(sorted_summary_df)

    # Data-driven summary based on survival probabilities
    st.markdown("### 📌 Data-Driven Insights Based on Neighborhoods")
   
    # To Calculate the overall survival rate at 5 years and 10 years
    overall_5_year_survival = sorted_summary_df["5-Year Survival (%)"].mean()
    overall_10_year_survival = sorted_summary_df["10-Year Survival (%)"].mean()

    st.markdown(f"""
    Based on the survival analysis, the overall business survival rates across neighborhoods are:
    - **Average 5-Year Survival Rate**: {overall_5_year_survival:.2f}%
    - **Average 10-Year Survival Rate**: {overall_10_year_survival:.2f}%
    
    These survival rates provide a clear indication of the overall business longevity across neighborhoods.
    """)

    # To Identify the best and bottom performing neighborhoods
    best_neigh_5_year = sorted_summary_df.loc[sorted_summary_df['5-Year Survival (%)'].idxmax()]
    bottom_neigh_5_year = sorted_summary_df.loc[sorted_summary_df['5-Year Survival (%)'].idxmin()]

    st.markdown(f"""
    - The **best performing neighborhood** at 5 years is **{best_neigh_5_year['Neighborhood']}**, with a survival rate of {best_neigh_5_year['5-Year Survival (%)']:.2f}%.
    - The **bottom performing neighborhood** at 5 years is **{bottom_neigh_5_year['Neighborhood']}**, with a survival rate of {bottom_neigh_5_year['5-Year Survival (%)']:.2f}%.
    
    The difference in survival rates between neighborhoods highlights areas where business conditions may need improvement.
    """)

    # Data-driven summary based on License Type Survival probabilities

    # To Calculate the overall survival rate at 5 years and 10 years
    license_survival_trends = []

    # To Fit Kaplan-Meier for each license type with at least 10 entries
    for name, group in df_top.groupby('lic_code_description'):
        if len(group) >= 10:
            kmf.fit(group['business_age'], group['administratively_closed'])
            survival_at_5 = kmf.predict(5) * 100  # Convert to percentage
            survival_at_10 = kmf.predict(10) * 100  # Convert to percentage
            license_survival_trends.append({
                "License Type": name,
                "5-Year Survival (%)": round(survival_at_5, 2),
                "10-Year Survival (%)": round(survival_at_10, 2)
            })

    # To Create Dataframe sort
    license_summary_df = pd.DataFrame(license_survival_trends)
    sorted_summary_df = license_summary_df.sort_values(by="5-Year Survival (%)", ascending=False)

    # To Calculate overall averages
    overall_5_year_survival = sorted_summary_df["5-Year Survival (%)"].mean()
    overall_10_year_survival = sorted_summary_df["10-Year Survival (%)"].mean()

    # To Identify best and bottom performing license types (based on 5-year survival)
    best_license_5_year = sorted_summary_df.loc[sorted_summary_df["5-Year Survival (%)"].idxmax()]
    bottom_license_5_year = sorted_summary_df.loc[sorted_summary_df["5-Year Survival (%)"].idxmin()]


    # Streamlit display
    st.markdown("### 📊 Business Survival by License Type (5 and 10 Years)")
    sorted_summary_df['License Type'] = sorted_summary_df['License Type'].str.title()
    st.dataframe(sorted_summary_df)

    # To Show averages and insights
    st.markdown("### 📈 Data-Driven Insights Based on License Types")
    st.markdown(f"""
    Based on the survival analysis, the overall business survival rates across License Types are:

    - **Average 5-Year Survival Rate**: {overall_5_year_survival:.2f}%
    - **Average 10-Year Survival Rate**: {overall_10_year_survival:.2f}%

    These survival rates reveal distinct patterns of business longevity linked to each License Type.

    - The **Best Performing License Type (5-Year)**: {best_license_5_year['License Type'].title()} — {best_license_5_year['5-Year Survival (%)']}%
    - The **bottom Performing License Type (5-Year)**: {bottom_license_5_year['License Type'].title()} — {bottom_license_5_year['5-Year Survival (%)']}%

    The variation in survival rates across License Types highlights areas where business conditions could be improved.
    """)

    # Summary of overall recommendations    

    st.markdown("### 💡 Overall Recommendations:")
    st.markdown("""
    **Neighborhoods** 
    - Neighborhoods with higher survival rates should be further nurtured with targeted economic development programs. 
    - Neighborhoods with lower survival rates should receive tailored support such as grants, infrastructure improvement, and mentorship programs to help improve their business longevity.

    **License Types** 
    - License types with higher survival rates could act as models for businesses in struggling sectors. 
    - Focus efforts on business types with lower survival rates by identifying barriers to their success and offering targeted programs, policy changes, and financial support.
    """)
