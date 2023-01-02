import streamlit as st
from millify import millify
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt
def comparison_page():
    st.markdown("## Marketplace Comparison ")
    st.markdown(
        "Text..."
    )
    st.markdown("---")

    # Sales Count
    save_dict_sales_count_total = {"Platform": [], "Sales Count": []}
    api_data_sales_count_total = requests.get(url=urls.url_market_comparison_total, headers={})
    for item in json.loads(api_data_sales_count_total.text):
        save_dict_sales_count_total["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_count_total["Sales Count"].append(item["TRANSACTION_COUNTS"])
    df_sales_count_total = pd.DataFrame(data=save_dict_sales_count_total, columns=['Platform', 'Sales Count'])

    save_dict_sales_count_daily = {"Date": [], "Platform": [], "Sales Count": []}
    api_data_sales_count_daily = requests.get(url=urls.url_market_comparison_daily, headers={})
    for item in json.loads(api_data_sales_count_daily.text):
        save_dict_sales_count_daily["Date"].append(item["BLOCK_DATE"])
        save_dict_sales_count_daily["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_count_daily["Sales Count"].append(item["TRANSACTION_COUNTS"])
    df_sales_count_daily = pd.DataFrame(data=save_dict_sales_count_daily, columns=['Date', 'Platform', 'Sales Count'])

    sales_count_total, sales_count_daily = st.columns(2)
    # Total Sales Count
    with sales_count_total:
        sales_count_total_chart = alt.Chart(df_sales_count_total).mark_arc().encode(
            theta=alt.Theta(field="Sales Count", type="quantitative"),
            color=alt.Color(
                field="Platform",
                type="nominal",
                scale=alt.Scale(
                    domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                    range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
                )
            ),
            tooltip=[
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Sales Count:Q', format=',')
            ]
        ).properties(title='Total Sales Count by Marketpalce since 2022-10-19')
        st.altair_chart(sales_count_total_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Counts
    with sales_count_daily:
        sales_count_daily_chart = alt.Chart(df_sales_count_daily).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Sales Count:Q", stack="normalize"),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Sales Count:Q', format=',')
            ]
        ).properties(title='Daily Sales Count by Marketpalce')
        st.altair_chart(sales_count_daily_chart, use_container_width=True)
        st.markdown(" ")

    # Sales Volume
    st.markdown(" ")
    save_dict_sales_volume_total = {"Platform": [], "Sales Volume": []}
    for item in json.loads(api_data_sales_count_total.text):
        save_dict_sales_volume_total["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_volume_total["Sales Volume"].append(item["TRANSACTION_VOLUMES"])
    df_sales_volume_total = pd.DataFrame(data=save_dict_sales_volume_total, columns=['Platform', 'Sales Volume'])

    save_dict_sales_volume_daily = {"Date": [], "Platform": [], "Sales Volume": []}
    for item in json.loads(api_data_sales_count_daily.text):
        save_dict_sales_volume_daily["Date"].append(item["BLOCK_DATE"])
        save_dict_sales_volume_daily["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_volume_daily["Sales Volume"].append(item["TRANSACTION_VOLUMES"])
    df_sales_volume_daily = pd.DataFrame(data=save_dict_sales_volume_daily, columns=['Date', 'Platform', 'Sales Volume'])

    sales_volume_total, sales_volume_daily = st.columns(2)
    # Total Sales Volume
    with sales_volume_total:
        sales_volume_total_chart = alt.Chart(df_sales_volume_total).mark_arc().encode(
            theta=alt.Theta(field="Sales Volume", type="quantitative"),
            color=alt.Color(
                field="Platform",
                type="nominal",
                scale=alt.Scale(
                    domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                    range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
                )
            ),
            tooltip=[
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Sales Volume:Q', format=',')
            ]
        ).properties(title='Total Sales Volume by Marketpalce since 2022-10-19')
        st.altair_chart(sales_volume_total_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Volume
    with sales_volume_daily:
        sales_volume_daily_chart = alt.Chart(df_sales_volume_daily).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Sales Volume:Q", stack="normalize"),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Sales Volume:Q', format=',')
            ]
        ).properties(title='Daily Sales Volume by Marketpalce')
        st.altair_chart(sales_volume_daily_chart, use_container_width=True)
        st.markdown(" ")


    # Unique Traders
    st.markdown(" ")
    save_dict_trader_total = {"Platform": [], "Traders": []}
    for item in json.loads(api_data_sales_count_total.text):
        save_dict_trader_total["Platform"].append(item["PLATFORM_NAME"])
        save_dict_trader_total["Traders"].append(item["TRADERS"])
    df_trader_total = pd.DataFrame(data=save_dict_trader_total, columns=['Platform', 'Traders'])

    save_dict_trader_daily = {"Date": [], "Platform": [], "Traders": []}
    for item in json.loads(api_data_sales_count_daily.text):
        save_dict_trader_daily["Date"].append(item["BLOCK_DATE"])
        save_dict_trader_daily["Platform"].append(item["PLATFORM_NAME"])
        save_dict_trader_daily["Traders"].append(item["TRADERS"])
    df_trader_daily = pd.DataFrame(data=save_dict_trader_daily,
                                         columns=['Date', 'Platform', 'Traders'])

    trader_total, trader_daily = st.columns(2)
    # Total Traders
    with trader_total:
        trader_total_chart = alt.Chart(df_trader_total).mark_arc().encode(
            theta=alt.Theta(field="Traders", type="quantitative"),
            color=alt.Color(
                field="Platform",
                type="nominal",
                scale=alt.Scale(
                    domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                    range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
                )
            ),
            tooltip=[
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Traders:Q', format=',')
            ]
        ).properties(title='Total Traders by Marketpalce since 2022-10-19')
        st.altair_chart(trader_total_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Volume
    with trader_daily:
        trader_daily_chart = alt.Chart(df_trader_daily).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Traders:Q", stack="normalize"),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Traders:Q', format=',')
            ]
        ).properties(title='Daily Traders by Marketpalce')
        st.altair_chart(trader_daily_chart, use_container_width=True)
        st.markdown(" ")

    # % of Ethereum NFT traders that have certain Marketplace
    st.markdown(" ")
    save_dict_penetration = {"Date": [], "Platform": [], "Penetration": []}
    api_data_penetration = requests.get(url=urls.url_market_share, headers={})
    for item in json.loads(api_data_penetration.text):
        save_dict_penetration["Date"].append(item["BLOCK_DATE"])
        save_dict_penetration["Platform"].append(item["PLATFORM_NAME"])
        save_dict_penetration["Penetration"].append(item["PENETRATION"])
    df_penetration = pd.DataFrame(data=save_dict_penetration, columns=['Date', 'Platform', 'Penetration'])

    penetration = st.container()
    with penetration:
        penetration_chart = alt.Chart(df_penetration).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Penetration:Q", axis=alt.Axis(format='%')),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('Penetration:Q', format='.2%')
            ]
        ).properties(title='NFT Trader Penetration on Ethereum')
        st.altair_chart(penetration_chart, use_container_width=True)