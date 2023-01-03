import streamlit as st
from millify import millify
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def overview_page():
    st.markdown("## Overview ")
    st.markdown(
        "Blur is the NFT marketplace launched on Ethereum since Oct 19 2022. "
        "It's for pro traders and benefits them with zero cost and faster trading speed."
    )
    st.markdown("---")
    st.markdown(
        "These kinds of charts show the overall performance of Blur's KPIs, "
        "including sales count, sales volume, traders and sales NFT collections. "
        "You can have a more deeper dive for a more specific view by selecting different pages in the sidebar. "
        "We cover **Trading Analysis**, **Trader Analysis**, **NFT Analysis** and **Marketplace Comparison**. "
    )

    # Metrics

    api_data_metric_total = requests.get(url=urls.url_total, headers={})
    json_metric_total = json.loads(api_data_metric_total.text)
    total_sales_count = millify(json_metric_total[0]['TRANSACTION_COUNTS'])
    total_sales_volume = millify(json_metric_total[0]['TRANSACTION_VOLUMES'])
    total_traders = millify(json_metric_total[0]['TRADERS'])
    total_collections = millify(json_metric_total[0]['TRANSACTION_COLLECTIONS'])

    api_data_metric_current = requests.get(url=urls.url_current, headers={})
    json_metric_current = json.loads(api_data_metric_current.text)
    current_sales_count = millify(json_metric_current[0]['TRANSACTION_COUNTS'])
    current_sales_volume = millify(json_metric_current[0]['TRANSACTION_VOLUMES'])
    current_traders = millify(json_metric_current[0]['TRADERS'])
    current_collections = millify(json_metric_current[0]['TRANSACTION_COLLECTIONS'])

    metric_total_1, metric_total_2, metric_total_3, metric_total_4 = st.columns(4)
    metric_total_1.metric(label="Total Sales Count", value=total_sales_count)
    metric_total_2.metric(label="Total Sales Volume in USD", value=total_sales_volume)
    metric_total_3.metric(label="Total Unique Traders", value=total_traders)
    metric_total_4.metric(label="Total Sales NFT Collections", value=total_collections)

    metric_current_1, metric_current_2, metric_current_3, metric_current_4 = st.columns(4)
    metric_current_1.metric(label="24H Sales Count", value=current_sales_count)
    metric_current_2.metric(label="24H Sales Volume in USD", value=current_sales_volume)
    metric_current_3.metric(label="24H Unique Traders", value=current_traders)
    metric_current_4.metric(label="24H Sales NFT Collections", value=current_collections)

    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown(" ")

    # Daily sales count v.s. Ether Price
    api_data_sales_trend = requests.get(url=urls.url_sales_trend, headers={})
    save_dict_sales_trend_count = {"Date": [], "Sales Count": [], "Ether Price": []}
    for item in json.loads(api_data_sales_trend.text):
        save_dict_sales_trend_count["Date"].append(item["BLOCK_DATE"])
        save_dict_sales_trend_count["Sales Count"].append(item["TRANSACTION_COUNTS"])
        save_dict_sales_trend_count["Ether Price"].append(item["AVG_PRICE"])
    total_sales_count_df = pd.DataFrame(data=save_dict_sales_trend_count, columns=['Date', 'Sales Count', 'Ether Price'])

    sales_trend_count = st.container()
    with sales_trend_count:
        sales_trend_count_base = alt.Chart(total_sales_count_df).encode(x=alt.X('Date:T', axis=alt.Axis(title=None)))
        sales_trend_count_area = sales_trend_count_base.mark_area(color='#E4831E').encode(
            y='Sales Count:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Sales Count:Q', format=',')
            ]
        )
        sales_trend_count_line = sales_trend_count_base.mark_line(color='grey').encode(
            y='Ether Price:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Ether Price:Q', format='$,.2f')
            ]
        )
        sales_trend_count_layer = alt.layer(
            sales_trend_count_area,
            sales_trend_count_line
        ).resolve_scale(y='independent').properties(title='Daily Sales Count v.s. Ether Price')

        st.altair_chart(sales_trend_count_layer, use_container_width=True)
        st.markdown(" ")

    # Daily sales volume v.s Ether Price
    st.markdown(" ")
    save_dict_sales_trend_volume = {"Date": [], "Sales Volume": [], "Ether Price": []}
    for item in json.loads(api_data_sales_trend.text):
        save_dict_sales_trend_volume["Date"].append(item["BLOCK_DATE"])
        save_dict_sales_trend_volume["Sales Volume"].append(item["TRANSACTION_VOLUMES"])
        save_dict_sales_trend_volume["Ether Price"].append(item["AVG_PRICE"])
    total_sales_volume_df = pd.DataFrame(data=save_dict_sales_trend_volume,
                                        columns=['Date', 'Sales Volume', 'Ether Price'])

    sales_trend_volume = st.container()
    with sales_trend_volume:
        sales_trend_volume_base = alt.Chart(total_sales_volume_df).encode(x=alt.X('Date:T', axis=alt.Axis(title=None)))
        sales_trend_volume_area = sales_trend_volume_base.mark_area(color='#E4831E').encode(
            y='Sales Volume:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Sales Volume:Q', format='$,')
            ]
        )
        sales_trend_volume_line = sales_trend_volume_base.mark_line(color='grey').encode(
            y='Ether Price:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Ether Price:Q', format='$,.2f')
            ]
        )
        sales_trend_volume_layer = alt.layer(
            sales_trend_volume_area,
            sales_trend_volume_line
        ).resolve_scale(y='independent').properties(title='Daily Sales Volume in USD v.s. Ether Price')

        st.altair_chart(sales_trend_volume_layer, use_container_width=True)
        st.markdown(" ")

    # Daily Unique Traders v.s. Ether Price
    st.markdown(" ")
    save_dict_trader_trend = {"Date": [], "Traders": [], "Ether Price": []}
    for item in json.loads(api_data_sales_trend.text):
        save_dict_trader_trend["Date"].append(item["BLOCK_DATE"])
        save_dict_trader_trend["Traders"].append(item["TRADERS"])
        save_dict_trader_trend["Ether Price"].append(item["AVG_PRICE"])
    df_trader_trend = pd.DataFrame(data=save_dict_trader_trend, columns=['Date', 'Traders', 'Ether Price'])

    trader_trend = st.container()
    with trader_trend:
        trader_trend_base = alt.Chart(df_trader_trend).encode(x=alt.X('Date:T', axis=alt.Axis(title=None)))
        trader_trend_area = trader_trend_base.mark_area(color='#E4831E').encode(
            y='Traders:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Traders:Q', format=',')
            ]
        )
        trader_trend_line = trader_trend_base.mark_line(color='grey').encode(
            y='Ether Price:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Ether Price:Q', format='$,.2f')
            ]
        )
        trader_trend_layer = alt.layer(
            trader_trend_area,
            trader_trend_line
        ).resolve_scale(y='independent').properties(title='Daily Traders v.s. Ether Price')
        st.altair_chart(trader_trend_layer, use_container_width=True)
        st.markdown(" ")

    # Daily Sales Collections v.s. Ether Price
    st.markdown(" ")
    save_dict_collections_trend = {"Date": [], "Sales Collections": [], "Ether Price": []}
    for item in json.loads(api_data_sales_trend.text):
        save_dict_collections_trend["Date"].append(item["BLOCK_DATE"])
        save_dict_collections_trend["Sales Collections"].append(item["TRANSACTION_COLLECTIONS"])
        save_dict_collections_trend["Ether Price"].append(item["AVG_PRICE"])
    df_collections_trend = pd.DataFrame(data=save_dict_collections_trend, columns=['Date', 'Sales Collections', 'Ether Price'])

    collections_trend = st.container()
    with collections_trend:
        collections_trend_base = alt.Chart(df_collections_trend).encode(x=alt.X('Date:T', axis=alt.Axis(title=None)))
        collections_trend_area = collections_trend_base.mark_area(color='#E4831E').encode(
            y='Sales Collections:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Sales Collections:Q', format=',')
            ]
        )
        collections_trend_line = trader_trend_base.mark_line(color='grey').encode(
            y='Ether Price:Q',
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('Ether Price:Q', format='$,.2f')
            ]
        )
        collections_trend_layer = alt.layer(
            collections_trend_area,
            collections_trend_line
        ).resolve_scale(y='independent').properties(title='Daily Sales Collections v.s. Ether Price')
        st.altair_chart(collections_trend_layer, use_container_width=True)
        st.markdown(" ")

    # Blur's network penetration
    st.markdown(" ")
    save_dict_share_trader = {"Date": [], "% of Total Traders on Ethereum": []}
    api_data_share_trader = requests.get(url=urls.url_share_trader, headers={})
    for item in json.loads(api_data_share_trader.text):
        save_dict_share_trader["Date"].append(item["BLOCK_DATE"])
        save_dict_share_trader["% of Total Traders on Ethereum"].append(item["BLUR_SHARE"])
    df_trader_share = pd.DataFrame(data=save_dict_share_trader, columns=['Date', '% of Total Traders on Ethereum'])

    trader_share = st.container()

    with trader_share:
        trader_share_chart = alt.Chart(df_trader_share).mark_area(color='#E4831E').encode(
            x=alt.X("Date:T", axis=alt.Axis(title=None)),
            y=alt.Y("% of Total Traders on Ethereum:Q", axis=alt.Axis(format='%')),
            tooltip=[
                alt.Tooltip('Date:T'),
                alt.Tooltip('% of Total Traders on Ethereum:Q', format='.2%')
            ]
        ).properties(title='% of Total NFT traders on Ethereum')
        st.altair_chart(trader_share_chart, use_container_width=True)
        st.markdown(" ")