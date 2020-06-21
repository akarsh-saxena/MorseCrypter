import os
import base64

import numpy as np
from PIL import Image
import streamlit as st
from pandas.io.clipboard import copy as copy_to_clipboard
from .. import utils

@st.cache(allow_output_mutation=True)
def encode_image(image):

    print('Encode image called')
    orig, text = utils.encode_image(image)
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

FILE_TYPES = ["png", "jpg"]

def write(cache):

    cache = utils.get_static_store()
    fl = st.empty()

    if cache['copy'] is None:
        rand = np.random.randint(0, high=9999, size=1)[0]
        cache['copy'] = True
        cache['key'] = rand
    else:
        rand = None

    st.markdown('# Upload Image')
    st.markdown('## Upload an image to extract text and convert to morse code!')
    st.markdown('&nbsp; &nbsp;')

    f = st.file_uploader('', type=FILE_TYPES, key=cache['key'])
        
    if f is not None:
        
        cache['copy'] = True
    
        image = Image.open(f)
        
        if image.width<400:
            use_col_width = False
        else:
            use_col_width = True
        st.markdown('&nbsp; &nbsp; &nbsp;')
        im = st.image(image, use_column_width=use_col_width, channels='BGR')
        orig, text = encode_image(image)

        if text:

            orig = orig.replace('\n', ' ')

            st.markdown('### Original text: **'+orig+'**', unsafe_allow_html=True)
            st.markdown('### Morse code :   **'+text+'**', unsafe_allow_html=True)
            st.markdown('&nbsp; &nbsp;')

            # copy = st.button('Copy')

            # if copy:
            #     cache['copy'] = copy
            #     copy_code(text)
            
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

            st.error('Could not extract text')

    return f

if __name__=='__main__':
    write(_)