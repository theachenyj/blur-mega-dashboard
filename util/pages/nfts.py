import streamlit as st
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def nfts_page():
    st.markdown("## NFT Analysis ")
    st.markdown("---")

    # NFT Leaderboard
    # Total
    save_dict_top_nft_count = {"NFT Collection": [], "Sales Count": []}
    api_data_top_nft_count = requests.get(url=urls.url_top_nft_count, headers={})
    for item in json.loads(api_data_top_nft_count.text):
        save_dict_top_nft_count["NFT Collection"].append(item["PROJECT_NAME"])
        save_dict_top_nft_count["Sales Count"].append(item["SALES_COUNT"])
    df_top_nft_count = pd.DataFrame(data=save_dict_top_nft_count, columns=['NFT Collection', 'Sales Count'])

    save_dict_top_nft_volume = {"NFT Collection": [], "Sales Volume": []}
    api_data_top_nft_volume = requests.get(url=urls.url_top_nft_volume, headers={})
    for item in json.loads(api_data_top_nft_volume.text):
        save_dict_top_nft_volume["NFT Collection"].append(item["PROJECT_NAME"])
        save_dict_top_nft_volume["Sales Volume"].append(item["SALES_VOLUME"])
    df_top_nft_volume = pd.DataFrame(data=save_dict_top_nft_volume, columns=['NFT Collection', 'Sales Volume'])

    top_nft_count, top_nft_volume = st.columns(2)
    with top_nft_count:
        top_nft_count_chart = alt.Chart(df_top_nft_count).mark_bar(color='#E4831E').encode(
            x=alt.X('Sales Count:Q', axis=alt.Axis(title=None)),
            y=alt.Y('NFT Collection:N', sort='-x'),
            tooltip=[
                alt.Tooltip('NFT Collection:N'),
                alt.Tooltip('Sales Count:Q', format=',')
            ]
        ).properties(title='Top NFT Collection Based on Sales Count since 2022-10-19')
        st.altair_chart(top_nft_count_chart, use_container_width=True)
        st.markdown(" ")

    with top_nft_volume:
        top_nft_volume_chart = alt.Chart(df_top_nft_volume).mark_bar(color='#E4831E').encode(
            x=alt.X('Sales Volume:Q', axis=alt.Axis(title=None)),
            y=alt.Y('NFT Collection:N', sort='-x'),
            tooltip=[
                alt.Tooltip('NFT Collection:N'),
                alt.Tooltip('Sales Volume:Q', format='$,')
            ]
        ).properties(title='Top NFT Collection Based on Sales Volume since 2022-10-19')
        st.altair_chart(top_nft_volume_chart, use_container_width=True)
        st.markdown(" ")

    # 24H
    save_dict_top_nft_count_24h = {"NFT Collection": [], "Sales Count": []}
    api_data_top_nft_count_24h = requests.get(url=urls.url_top_nft_count_24h, headers={})
    for item in json.loads(api_data_top_nft_count_24h.text):
        save_dict_top_nft_count_24h["NFT Collection"].append(item["PROJECT_NAME"])
        save_dict_top_nft_count_24h["Sales Count"].append(item["SALES_COUNT"])
    df_top_nft_count_24h = pd.DataFrame(data=save_dict_top_nft_count_24h, columns=['NFT Collection', 'Sales Count'])

    save_dict_top_nft_volume_24h = {"NFT Collection": [], "Sales Volume": []}
    api_data_top_nft_volume_24h = requests.get(url=urls.url_top_nft_volume_24h, headers={})
    for item in json.loads(api_data_top_nft_volume_24h.text):
        save_dict_top_nft_volume_24h["NFT Collection"].append(item["PROJECT_NAME"])
        save_dict_top_nft_volume_24h["Sales Volume"].append(item["SALES_VOLUME"])
    df_top_nft_volume_24h = pd.DataFrame(data=save_dict_top_nft_volume_24h, columns=['NFT Collection', 'Sales Volume'])

    top_nft_count_24h, top_nft_volume_24h = st.columns(2)
    with top_nft_count_24h:
        top_nft_count_24h_chart = alt.Chart(df_top_nft_count_24h).mark_bar(color='#E4831E').encode(
            x=alt.X('Sales Count:Q', axis=alt.Axis(title=None)),
            y=alt.Y('NFT Collection:N', sort='-x'),
            tooltip=[
                alt.Tooltip('NFT Collection:N'),
                alt.Tooltip('Sales Count:Q', format=',')
            ]
        ).properties(title='24H Top NFT Collection Based on Sales Count')
        st.altair_chart(top_nft_count_24h_chart, use_container_width=True)
        st.markdown(" ")

    with top_nft_volume_24h:
        top_nft_volume_24h_chart = alt.Chart(df_top_nft_volume_24h).mark_bar(color='#E4831E').encode(
            x=alt.X('Sales Volume:Q', axis=alt.Axis(title=None)),
            y=alt.Y('NFT Collection:N', sort='-x'),
            tooltip=[
                alt.Tooltip('NFT Collection:N'),
                alt.Tooltip('Sales Volume:Q', format='$,')
            ]
        ).properties(title='24H Top NFT Collection Based on Sales Volume')
        st.altair_chart(top_nft_volume_24h_chart, use_container_width=True)
        st.markdown(" ")