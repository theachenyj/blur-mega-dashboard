import streamlit as st
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def trading_page():
    st.markdown("## Trading Analysis ")
    st.markdown("---")

    # The Percentage(%) Increase/Decrease of Sales Count
    # The Percentage(%) Increase/Decrease of Sales Volume
    api_data_sales_dod = requests.get(url=urls.url_sales_dod, headers={})
    save_dict_sales_count_dod = {"Date": [], "Change": []}
    for item in json.loads(api_data_sales_dod.text):
        save_dict_sales_count_dod["Date"].append(item["BLOCK_WEEK"])
        save_dict_sales_count_dod["Change"].append(item["TRANSACTION_COUNTS_DOD"])
    df_sales_count_dod = pd.DataFrame(data=save_dict_sales_count_dod, columns=['Date', 'Change'])

    save_dict_sales_volume_dod = {"Date": [], "Change": []}
    for item in json.loads(api_data_sales_dod.text):
        save_dict_sales_volume_dod["Date"].append(item["BLOCK_WEEK"])
        save_dict_sales_volume_dod["Change"].append(item["TRANSACTION_VOLUMES_DOD"])
    df_sales_volume_dod = pd.DataFrame(data=save_dict_sales_volume_dod, columns=['Date', 'Change'])

    sales_count_dod, sales_volume_dod = st.columns(2)

    with sales_count_dod:
        sales_count_dod_chart = alt.Chart(df_sales_count_dod).mark_bar(size=20).encode(
            alt.X('Date:T',  axis=alt.Axis(title=None)),
            alt.Y('Change:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.Change > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            ),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Change:Q', format='.2%')
            ]
        ).properties(title='The Percentage(%) Increase/Decrease of Sales Count')
        st.altair_chart(sales_count_dod_chart, use_container_width=True)
        st.markdown(" ")

    with sales_volume_dod:
        sales_volume_dod_chart = alt.Chart(df_sales_volume_dod).mark_bar(size=20).encode(
            alt.X('Date:T',  axis=alt.Axis(title=None)),
            alt.Y('Change:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.Change > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            ),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Change:Q', format='.2%')
            ]
        ).properties(title='The Percentage(%) Increase/Decrease of Sales Volume')
        st.altair_chart(sales_volume_dod_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Count
    st.markdown(" ")
    save_dict_daily_sales_count = {"Date": [], "Sales Count": []}
    api_data_daily_sales = requests.get(url=urls.url_sales_trend, headers={})
    for item in json.loads(api_data_daily_sales.text):
        save_dict_daily_sales_count["Date"].append(item["BLOCK_DATE"])
        save_dict_daily_sales_count["Sales Count"].append(item["TRANSACTION_COUNTS"])
    df_daily_sales_count = pd.DataFrame(data=save_dict_daily_sales_count, columns=['Date', 'Sales Count'])

    save_dict_daily_sales_volume = {"Date": [], "Sales Volume": []}
    for item in json.loads(api_data_daily_sales.text):
        save_dict_daily_sales_volume["Date"].append(item["BLOCK_DATE"])
        save_dict_daily_sales_volume["Sales Volume"].append(item["TRANSACTION_VOLUMES"])
    df_daily_sales_volume = pd.DataFrame(data=save_dict_daily_sales_volume, columns=['Date', 'Sales Volume'])

    daily_sales_count = st.container()
    with daily_sales_count:
        daily_sales_count_chart = alt.Chart(df_daily_sales_count).mark_bar(color='#E4831E').encode(
            x=alt.X('Date:T', axis=alt.Axis(title=None)),
            y='Sales Count:Q'
        ).properties(title='Daily Sales Count')
        st.altair_chart(daily_sales_count_chart, use_container_width=True)
        st.markdown(" ")

    daily_sales_volume = st.container()
    with daily_sales_volume:
        daily_sales_volume_chart = alt.Chart(df_daily_sales_volume).mark_bar(color='#E4831E').encode(
            x=alt.X('Date:T', axis=alt.Axis(title=None)),
            y='Sales Volume:Q'
        ).properties(title='Daily Sales Volume')
        st.altair_chart(daily_sales_volume_chart, use_container_width=True)
        st.markdown(" ")

    # Weekly change of sales NFTs and NFT collections
    st.markdown(" ")
    save_dict_sales_nft_dod = {"Date": [], "Change": []}
    for item in json.loads(api_data_sales_dod.text):
        save_dict_sales_nft_dod["Date"].append(item["BLOCK_WEEK"])
        save_dict_sales_nft_dod["Change"].append(item["TRANSACTION_NFTS_DOD"])
    df_sales_nft_dod = pd.DataFrame(data=save_dict_sales_nft_dod, columns=['Date', 'Change'])

    save_dict_sales_coolection_dod = {"Date": [], "Change": []}
    for item in json.loads(api_data_sales_dod.text):
        save_dict_sales_coolection_dod["Date"].append(item["BLOCK_WEEK"])
        save_dict_sales_coolection_dod["Change"].append(item["TRANSACTION_COLLECTIONS_DOD"])
    df_sales_collection_dod = pd.DataFrame(data=save_dict_sales_coolection_dod, columns=['Date', 'Change'])

    sales_collection, sales_nft = st.columns(2)
    with sales_collection:
        sales_collection_chart = alt.Chart(df_sales_collection_dod).mark_bar(size=20).encode(
            alt.X('Date:T', axis=alt.Axis(title=None)),
            alt.Y('Change:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.Change > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            ),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Change:Q', format='.2%')
            ]
        ).properties(title='The Percentage(%) Increase/Decrease of Sales NFT Collections')
        st.altair_chart(sales_collection_chart, use_container_width=True)
        st.markdown(" ")

    with sales_nft:
        sales_nft_chart = alt.Chart(df_sales_nft_dod).mark_bar(size=20).encode(
            alt.X('Date:T', axis=alt.Axis(title=None)),
            alt.Y('Change:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.Change > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            ),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Change:Q', format='.2%')
            ]
        ).properties(title='The Percentage(%) Increase/Decrease of Sales NFTs')
        st.altair_chart(sales_nft_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales NFTs
    # Daily Sales NFT Collections
    st.markdown(" ")
    save_dict_daily_sales_collection = {"Date": [], "Sales NFT Collections": []}
    for item in json.loads(api_data_daily_sales.text):
        save_dict_daily_sales_collection["Date"].append(item["BLOCK_DATE"])
        save_dict_daily_sales_collection["Sales NFT Collections"].append(item["TRANSACTION_COLLECTIONS"])
    df_daily_sales_collection = pd.DataFrame(data=save_dict_daily_sales_collection, columns=['Date', 'Sales NFT Collections'])

    save_dict_daily_sales_nft = {"Date": [], "Sales NFTs": []}
    for item in json.loads(api_data_daily_sales.text):
        save_dict_daily_sales_nft["Date"].append(item["BLOCK_DATE"])
        save_dict_daily_sales_nft["Sales NFTs"].append(item["TRANSACTION_NFTS"])
    df_daily_sales_nft = pd.DataFrame(data=save_dict_daily_sales_nft, columns=['Date', 'Sales NFTs'])

    daily_sales_collection = st.container()
    with daily_sales_collection:
        daily_sales_collection_chart = alt.Chart(df_daily_sales_collection).mark_bar(color='#E4831E').encode(
            x=alt.X('Date:T', axis=alt.Axis(title=None)),
            y='Sales NFT Collections:Q'
        ).properties(title='Daily Sales NFT Collections')
        st.altair_chart(daily_sales_collection_chart, use_container_width=True)
        st.markdown(" ")

    daily_sales_nft = st.container()
    with daily_sales_nft:
        daily_sales_nft_chart = alt.Chart(df_daily_sales_nft).mark_bar(color='#E4831E').encode(
            x=alt.X('Date:T', axis=alt.Axis(title=None)),
            y='Sales NFTs:Q'
        ).properties(title='Daily Sales NFTs')
        st.altair_chart(daily_sales_nft_chart, use_container_width=True)
        st.markdown(" ")



