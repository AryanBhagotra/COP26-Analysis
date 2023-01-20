
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
                    color="aqi", 
                    hover_name="Country", 
                    color_continuous_scale=px.colors.sequential.Plasma)


    fig.update_layout(coloraxis_colorbar=dict(
        title="Average Air Quality Index",
        tickvals=[1, 2, 3, 4, 5],
        ticktext=["Good", "Fair", "Moderate", "Poor", "Very Poor"],
        dtick=4
    ))

    st.plotly_chart(fig, use_container_width=True)


@st.cache(ttl=24*60*60)
def get_country_data(country):
    country_df_post = post_df[post_df['Country'] == country]
    country_df_pre = pre_df[pre_df['Country'] == country]
    country_df_during = during_df[during_df['Country'] == country]
    return country_df_post, country_df_pre, country_df_during

@st.cache(ttl=24*60*60)
def get_country_aqi_data(country):
    country_df_post = post_df[post_df['Country'] == country]
    country_df_pre = pre_df[pre_df['Country'] == country]
    country_df_during = during_df[during_df['Country'] == country]
    
    aqi_correspondance_dict = {1:"Good", 2:"Fair", 3:"Moderate", 4: "Poor", 5: "Very Poor"}
    post_aqi = country_df_post['aqi'].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0).\
                            rename(index=aqi_correspondance_dict)
    pre_aqi = country_df_pre['aqi'].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0).\
                            rename(index=aqi_correspondance_dict)
    during_aqi = country_df_during['aqi'].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0).\
                            rename(index=aqi_correspondance_dict)

    return post_aqi, pre_aqi, during_aqi



def plot_country_feature(feature, country_df_post, country_df_pre, country_df_during):
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Pre COP26 climate conference",
                     "During COP26 climate conference", "Post COP26 climate conference"))
    fig.add_trace(go.Scatter(x=country_df_pre.Date, y=country_df_pre[feature],
                            name='Pre',marker_color='blue'), row=1, col=1)
    fig.add_trace(go.Scatter(x=country_df_during.Date, y=country_df_during[feature],
                            name='During',marker_color='green'), row=1, col=2)
    fig.add_trace(go.Scatter(x=country_df_post.Date, y=country_df_post[feature],
                            name='Post',marker_color='red'), row=1, col=3)
    fig.update_layout(template='simple_white',height = 500, 
                    title=f'{feature}')


    min_y = min([country_df_pre[feature].min(), country_df_during[feature].min(), country_df_post[feature].min()])-0.5
    max_y = max([country_df_pre[feature].max(), country_df_during[feature].max(), country_df_post[feature].max()])+0.5

    fig.update_yaxes(range=[min_y, max_y], row=1, col=1)
    fig.update_yaxes(range=[min_y, max_y], row=1, col=2)
    fig.update_yaxes(range=[min_y, max_y], row=1, col=3)

    st.plotly_chart(fig, use_container_width=True)


def get_country_aqi_data_nomalized(country):
    country_df_post = post_df[post_df['Country'] == country]
    country_df_pre = pre_df[pre_df['Country'] == country]
    country_df_during = during_df[during_df['Country'] == country]
    
    aqi_correspondance_dict = {1:"Good", 2:"Fair", 3:"Moderate", 4: "Poor", 5: "Very Poor"}
    post_aqi = country_df_post['aqi'].value_counts(normalize=True).reindex([1, 2, 3, 4, 5], fill_value=0).\
                            rename(index=aqi_correspondance_dict)
    pre_aqi = country_df_pre['aqi'].value_counts(normalize=True).reindex([1, 2, 3, 4, 5], fill_value=0).\
                            rename(index=aqi_correspondance_dict)
    during_aqi = country_df_during['aqi'].value_counts(normalize=True).reindex([1, 2, 3, 4, 5], fill_value=0).\
                            rename(index=aqi_correspondance_dict)

    return post_aqi, pre_aqi, during_aqi

def plot_stacked_bar(post_aqi, pre_aqi, during_aqi):
    pre_aqi_df = pre_aqi.reset_index()
    during_aqi_df = during_aqi.reset_index()
    post_aqi_df = post_aqi.reset_index()
    pre_aqi_df['Data'] = 'Pre'
    during_aqi_df['Data'] = 'During'
    post_aqi_df['Data'] = 'Post'
    data = pd.concat([pre_aqi_df, during_aqi_df, post_aqi_df])
    data['aqi'] = data['aqi'] * 100
    color_discrete_map={
                "Very Poor": "red",
                "Good": "green",
                "Poor": "blue",
                "Moderate": "#636EFA",
                "Fair": "#00CC96"}
    fig = px.bar(data, x='Data', y='aqi', color='index',
             color_discrete_map=color_discrete_map, hover_data={'aqi': ':.2f'})
    fig.update_xaxes(title="Data")
    fig.update_yaxes(title="% of Quality")

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
        
    row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
    with row6_1:
        st.subheader('Feature Analysis by Country')
    row7_spacer1, row7_1, row7_spacer2, row7_2, row7_spacer3 = st.columns(
        (.2, 2.3, .4, 4.4, .2))
    with row7_1:
        feature = st.selectbox("Please select a feature", list(
            post_df.columns[1:-1]), key='feature', index=0)
        country = st.selectbox("Please select a country", list(
            post_df['Country'].unique()), key='country')
        st.markdown('This chart shows different features of the selected country.')
        st.markdown('**aqi=Air Quality Index**')
        st.markdown('- Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor')

    row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
    with row8_1:
        country_df_post, country_df_pre, country_df_during = get_country_data(country)
        plot_country_feature(feature, country_df_post, country_df_pre, country_df_during)

    row10_spacer1, row10_1, row10_spacer2 = st.columns((.2, 7.1, .2))
    with row10_1:
        st.subheader('Air Quality Index by Country')
    row11_spacer1, row11_1, row11_spacer2, row11_2, row11_spacer3 = st.columns(
        (.2, 2.3, .4, 4.4, .2))
    with row11_1:
        aqi_country = st.selectbox("Please select Country", list(
            post_df['Country'].unique()), key='aqi_country', index=0)
        st.markdown('This chart shows side by side comparison of Air Quality of the selected country during three periods.')

    with row11_2:
        post_aqi, pre_aqi, during_aqi = get_country_aqi_data_nomalized(aqi_country)
        plot_stacked_bar(post_aqi, pre_aqi, during_aqi)

main_page()