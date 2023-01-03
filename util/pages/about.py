import streamlit as st
import requests
import json
import util.constants.urls as urls

def about_page():
    api_data_last_updated_time = requests.get(url=urls.url_last_updated, headers={})
    json_last_updated_time = json.loads(api_data_last_updated_time.text)
    last_updated_time = json_last_updated_time[0]["DATE"]

    st.markdown("## About ")
    st.markdown("---")

    # need a photo
    st.markdown("![ ](https://blur.io/homepage/img/logo.gif \"Blur\")")

    st.markdown("#### About ")
    st.markdown("This dashboard is made with love by [@TheaChenyj](https://twitter.com/Thea_Chenyj), in a response "
                "to MetricsDAO Analytics 📊 Bounty - [In the News Megadashboard](https://airtable.com/shrOhIcLvmeWrcMME/tblHEDBsMC1jourQf/viwMjFRVN6TcYfSuc/recLtLYUxoWXcm5Zs?backgroundColor=cyanLight&viewControls=on). "
                "I hope it serves as a valuable window into high-level metrics that display the vitality and growth of the Blur Ecosystem.")

    st.markdown("#### Methodology")
    st.markdown("Data is from Flipside's dataset ez_nft_sales. I created some relevant querys and drew it by existing APIs.")
    st.write("Data Last Updated: "+ last_updated_time)