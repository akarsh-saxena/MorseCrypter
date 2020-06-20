import streamlit as st
from .. import utils

def write(_):

    cache = utils.get_static_store()
    cache['copy'] = None

    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/800px-International_Morse_Code.svg.png', use_column_width=True)

    st.info("""

        For list of all supported characters, visit [Wikipedia]('https://en.wikipedia.org/wiki/Morse_code#Letters,_numbers,_punctuation,_prosigns_for_Morse_code_and_non-English_variants')

    """)

if __name__ == '__main__':
    write(_)
