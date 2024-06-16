import streamlit as st

# Setting the page configuration
st.set_page_config(page_title="Mentor Space", layout="wide")

# Custom CSS to emulate your original design
st.markdown("""
<style>
    /* CSS reset */
    html, body, .reportview-container .main, .css-18e3th9 {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
        font-family: 'Arial', sans-serif;
    }
    /* Header styling */
    .header {
        background-color: #fff;
        padding: 20px 50px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .menu-item {
        display: inline-block;
        margin: 0 20px;
        font-weight: bold;
        color: #333;
    }
    .signup-btn {
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        text-transform: uppercase;
        border: none;
    }
    /* Main content styling */
    .mentor-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin: 40px auto;
        padding: 30px;
        background-color: #e0e0e0;
        border-radius: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        max-width: 80%;
    }
    .content {
        width: 50%;
    }
    .image-box {
        width: 500px;
        height: 500px;
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }
    .big-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 25px;
        cursor: pointer;
        border-radius: 5px;
        font-size: 16px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header with navigation links
st.markdown("""
<div class="header">
    <nav>
        <a href="#" class="menu-item">Mentor Space</a>
        <a href="#" class="menu-item">Solutions</a>
        <a href="#" class="menu-item">Pricing</a>
        <a href="#" class="menu-item">About</a>
        <button class="signup-btn">Sign up</button>
    </nav>
</div>
""", unsafe_allow_html=True)

# Main content section
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<div class='content'><h1>Mentor Stars</h1><p>Chers mentors, votre dévouement sur la plateforme HICKMA est inestimable. Pour reconnaître votre contribution, nous proposons une rémunération symbolique.</p><button class='big-btn'>Let's get your benefits</button></div>", unsafe_allow_html=True)

with col2:
    image_path = 'pexels-zhuhehuai-716276.jpg'
    col2.markdown(f"<div class='image-box' style='background-image: url({image_path}); background-size: cover;'></div>", unsafe_allow_html=True)
