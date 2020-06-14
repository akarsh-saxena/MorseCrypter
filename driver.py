import importlib
import streamlit as st

import utils
from pages import home, text, image, guide

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

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def main():

    st.sidebar.title("Navigation")

    cache = utils.get_static_store()

    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    _reload_module(page)
    write_page(page, cache)

if __name__ == '__main__':
    main()
