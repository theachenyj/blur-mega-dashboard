import streamlit as st
from millify import millify
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt
def comparison_page():
    st.markdown("## NFT Marketplace Comparison ")
    st.markdown(
        "Text..."
    )


    st.markdown("#### Sales Count ")
    st.markdown("---")
    # Sales Count
    col1, col2 = st.columns(2)
    # Total Sales Count
    with col1:
        save_dict = {"Platform Name": [], "Sales Count": []}
        web_data = requests.get(url=urls.url_market_comparison_total, headers={})
        for item in json.loads(web_data.text):
            save_dict["Platform Name"].append(item["PLATFORM_NAME"])
            save_dict["Sales Count"].append(item["TRANSACTION_COUNTS"])
        df = pd.DataFrame(data=save_dict, columns=['Platform Name', 'Sales Count'])

        c = alt.Chart(df).mark_arc().encode(
            theta=alt.Theta(field="Sales Count", type="quantitative"),
            color=alt.Color(field="Platform Name", type="nominal"),
        )
        st.altair_chart(c, use_container_width=True)
    # Daily Sales Counts
    with col2:
        save_dict = {"Block Date": [], "Platform": [], "Sales Count": []}
        web_data = requests.get(url=urls.url_market_comparison_daily, headers={})
        for item in json.loads(web_data.text):
            save_dict["Block Date"].append(item["BLOCK_DATE"])
            save_dict["Platform"].append(item["PLATFORM_NAME"])
            save_dict["Sales Count"].append(item["TRANSACTION_COUNTS"])
        df = pd.DataFrame(data=save_dict, columns=['Block Date', 'Platform', 'Sales Count'])
        c = alt.Chart(df).mark_area().encode(
            x=alt.X("Block Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Sales Count:Q", stack="normalize"),
            color="Platform:N"
        )
        st.altair_chart(c, use_container_width=True)

    # Sales Volume
    st.markdown("#### Sales Volume ")
    st.markdown("---")
    col1, col2 = st.columns(2)
    # Total Sales Volume
    with col1:
        save_dict = {"Platform": [], "Sales Volume": []}
        web_data = requests.get(url=urls.url_market_comparison_total, headers={})
        for item in json.loads(web_data.text):
            save_dict["Platform"].append(item["PLATFORM_NAME"])
            save_dict["Sales Volume"].append(item["TRANSACTION_VOLUMES"])
        df = pd.DataFrame(data=save_dict, columns=['Platform', 'Sales Volume'])

        c = alt.Chart(df).mark_arc().encode(
            theta=alt.Theta(field="Sales Volume", type="quantitative"),
            color=alt.Color(field="Platform", type="nominal"),
        )
        st.altair_chart(c, use_container_width=True)
    # Daily Sales Volume
    with col2:
        save_dict = {"Block Date": [], "Platform": [], "Sales Volume": []}
        web_data = requests.get(url=urls.url_market_comparison_daily, headers={})
        for item in json.loads(web_data.text):
            save_dict["Block Date"].append(item["BLOCK_DATE"])
            save_dict["Platform"].append(item["PLATFORM_NAME"])
            save_dict["Sales Volume"].append(item["TRANSACTION_VOLUMES"])
        df = pd.DataFrame(data=save_dict, columns=['Block Date', 'Platform', 'Sales Volume'])
        c = alt.Chart(df).mark_area().encode(
            x=alt.X("Block Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Sales Volume:Q", stack="normalize"),
            color="Platform:N"
        )
        st.altair_chart(c, use_container_width=True)

    # Unique Traders
    st.markdown("#### Unique Traders ")
    st.markdown("---")
    col1, col2 = st.columns(2)
    # Total Unique Traders
    with col1:
        save_dict = {"Platform": [], "Traders": []}
        web_data = requests.get(url=urls.url_market_comparison_total, headers={})
        for item in json.loads(web_data.text):
            save_dict["Platform"].append(item["PLATFORM_NAME"])
            save_dict["Traders"].append(item["TRADERS"])
        df = pd.DataFrame(data=save_dict, columns=['Platform', 'Traders'])

        c = alt.Chart(df).mark_arc().encode(
            theta=alt.Theta(field="Traders", type="quantitative"),
            color=alt.Color(field="Platform", type="nominal"),
        )
        st.altair_chart(c, use_container_width=True)
    # Daily Unique Traders
    with col2:
        save_dict = {"Block Date": [], "Platform": [], "Traders": []}
        web_data = requests.get(url=urls.url_market_comparison_daily, headers={})
        for item in json.loads(web_data.text):
            save_dict["Block Date"].append(item["BLOCK_DATE"])
            save_dict["Platform"].append(item["PLATFORM_NAME"])
            save_dict["Traders"].append(item["TRADERS"])
        df = pd.DataFrame(data=save_dict, columns=['Block Date', 'Platform', 'Traders'])
        c = alt.Chart(df).mark_area().encode(
            x=alt.X("Block Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Traders:Q", stack="normalize"),
            color="Platform:N"
        )
        st.altair_chart(c, use_container_width=True)

    # % of Ethereum NFT traders that have certain Marketplace
    st.markdown("#### NFT Traders Penetration on Ethereum ")
    st.markdown("---")
    with st.container():
        save_dict = {"Block Date": [], "Platform": [], "Penetration": []}
        web_data = requests.get(url=urls.url_market_share, headers={})
        for item in json.loads(web_data.text):
            save_dict["Block Date"].append(item["BLOCK_DATE"])
            save_dict["Platform"].append(item["PLATFORM_NAME"])
            save_dict["Penetration"].append(item["PENETRATION"])
        df = pd.DataFrame(data=save_dict, columns=['Block Date', 'Platform', 'Penetration'])
        c = alt.Chart(df).mark_area().encode(
            x=alt.X("Block Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Penetration:Q", axis=alt.Axis(format='%')),
            color="Platform:N"
        )
        st.altair_chart(c, use_container_width=True)