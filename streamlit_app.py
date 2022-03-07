import streamlit as st
from datetime import date, time
import pandas as pd
import numpy as np
import time as tm

st.set_page_config(
    page_title = "HCI - Streamlit",
    layout = "wide",
    menu_items = {
        'Get Help' : 'https://docs.streamlit.io/',
        'Report a bug' : 'https://www.google.com/',
        'About' : '# Welcome to HCI, Developed by Miguel Sablan'
    }
)

st.title("Learning Streamlit")
st.header("HCI - Prof Gregory Murad Reis, PhD")

add_selectbox = st.sidebar.selectbox(
    "Select a Project",
    ["Homepage","Geological periods","United States Capitals","Monitoring Biscayne Bay","Crypto"]
)

if add_selectbox == 'Geological periods':
    # Dividing the screen into 3 columns
    col1, col2, col3 = st.columns(3)

    # Populating each column
    with col1:
        # creating a dataframe for the geological periods
        geological_periods = pd.DataFrame(
            {
                "Geological Period": ["Quaternary","Neogene", "Paleogene","Cretaceous","Jurassic","Triassic"],
                "Millions of Years": [2.588, 23.03, 66, 145.5, 201.3, 252.17]
            }
        )
        # Displaying the dataframe
        st.dataframe(geological_periods)
        st.caption("Geological periods in millions of years ago")
    with col2:
        st.image("media/sedona_usa.jpeg")
        st.caption("Sedona, Arizona, USA, by Edmundo Mendez Jr, 2020")
    with col3:
        st.video("media/volcano.mp4")
        st.caption("Volcano by Martin Sanchez")

elif add_selectbox == 'United States Capitals':
    col1, col2 = st.columns(2)

    with col1:
        # Reading the csv file for the USA capitals
        usa_capitals = pd.read_csv('csv/capitals_usa.csv')

        # Displaying the data as a dataframe
        st.dataframe(usa_capitals)
        st.caption('Table of the 50 states of the USA with their respective city capitals and their coordinates')

    with col2:
        st.map(usa_capitals)
        st.caption('Map marking the city capitals of all the states in the USA.')

elif add_selectbox == 'Monitoring Biscayne Bay':
    st.subheader('1 - Map - Water Quality Parameters')
    uploaded_file = st.file_uploader('Choose a CSV file (if none is provided, a default dataset will be shown!)')

elif add_selectbox == 'Crypto':
    st.write("To be constructed")
else:
    st.subheader("Personal Info")

    first_name = st.text_input("First Name?")
    last_name = st.text_input('Last Name?')
    major = st.selectbox('What is your major?',
                         ['', 'Computer Science', "Information Technology", "CyberSecurity", "Data Science"])
    campus = st.radio('Which campus are you at?',
                      ['MMC', "BBC", "EC"])
    date_started = st.date_input("Start Date at FIU")
    today = date.today().year

    if first_name and last_name and major and campus and date_started:
        st.write("Hi", first_name, "! you have been at FIU", campus, "for", str(today-date_started.year), "years studying", major, ".")

    campuses_map = st.checkbox("See all the FIU campuses on the map")
    if campuses_map:
        map_data = pd.DataFrame(
            np.array([
                    [25.759005, -80.373825],
                    [25.770459, -80.368130],
                    [25.910728, -80.138982],
                    [25.992332, -80.339832],
                    [25.763418, -80.190564],
                    [25.790110, -80.131561],
                    [24.950351, -80.452974],
                    [38.895549, -77.011910],
                    [25.772754, -80.134411],
                    [25.781113, -80.132460]]),
        columns=['lat','lon'])
        st.map(map_data)

    st.subheader("Streamlit Features")

    basic_plots = st.checkbox("Basic Plots")
    if basic_plots:
        chart_data = pd.DataFrame(
            np.random.rand(20,4),
        columns=["A","B","C","D"])
        st.line_chart(chart_data)

    sliders = st.checkbox("Sliders")
    if sliders:
        st.info("Integer Slider for Age")
        age = st.slider("How old are you?", 0,130,21)
        st.write("I'm",str(age),"years old.")

        st.info("Time slider for appointment")
        appointment = st.slider(
            "Schedule your appointment:",
            value = (time(11,30),time(12,45))
        )
        st.write("You're scheduled for:", appointment[0].strftime("%H:%M"), "to", appointment[1].strftime("%H:%M"))

        st.info("Float slider for a range")
        values = st.slider("Select a range of values",
                           0.0,100.0,(25.0,75.0))
        st.write("Values:", str(values))

    audio = st.checkbox("Audio")
    if audio:
        st.write("Waves and Birds")
        st.audio("https://bigsoundbank.com/UPLOAD/mp3/0267.mp3", format="media/mp3", start_time=0)

        st.write("Alla Turca by Wolfgang Amadeus Mozart Sonata No. 11")
        st.audio("media/Alla-Turca.mp3", format="media/mp3",start_time=0)
        st.caption("License & Usage: Creative Commons CC BY 3.0")

    boxes = st.checkbox("Message boxes")
    if boxes:
        st.success("This is a success box")
        st.warning("This is a warning box")
        st.error("This is an error box")
        st.info("This is an info box")

    balloons = st.checkbox("Surprise!")
    if balloons:
        st.balloons()

    progress_bar = st.checkbox("Progress Bar")
    if progress_bar:
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            tm.sleep(0.1)