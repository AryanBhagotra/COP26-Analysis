
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
st.set_page_config(layout="wide")


@st.cache
def get_data():
    post_df = pd.read_csv('data/post.csv')
    during_df = pd.read_csv('data/during.csv')
    pre1_df = pd.read_csv('data/pre1.csv')
    pre2_df = pd.read_csv('data/pre2.csv')
    pre_df = pd.concat([pre1_df, pre2_df])
    return pre_df, during_df, post_df


pre_df, during_df, post_df = get_data()

@st.cache(ttl=24*60*60)
def get_data_time(time_frame='Post COP26 climate conference'):
    if time_frame == 'Post COP26 climate conference':
        return post_df.groupby('Country')['aqi'].mean().reset_index()
    elif time_frame == 'Pre COP26 climate conference':
        return pre_df.groupby('Country')['aqi'].mean().reset_index()
    else:
        return during_df.groupby('Country')['aqi'].mean().reset_index()

def plot_map(df):
    fig = px.choropleth(df, locations="Country", locationmode='country names',
                    color="aqi", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)


    fig.update_layout(coloraxis_colorbar=dict(
        title="Average Air Quality Index",
        tickvals=[1, 2, 3, 4, 5],
        ticktext=["Good", "Fair", "Moderate", "Poor", "Very Poor"],
        dtick=4
    ))

    st.plotly_chart(fig, use_container_width=True)




styl = """
<style>
.plot-container{
  box-shadow: 4px 4px 8px 4px rgba(0,0,0,0.2);
  transition: 0.3s;
  
}

</style>
"""
st.markdown(styl, unsafe_allow_html=True)


def main_page():
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
        (.1, 2.3, .1, 1.3, .1))
    with row0_1:
        st.title('COP26 Climate Conference Analysis')

    row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
    with row4_1:
        st.subheader('Average Air Quality Index')
    row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3 = st.columns(
        (.2, 2.3, .4, 4.4, .2))
    with row5_1:
        time_frame = st.selectbox("Please select time period", 
                ['Post COP26 climate conference', 'Pre COP26 climate conference',
                'During COP26 climate conference'], key='time_frame', index=0)
        df = get_data_time(time_frame)
        st.markdown('This chart shows the average air quality of all the countries based on the time period selected above.')

    with row5_2:
        plot_map(df)
        

main_page()
