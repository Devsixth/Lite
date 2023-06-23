import streamlit as st
import os
import telepot
import requests
from PIL import Image

url = "https://api.telegram.org/bot5378660401:AAG6VvrbQY4c5Ph3dtIlRdy7E4mmcew67O8/sendmessage"
chat_id_g = '-1001750224466'  # to the group
chat_id_c = '-1001542839898'  # to the channel
token = '5378660401:AAG6VvrbQY4c5Ph3dtIlRdy7E4mmcew67O8'


def to_group(cl):
    callg = {'chat_id': chat_id_g, 'text': cl}
    requests.post(url, data=callg).json()


def to_channel(cl):
    callc = {'chat_id': chat_id_c, 'text': cl}
    requests.post(url, data=callc).json()

def main():
    st.header("MESSAGE")
    msg = st.text_input("Enter the Text", )
    st.write(msg)
    if st.button("Send"):
        to_group(msg)
        to_channel(msg)
        st.write("msg sent to group & channel")


if __name__ == "__main__":
    main()









