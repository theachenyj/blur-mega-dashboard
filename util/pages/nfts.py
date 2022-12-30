import streamlit as st
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def nfts_page():
    st.markdown("## NFT Analysis ")
    st.markdown("---")

    st.markdown("#### Sales NFT Collection")
    st.markdown(
        "Text..."
    )
    with st.container():
        save_dict = {"block_date": [], "collections": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["collections"].append(item["TRANSACTION_COLLECTIONS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'collections'])
        c = alt.Chart(df).mark_bar().encode(x='block_date:T', y='collections')
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "collection_dod": []}
        web_data = requests.get(url=urls.url_sales_dod, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["collection_dod"].append(item["TRANSACTION_COLLECTIONS_DOD"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'collection_dod'])
        c = alt.Chart(df).mark_bar().encode(
            alt.X('block_date:T'),
            alt.Y('collection_dod:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.collection_dod > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            )
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    st.markdown("#### Sales NFTs")
    st.markdown(
        "Text..."
    )
    with st.container():
        save_dict = {"block_date": [], "nfts": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["nfts"].append(item["TRANSACTION_NFTS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'nfts'])
        c = alt.Chart(df).mark_bar().encode(x='block_date:T', y='nfts')
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "nft_dod": []}
        web_data = requests.get(url=urls.url_sales_dod, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["nft_dod"].append(item["TRANSACTION_NFTS_DOD"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'nft_dod'])
        c = alt.Chart(df).mark_bar().encode(
            alt.X('block_date:T'),
            alt.Y('nft_dod:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.nft_dod > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            )
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    # NFT Leaderboard
    # Total
    col1, col2 = st.columns(2)
    with col1:
        save_dict = {"NFT Collection": [], "Sales Count": []}
        web_data = requests.get(url=urls.url_top_nft_count, headers={})
        for item in json.loads(web_data.text):
            save_dict["NFT Collection"].append(item["NFT_ADDRESS"])
            save_dict["Sales Count"].append(item["SALES_COUNT"])
        df = pd.DataFrame(data=save_dict, columns=['NFT Collection', 'Sales Count'])

        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('Sales Count:Q'),
            y=alt.Y('NFT Collection:N', sort='-x')
        ).properties(title='Top NFT Collection Based on Sales Count')
        st.altair_chart(c, use_container_width=True)
    with col2:
        save_dict = {"NFT Collection": [], "Sales Volume": []}
        web_data = requests.get(url=urls.url_top_nft_volume, headers={})
        for item in json.loads(web_data.text):
            save_dict["NFT Collection"].append(item["NFT_ADDRESS"])
            save_dict["Sales Volume"].append(item["SALES_VOLUME"])
        df = pd.DataFrame(data=save_dict, columns=['NFT Collection', 'Sales Volume'])

        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('Sales Volume:Q'),
            y=alt.Y('NFT Collection:N', sort='-x')
        ).properties(title='Top NFT Collection Based on Sales Volume')
        st.altair_chart(c, use_container_width=True)

    # 24H
    col3, col4 = st.columns(2)
    with col3:
        save_dict = {"NFT Collection": [], "Sales Count": []}
        web_data = requests.get(url=urls.url_top_nft_count_24h, headers={})
        for item in json.loads(web_data.text):
            save_dict["NFT Collection"].append(item["NFT_ADDRESS"])
            save_dict["Sales Count"].append(item["SALES_COUNT"])
        df = pd.DataFrame(data=save_dict, columns=['NFT Collection', 'Sales Count'])

        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('Sales Count:Q'),
            y=alt.Y('NFT Collection:N', sort='-x')
        ).properties(title='24H Top NFT Collection Based on Sales Count')
        st.altair_chart(c, use_container_width=True)
    with col4:
        save_dict = {"NFT Collection": [], "Sales Volume": []}
        web_data = requests.get(url=urls.url_top_nft_volume_24h, headers={})
        for item in json.loads(web_data.text):
            save_dict["NFT Collection"].append(item["NFT_ADDRESS"])
            save_dict["Sales Volume"].append(item["SALES_VOLUME"])
        df = pd.DataFrame(data=save_dict, columns=['NFT Collection', 'Sales Volume'])

        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('Sales Volume:Q'),
            y=alt.Y('NFT Collection:N', sort='-x')
        ).properties(title='24H Top NFT Collection Based on Sales Volume')
        st.altair_chart(c, use_container_width=True)



