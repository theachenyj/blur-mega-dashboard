import streamlit as st
from millify import millify
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt
def comparison_page():
    st.markdown("## Marketplace Comparison ")
    st.markdown("---")

    # Sales Count
    save_dict_sales_count_total = {"Platform": [], "% of Total Sales Count": []}
    api_data_sales_count_total = requests.get(url=urls.url_market_comparison_total, headers={})
    for item in json.loads(api_data_sales_count_total.text):
        save_dict_sales_count_total["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_count_total["% of Total Sales Count"].append(item["TRASNSACTION_COUNTS_PCT"])
    df_sales_count_total = pd.DataFrame(data=save_dict_sales_count_total, columns=['Platform', '% of Total Sales Count'])

    save_dict_sales_count_daily = {"Date": [], "Platform": [], "% of Sales Count": []}
    api_data_sales_count_daily = requests.get(url=urls.url_market_comparison_daily, headers={})
    for item in json.loads(api_data_sales_count_daily.text):
        save_dict_sales_count_daily["Date"].append(item["BLOCK_DATE"])
        save_dict_sales_count_daily["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_count_daily["% of Sales Count"].append(item["TRANSACTION_COUNTS_PCT"])
    df_sales_count_daily = pd.DataFrame(data=save_dict_sales_count_daily, columns=['Date', 'Platform', '% of Sales Count'])

    sales_count_total, sales_count_daily = st.columns(2)
    # Total Sales Count
    with sales_count_total:
        sales_count_total_chart = alt.Chart(df_sales_count_total).mark_arc().encode(
            theta=alt.Theta(field="% of Total Sales Count", type="quantitative"),
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
                alt.Tooltip('% of Total Sales Count:Q', format='.2%')
            ]
        ).properties(title='% of Total Sales Count since 2022-10-19')
        st.altair_chart(sales_count_total_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Counts
    with sales_count_daily:
        sales_count_daily_chart = alt.Chart(df_sales_count_daily).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("% of Sales Count:Q", stack="normalize"),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('% of Sales Count:Q', format='.2%')
            ]
        ).properties(title='% of Daily Sales Count')
        st.altair_chart(sales_count_daily_chart, use_container_width=True)
        st.markdown(" ")

    # Sales Volume
    st.markdown(" ")
    save_dict_sales_volume_total = {"Platform": [], "% of Total Sales Volume": []}
    for item in json.loads(api_data_sales_count_total.text):
        save_dict_sales_volume_total["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_volume_total["% of Total Sales Volume"].append(item["TRANSACTION_VOLUMES_PCT"])
    df_sales_volume_total = pd.DataFrame(data=save_dict_sales_volume_total, columns=['Platform', '% of Total Sales Volume'])

    save_dict_sales_volume_daily = {"Date": [], "Platform": [], "% of Sales Volume": []}
    for item in json.loads(api_data_sales_count_daily.text):
        save_dict_sales_volume_daily["Date"].append(item["BLOCK_DATE"])
        save_dict_sales_volume_daily["Platform"].append(item["PLATFORM_NAME"])
        save_dict_sales_volume_daily["% of Sales Volume"].append(item["TRANSACTION_VOLUMES_PCT"])
    df_sales_volume_daily = pd.DataFrame(data=save_dict_sales_volume_daily, columns=['Date', 'Platform', '% of Sales Volume'])

    sales_volume_total, sales_volume_daily = st.columns(2)
    # Total Sales Volume
    with sales_volume_total:
        sales_volume_total_chart = alt.Chart(df_sales_volume_total).mark_arc().encode(
            theta=alt.Theta(field="% of Total Sales Volume", type="quantitative"),
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
                alt.Tooltip('% of Total Sales Volume:Q', format='.2%')
            ]
        ).properties(title='% of Total Sales Volume since 2022-10-19')
        st.altair_chart(sales_volume_total_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Volume
    with sales_volume_daily:
        sales_volume_daily_chart = alt.Chart(df_sales_volume_daily).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("% of Sales Volume:Q", stack="normalize"),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('% of Sales Volume:Q', format='.2%')
            ]
        ).properties(title='% of Daily Sales Volume')
        st.altair_chart(sales_volume_daily_chart, use_container_width=True)
        st.markdown(" ")


    # Unique Traders
    st.markdown(" ")
    save_dict_trader_total = {"Platform": [], "% of Total Traders": []}
    for item in json.loads(api_data_sales_count_total.text):
        save_dict_trader_total["Platform"].append(item["PLATFORM_NAME"])
        save_dict_trader_total["% of Total Traders"].append(item["TRADER_PCT"])
    df_trader_total = pd.DataFrame(data=save_dict_trader_total, columns=['Platform', '% of Total Traders'])

    save_dict_trader_daily = {"Date": [], "Platform": [], "% of Traders": []}
    for item in json.loads(api_data_sales_count_daily.text):
        save_dict_trader_daily["Date"].append(item["BLOCK_DATE"])
        save_dict_trader_daily["Platform"].append(item["PLATFORM_NAME"])
        save_dict_trader_daily["% of Traders"].append(item["TRADERS_PCT"])
    df_trader_daily = pd.DataFrame(data=save_dict_trader_daily,
                                         columns=['Date', 'Platform', '% of Traders'])

    trader_total, trader_daily = st.columns(2)
    # Total Traders
    with trader_total:
        trader_total_chart = alt.Chart(df_trader_total).mark_arc().encode(
            theta=alt.Theta(field="% of Total Traders", type="quantitative"),
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
                alt.Tooltip('% of Total Traders:Q', format='.2%')
            ]
        ).properties(title='% of Total Traders since 2022-10-19')
        st.altair_chart(trader_total_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Volume
    with trader_daily:
        trader_daily_chart = alt.Chart(df_trader_daily).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("% of Traders:Q", stack="normalize"),
            color=alt.Color('Platform:N', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2', '#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Platform:N'),
                alt.Tooltip('% of Traders:Q', format='.2%')
            ]
        ).properties(title='% of Daily Traders')
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