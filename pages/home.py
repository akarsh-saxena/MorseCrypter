import streamlit as st
import utils

def write(_):

    cache = utils.get_static_store()
    cache['copy'] = None

    st.image("https://hackster.imgix.net/uploads/attachments/583295/blob_H3sQ6UPdXT.blob?auto=compress%2Cformat&w=900&h=675&fit=min", use_column_width=True)

    st.markdown("""
        <br />

        # MorseCrypter
        ## Encode any text (even from images) to morse code!

        <br />
    """, unsafe_allow_html=True)

    st.success("""
        ## Usage

        ***From the left navigation menu, select the source for the input.***
    """)

if __name__ == "__main__":
    write(_)