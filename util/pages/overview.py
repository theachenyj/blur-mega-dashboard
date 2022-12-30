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

    # KPIs for Blur
    st.markdown("#### KPIs ")
    st.markdown("These kinds of metric cards show Blur's KPIs. "
                "You can see total sales count, total sales volume, "
                "and total unique buyers and sellers since its inception. "
                "And current merics are calculated with last 24 hours' data.")

    api_data_total = requests.get(url=urls.url_total, headers={})
    json_data_total = json.loads(api_data_total.text)
    total_sales_count = millify(json_data_total[0]['TRANSACTION_COUNTS'])
    total_sales_volume = millify(json_data_total[0]['TRANSACTION_VOLUMES'])
    total_traders = millify(json_data_total[0]['TRADERS'])
    total_collections = millify(json_data_total[0]['TRANSACTION_COLLECTIONS'])

    api_data_current = requests.get(url=urls.url_current, headers={})
    json_data_current = json.loads(api_data_current.text)
    current_sales_count = millify(json_data_current[0]['TRANSACTION_COUNTS'])
    current_sales_volume = millify(json_data_current[0]['TRANSACTION_VOLUMES'])
    current_traders = millify(json_data_current[0]['TRADERS'])
    current_collections = millify(json_data_current[0]['TRANSACTION_COLLECTIONS'])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Sales Count", value=total_sales_count)
    col2.metric(label="Total Sales Volume in USD", value=total_sales_volume)
    col3.metric(label="Total Unique Traders", value=total_traders)
    col4.metric(label="Total Sales NFT Collections", value=total_collections)

    col5, col6, col7, col8 = st.columns(4)
    col5.metric(label="24H Sales Count", value=current_sales_count)
    col6.metric(label="24H Sales Volume in USD", value=current_sales_volume)
    col7.metric(label="24H Unique Traders", value=current_traders)
    col8.metric(label="24H Sales NFT Collections", value=current_collections)

    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("---")

    # Daily sales count v.s. Ether Price
    st.markdown("#### Daily Sales Count v.s. Ether Price")
    with st.container():
        save_dict = {"block_date": [], "count": [], "price": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["count"].append(item["TRANSACTION_COUNTS"])
            save_dict["price"].append(item["AVG_PRICE"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'count', 'price'])
        base = alt.Chart(df).encode(x='block_date:T')
        bar = base.mark_bar().encode(y='count:Q')
        line = base.mark_line(color='red').encode(y='price:Q')
        layer = alt.layer(bar, line).resolve_scale(y='independent')
        st.altair_chart(layer, use_container_width=True)
        st.markdown("---")

    # Daily sales volume v.s Ether Price
    st.markdown("#### Daily Sales Volume in $USD v.s. Ether Price")
    with st.container():
        save_dict = {"block_date": [], "volume": [], "price": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["volume"].append(item["TRANSACTION_VOLUMES"])
            save_dict["price"].append(item["AVG_PRICE"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'volume', 'price'])
        base = alt.Chart(df).encode(x='block_date:T')
        bar = base.mark_bar().encode(y='volume:Q')
        line = base.mark_line(color='red').encode(y='price:Q')
        layer = alt.layer(bar, line).resolve_scale(y='independent')
        st.altair_chart(layer, use_container_width=True)
        st.markdown("---")

    # Daily Unique Traders v.s. Ether Price
    st.markdown("#### Daily Unique Traders v.s. Ether Price")
    with st.container():
        save_dict = {"block_date": [], "trader": [], "price": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["trader"].append(item["TRADERS"])
            save_dict["price"].append(item["AVG_PRICE"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'trader', 'price'])
        base = alt.Chart(df).encode(x='block_date:T')
        bar = base.mark_bar().encode(y='trader:Q')
        line = base.mark_line(color='red').encode(y='price:Q')
        layer = alt.layer(bar, line).resolve_scale(y='independent')
        st.altair_chart(layer, use_container_width=True)
        st.markdown("---")

    # Blur's network penetration
    st.markdown("#### % of Ethereum NFT traders that have used Blur")
    st.markdown(
        "Blur’s Network Penetration measures the share of total wallets that have sold or bought NFTs on Blur "
        "versus the total amount of active wallets on Ethereum since Oct. 19, 2022 (  the same day that Blur launched)."
    )
    with st.container():
        save_dict = {"block_date": [], "blur_share": []}
        web_data = requests.get(url=urls.url_share_trader, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["blur_share"].append(item["BLUR_SHARE"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'blur_share'])
        c = alt.Chart(df).mark_area().encode(
            alt.X('block_date:T'),
            alt.Y('blur_share:Q', axis=alt.Axis(format='%'))
        )
        st.altair_chart(c, use_container_width=True)