import os
import base64
import streamlit as st

from pandas.io.clipboard import copy as copy_to_clipboard
from .. import utils


def encode_text(inp):

    print('Encode text called')
    orig, text = utils.encode_text(inp)
    text = ' '.join(text)
    return orig, text


def copy_code(text):

    print('Copy Called')
    copy_to_clipboard(text)


def play_audio(text):
 
    print('Play Called')
    f = utils.morse_to_wav(text)
    print(f)
    return f


def play_video(text):
    
    print('Play Called')
    f = utils.morse_to_vid(text)
    print(f)
    return f


def write(cache):

    cache = utils.get_static_store()
    cache['copy'] = None

    st.markdown('# Enter some text')
    st.markdown('## Enter text to convert to morse code!')
    st.markdown('&nbsp; &nbsp; &nbsp;')

    inp = st.text_input('Enter here...')

    if inp:

        orig, text = encode_text(inp)

        if text:

            orig = orig.replace('\n', ' ')

            st.markdown('&nbsp; &nbsp; &nbsp;')
            st.markdown('### Original text: **'+orig+'**', unsafe_allow_html=True)
            st.markdown('### Morse code :   **'+text+'**', unsafe_allow_html=True)

            st.markdown('&nbsp; &nbsp;')
            copy_button = st.button('Copy')

            if copy_button:
                copy_code(text)

            st.markdown('&nbsp;')
            audio_file = play_audio(text)
            audio_ = open(audio_file, 'rb')
            play_button = st.audio(audio_, format='audio/wav')
            audio_.close()
            os.remove(audio_file)

            video_file = play_video(text)

            file_ = open(video_file, 'rb')
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            mymidia_html = f'<video width="300" height="300" controls id="vid" class="stVideo"><source type="video/webm" src="data:video/webm;base64,{data_url}">Your browser does not support the video element.</video>'
            st.markdown('&nbsp;')
            video = st.markdown(mymidia_html, unsafe_allow_html=True)
            file_.close()
            os.remove(video_file)
        
        else:

            st.error('Could not convert to morse code. Please refer to guide for possible input characters.')
    
    return inp

if __name__=='__main__':
    write(_)