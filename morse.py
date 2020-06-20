import importlib
import streamlit as st

import src.utils
from src.pages import home, text, image, guide

def write_page(page, cache):  # pylint: disable=redefined-outer-name
    """Writes the specified page/module
    Our multipage app is structured into sub-files with a `def write()` function
    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    # _reload_module(page)
    page.write(cache)

def _reload_module(page):
    """Reloads the specified module/ page
    Arguments:
        page {module} -- A page/ module
    """
    try:
        importlib.import_module(page.__name__)
        importlib.reload(page)
    except ImportError as _:
        print('Exception')

PAGES = {
    'Home': home,
    "Text": text,
    'Image': image,
    'Guide': guide
}

with open("src/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def main():

    st.sidebar.title("Navigation")

    cache = src.utils.get_static_store()

    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    _reload_module(page)
    write_page(page, cache)

    st.sidebar.markdown('<br />', unsafe_allow_html=True)

    st.sidebar.title("About")

    st.sidebar.info("""

        By Akarsh Saxena

        For source code, visit
        [Github](https://github.com/akarsh-saxena/MorseCrypter)
    """)

    st.sidebar.markdown('<br />', unsafe_allow_html=True)

    st.sidebar.title("Reach me out")

    st.sidebar.markdown("""

    <a href="https://bit.ly/AkarshSaxena" target="_blank"><img  class="connect_button" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg"></a>
    <a href="https://bit.ly/AkarshLinkedIn" target="_blank"><img  class="connect_button"  style="{margin-left: 5%;}" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-tile.svg"></a>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
