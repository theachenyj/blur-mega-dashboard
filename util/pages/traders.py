import streamlit as st
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def traders_page():
    st.markdown("## Trader Analysis ")
    st.markdown("---")

    # The Percentage(%) Increase/Decrease of Traders
    st.markdown(" ")
    api_data_trader_dod = requests.get(url=urls.url_trader_dod, headers={})
    save_dict_trader_dod = {"Date": [], "Change": []}
    for item in json.loads(api_data_trader_dod.text):
        save_dict_trader_dod["Date"].append(item["BLOCK_WEEK"])
        save_dict_trader_dod["Change"].append(item["TRADER_DOD"])
    df_trader_dod = pd.DataFrame(data=save_dict_trader_dod, columns=['Date', 'Change'])

    trader_dod = st.container()
    with trader_dod:
        trader_dod_chart = alt.Chart(df_trader_dod).mark_bar(size=30).encode(
            alt.X('Date:T', axis=alt.Axis(title=None)),
            alt.Y('Change:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.Change > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            )
        ).properties(title='The Percentage(%) Increase/Decrease of Traders')
        st.altair_chart(trader_dod_chart, use_container_width=True)
        st.markdown(" ")

    # Unique Traders
    save_dict_daily_unique_trader = {"Date": [], "Traders": []}
    api_data_daily_unique_trader = requests.get(url=urls.url_sales_trend, headers={})
    for item in json.loads(api_data_daily_unique_trader.text):
        save_dict_daily_unique_trader["Date"].append(item["BLOCK_DATE"])
        save_dict_daily_unique_trader["Traders"].append(item["TRADERS"])
    df_daily_unique_trader = pd.DataFrame(data=save_dict_daily_unique_trader, columns=['Date', 'Traders'])

    daily_unique_trader = st.container()
    with daily_unique_trader:
        daily_unique_trader_chart = alt.Chart(df_daily_unique_trader).mark_bar(color='#E4831E').encode(
            x=alt.X('Date:T', axis=alt.Axis(title=None)),
            y='Traders:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Traders:Q', format=',')
            ]
        ).properties(title='Daily Unique Traders')
        st.altair_chart(daily_unique_trader_chart, use_container_width=True)
        st.markdown(" ")

    # Unique Buyer/Seller
    st.markdown(" ")
    save_dict_buyer_seller = {"Date": [], "Trader Type": [], "Traders": []}
    api_data_buyer_seller = requests.get(url=urls.url_trader_comparison, headers={})
    for item in json.loads(api_data_buyer_seller.text):
        save_dict_buyer_seller["Date"].append(item["BLOCK_DATE"])
        save_dict_buyer_seller["Trader Type"].append(item["TRADER_TYPE"])
        save_dict_buyer_seller["Traders"].append(item["WALLETS"])
    df_buyer_seller = pd.DataFrame(data=save_dict_buyer_seller, columns=['Date', 'Trader Type', 'Traders'])

    daily_buyer_seller, daily_buyer_seller_normalize = st.columns(2)
    with daily_buyer_seller:
        daily_buyer_seller_chart = alt.Chart(df_buyer_seller).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Traders:Q"),
            color=alt.Color('Trader Type', scale=alt.Scale(
                domain=['Buyer', 'Seller'],
                range=['#E4831E', '#D32DF3']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Trader Type:N'),
                alt.Tooltip('Traders:Q', format=',')
            ]
        ).properties(title='Daily Buyer&Seller')

        st.altair_chart(daily_buyer_seller_chart, use_container_width=True)
        st.markdown(" ")

    with daily_buyer_seller_normalize:
        daily_buyer_seller_normalize_chart = alt.Chart(df_buyer_seller).mark_area().encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Traders:Q", stack="normalize"),
            color=alt.Color('Trader Type', scale=alt.Scale(
                domain=['Buyer', 'Seller'],
                range=['#E4831E', '#D32DF3']
            )),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Trader Type:N'),
                alt.Tooltip('Traders:Q', format=',')
            ]
        ).properties(title='Daily Buyer&Seller Normalize')

        st.altair_chart(daily_buyer_seller_normalize_chart, use_container_width=True)
        st.markdown(" ")

    # Daily Buyer/Seller Ratio
    st.markdown(" ")
    save_dict_buyer_seller_ratio = {"Date": [], "Ratio": []}
    api_data_buyer_seller_ratio = requests.get(url=urls.url_trader_ratio, headers={})

    for item in json.loads(api_data_buyer_seller_ratio.text):
        save_dict_buyer_seller_ratio["Date"].append(item["BLOCK_DATE"])
        save_dict_buyer_seller_ratio["Ratio"].append(item["BUYER_SELLER_RATIO"])
    df_buyer_seller_ratio = pd.DataFrame(data=save_dict_buyer_seller_ratio, columns=['Date', 'Ratio'])

    daily_buyer_seller_ratio = st.container()
    with daily_buyer_seller_ratio:
        daily_buyer_seller_ratio_chart = alt.Chart(df_buyer_seller_ratio).mark_line(color='#E4831E').encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("Ratio:Q", axis=alt.Axis(format='%')),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Ratio:Q', format='.2%')
            ]
        ).properties(title='Daily Buyer/Seller Ratio')
        st.altair_chart(daily_buyer_seller_ratio_chart, use_container_width=True)
        st.markdown(" ")

    # User Acquisition
    # Cumulative Traders
    # New Traders
    st.markdown(" ")
    save_dict_trader_cum = {"Date": [], "Cumulative Traders": []}
    api_data_trader_acq = requests.get(url=urls.url_trader_acq, headers={})
    for item in json.loads(api_data_trader_acq.text):
        save_dict_trader_cum["Date"].append(item["BLOCK_DATE"])
        save_dict_trader_cum["Cumulative Traders"].append(item["CUM_WALLTES"])
    df_trader_cum = pd.DataFrame(data=save_dict_trader_cum, columns=['Date', 'Cumulative Traders'])

    save_dict_trader_new = {"Date": [], "New Traders": []}
    for item in json.loads(api_data_trader_acq.text):
        save_dict_trader_new["Date"].append(item["BLOCK_DATE"])
        save_dict_trader_new["New Traders"].append(item["NEW_WALLETS"])
    df_trader_new = pd.DataFrame(data=save_dict_trader_new, columns=['Date', 'New Traders'])

    trader_new, trader_cum = st.columns(2)
    with trader_new:
        trader_new_chart = alt.Chart(df_trader_new).mark_bar(color='#E4831E').encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y="New Traders:Q",
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('New Traders:Q', format=',')
            ]
        ).properties(title='New Traders')
        st.altair_chart(trader_new_chart, use_container_width=True)
        st.markdown(" ")

    with trader_cum:
        trader_cum_chart = alt.Chart(df_trader_cum).mark_area(color='#E4831E').encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y="Cumulative Traders:Q",
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Cumulative Traders:Q', format=',')
            ]
        ).properties(title='Cumulative Traders')
        st.altair_chart(trader_cum_chart, use_container_width=True)
        st.markdown(" ")

    # User Group
    st.markdown(" ")
    # Trader Group Based on Sales Count
    save_dict_trader_group_count = {"Sales Count": [], "% of Total Traders": [], "Rankings": []}
    api_data_trader_group_count = requests.get(url=urls.url_trader_gp_count, headers={})
    for item in json.loads(api_data_trader_group_count.text):
        save_dict_trader_group_count["Sales Count"].append(item["SALES_COUNT_TIER"])
        save_dict_trader_group_count["% of Total Traders"].append(item["PCT"])
        save_dict_trader_group_count["Rankings"].append(item["RANKINGS"])
    df_trader_group_count = pd.DataFrame(data=save_dict_trader_group_count, columns=['Sales Count', '% of Total Traders', 'Rankings'])

    save_dict_trader_group_volume = {"Sales Volume": [], "% of Total Traders": [], "Rankings": []}
    api_data_trader_group_volume = requests.get(url=urls.url_trader_gp_volume, headers={})
    for item in json.loads(api_data_trader_group_volume.text):
        save_dict_trader_group_volume["Sales Volume"].append(item["SALES_VOLUME_TIER"])
        save_dict_trader_group_volume["% of Total Traders"].append(item["PCT"])
        save_dict_trader_group_volume["Rankings"].append(item["RANKINGS"])
    df_trader_group_volume = pd.DataFrame(data=save_dict_trader_group_volume,
                                         columns=['Sales Volume', '% of Total Traders', 'Rankings'])

    trader_group_count, trader_group_volume = st.columns(2)
    with trader_group_count:
        trader_group_count_chart = alt.Chart(df_trader_group_count).mark_bar(color='#E4831E').encode(
            x=alt.X("Sales Count:N", sort=alt.SortField(field='Rankings', order='ascending'),
                    axis=alt.Axis(title=None)),
            y=alt.Y("% of Total Traders:Q", axis=alt.Axis(format='%')),
            tooltip=[
                alt.Tooltip('Sales Count:N'),
                alt.Tooltip('% of Total Traders:Q', format='.2%')
            ]
        ).properties(title='User Grouping Baseed on Sales Count')
        st.altair_chart(trader_group_count_chart, use_container_width=True)
        st.markdown(" ")

    with trader_group_volume:
        trader_group_volume_chart = alt.Chart(df_trader_group_volume).mark_bar(color='#E4831E').encode(
            x=alt.X("Sales Volume:N", sort=alt.SortField(field='Rankings', order='ascending'),
                    axis=alt.Axis(title=None)),
            y=alt.Y("% of Total Traders:Q", axis=alt.Axis(format='%')),
            tooltip=[
                alt.Tooltip('Sales Volume:N'),
                alt.Tooltip('% of Total Traders:Q', format='.2%')
            ]
        ).properties(title='User Grouping Baseed on Sales Volume')
        st.altair_chart(trader_group_volume_chart, use_container_width=True)
        st.markdown(" ")

    # The First Platform of Blur's Traders
    st.markdown(" ")
    save_dict_source = {"First Platform": [], "% of Total Traders": []}
    api_data_source = requests.get(url=urls.url_trader_from, headers={})
    for item in json.loads(api_data_source.text):
        save_dict_source["First Platform"].append(item["FIRST_PLATFORM"])
        save_dict_source["% of Total Traders"].append(item["PCT"])
    df_source = pd.DataFrame(data=save_dict_source, columns=['First Platform', '% of Total Traders'])

    source=st.container()
    with source:
        source_chart = alt.Chart(df_source).mark_bar().encode(
            y=alt.Y('% of Total Traders:Q', axis=alt.Axis(format='%')),
            x=alt.X('First Platform:N', axis=alt.Axis(title=None), sort='-y'),
            color=alt.Color('First Platform', scale=alt.Scale(
                domain=['opensea', 'x2y2', 'blur', 'looksrare', 'sudoswap', 'nftx', 'rarible', 'larva labs'],
                range=['#4C81DF', '#4E31C2' ,'#E4831E', '#74CD61', '#B7B8FD', '#D62C7B', '#F4D834', '#DB05AF']
            )),
            tooltip=[
                alt.Tooltip('First Platform:N'),
                alt.Tooltip('% of Total Traders:Q', format='.2%')
            ]
        ).properties(title='The First Platform of Blur\'s Traders')
        st.altair_chart(source_chart, use_container_width=True)
    st.markdown(" ")