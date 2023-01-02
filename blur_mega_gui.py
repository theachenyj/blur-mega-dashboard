import streamlit as st

from util.pages.overview import overview_page
from util.pages.trading_page import trading_page
from util.pages.nfts import nfts_page
from util.pages.traders import traders_page
from util.pages.comparison import comparison_page

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.set_page_config(page_title="blur", layout="wide")

        st.sidebar.markdown("## Blur")
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        app["function"]()


app = MultiApp()

app.add_app("Overview", overview_page)
app.add_app("Trading Activity", trading_page)
app.add_app("Trader Analysis", traders_page)
app.add_app("NFT Analysis", nfts_page)
app.add_app("Marketplace Comparison", comparison_page)

app.run()