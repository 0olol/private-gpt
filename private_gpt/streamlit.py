import streamlit as st
# import subprocess

# Display Streamlit content
st.title("Streamlit App with Gradio Integration")

# Run the Gradio interface in a separate process
# aaa = subprocess.Popen(["gradio", "gradio_interface.py"])

# Replace the Gradio interface URL with your generated share link
gradio_interface_url = "http://127.0.0.1:8000/" # Example URL

# Load the Gradio interface using an iframe
st.write(f'<iframe src="{gradio_interface_url}" width="1000" height="1000"></iframe>',
         unsafe_allow_html=True)
