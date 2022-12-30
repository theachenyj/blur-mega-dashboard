import streamlit as st
import requests
import pandas as pd
import json
import util.constants.urls as urls
import altair as alt

def trading_page():
    st.markdown("## Trading Analysis ")
    st.markdown("---")

    st.markdown("#### Sales Count")
    st.markdown(
        "Text..."
    )
    with st.container():
        save_dict = {"block_date": [], "count": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["count"].append(item["TRANSACTION_COUNTS"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'count'])
        c = alt.Chart(df).mark_bar().encode(x='block_date:T', y='count')
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "count_dod": []}
        web_data = requests.get(url=urls.url_sales_dod, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["count_dod"].append(item["TRANSACTION_COUNTS_DOD"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'count_dod'])
        c = alt.Chart(df).mark_bar().encode(
            alt.X('block_date:T'),
            alt.Y('count_dod:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.count_dod > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            )
        )
        st.altair_chart(c, use_container_width=True)
        st.markdown("---")

    st.markdown("#### Sales Volume")
    st.markdown(
        "Text..."
    )
    with st.container():
        save_dict = {"block_date": [], "volume": []}
        web_data = requests.get(url=urls.url_sales_trend, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["volume"].append(item["TRANSACTION_VOLUMES"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'volume'])
        c = alt.Chart(df).mark_bar().encode(x='block_date:T', y='volume')
        st.altair_chart(c, use_container_width=True)

    with st.container():
        save_dict = {"block_date": [], "volume_dod": []}
        web_data = requests.get(url=urls.url_sales_dod, headers={})
        for item in json.loads(web_data.text):
            save_dict["block_date"].append(item["BLOCK_DATE"])
            save_dict["volume_dod"].append(item["TRANSACTION_VOLUMES_DOD"])
        df = pd.DataFrame(data=save_dict, columns=['block_date', 'volume_dod'])
        c = alt.Chart(df).mark_bar().encode(
            alt.X('block_date:T'),
            alt.Y('volume_dod:Q', axis=alt.Axis(format='%')),
            color=alt.condition(
                alt.datum.volume_dod > 0,
                alt.value("green"),  # The positive color
                alt.value("red")  # The negative color
            )
        )
        st.altair_chart(c, use_container_width=True)



