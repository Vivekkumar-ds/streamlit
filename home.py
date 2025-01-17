import time
import streamlit as st
st.write("hello world")
st.title("This the title")
st.image("Colours infra.jpg")
st.header("this is header")
st.video("3195394-uhd_3840_2160_25fps.mp4")
st.markdown("this is markdown")
st.subheader("this is subheader")
st.caption("this is caption")
st.code("x=2021")
#st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.checkbox('yes')
st.button('click me')
st.radio('pick your gender', ['male', 'female'])
st.selectbox('pick a fruit', ['apple', 'banana', 'orange'])
st.multiselect('chose a planet', ['mars', 'neptune', 'earth'])
st.select_slider('pick a mark', ['bad', 'good', 'excelent'])
st.slider('pick a number', 0, 50)


st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')


st.balloons()  # Celebration balloons
st.progress(90)  # Progress bar
#with st.spinner('Wait for it...'):
   # time.sleep(20)  # Simulating a process delay
    

st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("this is sidebar title")
st.sidebar.markdown("this is side bar text")

with st.container():
    st.write("this is inside container")


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=10)
st.pyplot(fig)



import streamlit as st
import graphviz

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')

import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.76, -122.4], columns=['lat', 'lon']
)
st.map(df)