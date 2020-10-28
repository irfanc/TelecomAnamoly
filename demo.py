
import streamlit as st
import os
port = int(os.environ.get(“PORT”, 5000))

if __name__ == "__main__":
    # execute only if run as a script
    st.title("""
     ** Predict Telecom Connection Status -  Attack or No-Attack ** !
    """)
    for i in range(10):
        print(" ** Predict Telecom Connection Status -  Attack or No-Attack ** !!!!   ".format(i))
