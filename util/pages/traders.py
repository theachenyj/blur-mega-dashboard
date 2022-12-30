import streamlit as st
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def traders_page():
    st.markdown("## Trader Analysis ")
    st.markdown("---")

    st.markdown("#### Unique Traders")
    st.markdown(
        "Text..."
    )
    with st.container():
        save_dict = {"block_date": [], "trader": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["trader"].append(item["TRADERS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'trader'])
        c = alt.Chart(df).mark_bar().encode(x='block_date:T', y='trader')
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "trader_dod": []}
        web_data = requests.get(url=urls.url_trader_dod, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["trader_dod"].append(item["TRADER_DOD"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'trader_dod'])
        c = alt.Chart(df).mark_bar().encode(
            alt.X('block_date:T'),
            alt.Y('trader_dod:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.trader_dod > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            )
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    st.markdown("#### Unique Buyer/Seller")
    st.markdown(
            "Text..."
        )
    with st.container():
        save_dict = {"block_date": [], "trader_type": [], "wallets": []}
        web_data = requests.get(url=urls.url_trader_comparison, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["trader_type"].append(item["TRADER_TYPE"])
            save_dict["wallets"].append(item["WALLETS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'trader_type', 'wallets'])
        c = alt.Chart(df).mark_area().encode(
            x="block_date:T",
            y="wallets:Q",
            color="trader_type:N"
        )
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "trader_type": [], "wallets": []}
        web_data = requests.get(url=urls.url_trader_comparison, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["trader_type"].append(item["TRADER_TYPE"])
            save_dict["wallets"].append(item["WALLETS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'trader_type', 'wallets'])
        c = alt.Chart(df).mark_area().encode(
            x="block_date:T",
            y=alt.Y("wallets:Q", stack="normalize"),
            color="trader_type:N"
        )
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "ratio": []}
        web_data = requests.get(url=urls.url_trader_ratio, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["ratio"].append(item["BUYER_SELLER_RATIO"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'ratio'])
        c = alt.Chart(df).mark_line().encode(
            x="block_date:T",
            y="ratio:Q"
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    st.markdown("#### User Acquisition")
    st.markdown(
            "Text..."
        )
    with st.container():
        save_dict = {"block_date": [], "Cumulative Wallets": []}
        web_data = requests.get(url=urls.url_trader_acq, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["Cumulative Wallets"].append(item["CUM_WALLTES"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'Cumulative Wallets'])
        c = alt.Chart(df).mark_area().encode(
            x="block_date:T",
            y="Cumulative Wallets:Q"
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    with st.container():
        save_dict = {"block_date": [], "New Wallets": []}
        web_data = requests.get(url=urls.url_trader_acq, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["New Wallets"].append(item["NEW_WALLETS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'New Wallets'])
        c = alt.Chart(df).mark_bar().encode(
            x="block_date:T",
            y="New Wallets:Q"
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    st.markdown("#### User Group")
    st.markdown(
        "Text..."
    )
    col1, col2 = st.columns(2)
    with col1:
        save_dict = {"group": [], "Percent of Total": [], "rankings": []}
        web_data = requests.get(url=urls.url_trader_gp_count, headers={})
        for item in json.loads(web_data.text):
            save_dict["group"].append(item["SALES_COUNT_TIER"])
            save_dict["Percent of Total"].append(item["PCT"])
            save_dict["rankings"].append(item["RANKINGS"])
        df = pd.DataFrame(data=save_dict, columns=['group', 'Percent of Total', 'rankings'])

        c = alt.Chart(df).mark_bar().encode(
            y=alt.Y('Percent of Total:Q', axis=alt.Axis(format='%')),
            x=alt.X('group:N', sort=alt.SortField(field='rankings', order='ascending'))
        ).properties(title='Trader Group Based on Sales Count')
        st.altair_chart(c, use_container_width=True)

    with col2:
        save_dict = {"group": [], "Percent of Total": [], "rankings": []}
        web_data = requests.get(url=urls.url_trader_gp_volume, headers={})
        for item in json.loads(web_data.text):
            save_dict["group"].append(item["SALES_VOLUME_TIER"])
            save_dict["Percent of Total"].append(item["PCT"])
            save_dict["rankings"].append(item["RANKINGS"])
        df = pd.DataFrame(data=save_dict, columns=['group', 'Percent of Total', 'rankings'])

        c = alt.Chart(df).mark_bar().encode(
            y=alt.Y('Percent of Total:Q', axis=alt.Axis(format='%')),
            x=alt.X('group:N', sort=alt.SortField(field='rankings', order='ascending'))
        ).properties(title='Trader Group Based on Sales Volume')
        st.altair_chart(c, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        save_dict = {"First Platform": [], "Percent of Total": []}
        web_data = requests.get(url=urls.url_trader_from, headers={})
        for item in json.loads(web_data.text):
            save_dict["First Platform"].append(item["FIRST_PLATFORM"])
            save_dict["Percent of Total"].append(item["PCT"])
        df = pd.DataFrame(data=save_dict, columns=['First Platform', 'Percent of Total'])

        c = alt.Chart(df).mark_bar().encode(
            y=alt.Y('Percent of Total:Q', axis=alt.Axis(format='%')),
            x=alt.X('First Platform:N')
        ).properties(title='The First Platform of Blur\'s Trader')
        st.altair_chart(c, use_container_width=True)
    st.markdown("---")

    st.markdown("#### Trader Leaderboard")
    st.markdown(
        "Text..."
    )
    col5, col6 = st.columns(2)
    with col5:
        save_dict = {"wallet": [], "sales count": []}
        web_data = requests.get(url=urls.url_top_trader_count, headers={})
        for item in json.loads(web_data.text):
            save_dict["wallet"].append(item["WALLET"])
            save_dict["sales count"].append(item["SALES_COUNT"])
        df = pd.DataFrame(data=save_dict, columns=['wallet', 'sales count'])

        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('sales count:Q'),
            y=alt.Y('wallet:N', sort='-x')
        ).properties(title='Top Traders Based on Sales Counts')
        st.altair_chart(c, use_container_width=True)

    with col6:
        save_dict = {"wallet": [], "sales volume": []}
        web_data = requests.get(url=urls.url_top_trader_volume, headers={})
        for item in json.loads(web_data.text):
            save_dict["wallet"].append(item["WALLET"])
            save_dict["sales volume"].append(item["SALES_VOLUME"])
        df = pd.DataFrame(data=save_dict, columns=['wallet', 'sales volume'])

        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('sales volume:Q'),
            y=alt.Y('wallet:N', sort='-x')
        ).properties(title='Top Traders Based on Sales Volume')
        st.altair_chart(c, use_container_width=True)