
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

def page2():
    st.markdown('# Pollution & Emission')
    st.markdown('<ins> Analysing and visualising the efficacy of international climate initiatives (COP26) through data </ins>', unsafe_allow_html=True)
    st.markdown('<br/><ins> Our Rationale: </ins>', unsafe_allow_html=True)
    st.markdown('''In a fast-paced world governed by the forces of data, as much as many of our problems are
manifest from the pressures that technology has put on us; it’s clear that technology also serves
to inspirit the very solution of some of the problems that our rapidly developing world has served
to create. <br/>
And, of course, there is no example where this is quite as true as climate change. <br/>
We all know that climate change has serious implications for the health & futures of young
people; but I think I speak for all of us when I say that when we young people look at ways we
can actively combat it, we find ourselves quite powerless. As such, we’ve seen a rise in a
phenomenon that is Climate Anxiety.<br/>
As the chart shows on the left, we have seen a rise in the number of young people across
different geographies expressing a fear of the future of the environment; and as two ecowarriors ourselves, we found ourselves particularly compelled to examine how our interests in
preserving the environment intersected with our interests in Data Science that we had developed over this term.''', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/1.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Upon further research, it became clear that the science, policy and communication practices
around DS will impact the solutions we utilise into the future with climate change. Data science
is a phenomenal tool in helping climate researchers really understand the uncertainties and
ambiguities inherent in climate data to ultimately identify interventions, strategies and solutions
to fulfill the needs of both humanity and the environment - assisting loads in cases where
decision makers are often faced with numerous and conflicting goals.''')    
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/2.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''These strategies empowered by data and data science were exactly the sort of thing we hear of
at the likes of COP27, where our very own Minouche Shafik spoke in November 2022. And is
where pledges determined by data like those shared at COP27, involving the likes of countries
promising to limit global warming to 1.5 degrees are predicated. Data science is what is used to
examine the uncertainty of climate models and ultimately help visualise the issue at hand. <br/><br/><br/>
It is in this vein that we have aimed to use Data Science to go one step beyond this and, in an
almost self reflective way, examine the efficacy of the very initiatives and pledges that Data
Science has helped to create and will do so by using an Air Pollution API. We will also go one
step beyond this and examine how the degree of response to climate change following a global
climate protocol like COP26 varies depending on the level of economic development of
countries as well.''', unsafe_allow_html=True)
    st.markdown('<ins> Preliminary Targets: </ins>', unsafe_allow_html=True)
    st.markdown('''Our initial targets following our complete change of project centred around investigating the
efficacy of the climate initiatives. We have seen, over the last few decades, countless
environmental initiatives being introduced. We were very interested in learning exactly what
effect these initiatives had on the pollution levels of different countries. Given our API
restrictions (will be examined further), we decided to focus on COP26.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/3.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''We are interested in answering the following questions to help us further examine the efficacy of
climate initiatives (COP26) and, moreover, ask ourselves exactly what this means for the
environment:''')
    st.markdown('''- Why have so many different climate initiatives been introduced over time?
- Did COP26 in particular turn out to be successful?
- What did the initiative have the largest impact on?
- Do different countries respond differently to these initiatives?
- Do discrepancies in the response of emerging and developed nations exist?
- What impacts have these initiatives had on the Air Quality Index and other polluting gasses?
- What time lags are associated with these initiatives?
- What are the short, medium and long-term effects of COP26 on the environment?''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/4.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('<ins>Our Dataset’s Chosen Locations:</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/5.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''We decided to investigate the effects of COP26 on the emissions of these six cities. We decided
to put the cities into three clusters:
Cluster containing High Income Cities: London and Washington DC

Cluster containing Newly Emerging Cities: Delhi and Gaborone

Cluster containing Low Income Cities: São Paulo and Delhi

It is important to note that we initially wanted to explore the impact on Beijing, but inputting the
longitude/latitude into the API kept generating an error, and we decided instead to investigate
the effects of COP26 on the pollution in São Paulo instead - which is in a similar

The choice of our 6 cities was entirely orientated around the fact that we wanted to have a
dimension of our findings that examined the extent of environmental response, and how this
depended on the level of economic growth that was encountered by a country. Our 6 locations
allowed us to gather good intel on a range of countries that were epitomes of their economic
categories.

Generally, economic theory produces 5 fundamental reasons why the level of environmental
response might vary by how wealthy a country is:

1. Financial resources: Wealthy countries typically have more financial resources to invest in environmental protection and sustainability initiatives. They can afford to implement more expensive and advanced technologies to reduce pollution and protect natural resources.

2. Economic priorities: Developing countries may prioritise economic growth over environmental protection, as they may see environmental regulations as a hindrance to economic development. On the other hand, developed countries may have a stronger emphasis on environmental protection as their economy has already been established.

3. Political will: Wealthy countries may have a stronger political will to address environmental issues, as they have the resources and stability to implement policies and regulations to protect the environment. Developing countries may have less political will to address environmental issues due to lack of resources and other pressing concerns.

4. Public awareness: Developed countries generally have higher levels of education and more access to information, which can lead to greater public awareness and concern about environmental issues. This can lead to greater pressure on governments and businesses to take action to protect the environment.

5. Technological capabilities: Wealthy countries typically have greater technological capabilities to address environmental issues, including the ability to monitor and assess the state of the environment, the ability to develop and implement new technologies to reduce pollution and protect natural resources, and the ability to adapt to the impacts of climate change.

We want to see how these fundamental tenets in the relationship between level of economic
wealth and responsiveness to climate change can be visualised and scrutinised with data
science. Our choice of these 6 cities enabled us to do exactly this. Furthermore (and perhaps
more fundamentally) when it came to deciding which countries to use as part of our analysis we
first identified the signatories of COP26. All of these countries had, to different extents,
committed to the conference and made pledges. ''')
    st.markdown('<ins>Our Choice of Further Variables (Dates and Pollutants): </ins>', unsafe_allow_html=True)
    st.markdown('''Dates (or, perhaps more accurately, our lack of them) were wholly based on our limited choice
of data sets - we will examine this further in the next section.
As for our choice of pollutants, we had quickly discerned that we required a range of different
pollutants in order to avoid the impacts of any selection bias that could have arisen from
selecting only one pollution metric.
Descriptions for our chosen pollutants are as follows:
- The first polluting gas we looked at was Carbon Monoxide. Carbon monoxide occurs primarily from emissions by fossil-fuel powered engines. We decided to look into Carbon Monoxide as one of our pollutants of interest as the API was able to return data on it. It seemed natural to focus on the evolution of this gas with the advent of the climate initiative
- We then decided to look at Ozone/ Oxygen Trioxide. When inhaled, ozone causes severe damage to the lungs. Ozone absorbs radiation, consequently acting as a greenhouse gas. As such a big contributor to the greenhouse effect, we felt it logical to investigate its evolution,
- NO2 or nitrous dioxide occurs primarily from cars, buses and trucks. It gets into the atmosphere, reacting to form Nitric acid (acid rain). This acid rain causes damage to buildings and causes the acidification of water bodies, contributing to biodiversity loss.
- We also examined the fine particulates (PM2.5) - these appear in the air, reducing the visibility. Exposure to PM2.5 has been said to cause premature mortality - so we chose to investigate this as our fourth metric of interest.''')
    st.markdown('<ins>Potential Datasets:</ins>', unsafe_allow_html=True)
    st.markdown('''We found out a lot of data was available online. Below are the sources we found, with the
respective numbers of datasets that each source held:
1. Open Weather Map’s API
2. WHO GHO OData API
3. European Environment Agency had 227 datasets available for use
4. Data.gov had 12 datasets available for use
5. Data.gov.uk had 7 datasets available for use
6. UKCOP26 had 4 datasets available for use
7. Local Government Associate had 5 datasets available for use''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/6.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''1. OpenWeather Air Pollution API - this was a phenomenal API that had a wealth of historical data covering 20 years of air pollution information across 9 different metrics from all across the world, bar a few key examples like Beijing.
2. OpenWeather’s Main alternative that we were looking at: the WHO GHO OData API. This proved to be a weaker option as the Air Pollution API by OpenWeather had a much more comprehensive repository of historical data than the WHO’s OData API. Although the WHO’s OData API covered a far larger number of years stemming from 2010-2019, it had actually taken an annual mean of each year of that data. Meaning that this API only provided 9 rows of historical data. We were initially attracted to this as we thought it would be a good idea to perhaps look at a range of climate protocols: the kyoto protocol of 1997, the Paris Agreement of 2016; but ultimately we realised given the severe lack of data, this wouldn’t be feasible. We ended up focusing on COP26 of 2021 and made the most of the OpenWeather Historical API to make use of the very comprehensive data it provided from over the past 2 years. Secondly and more briefly, the WHO’s OData API only provided data on PM2.5, a type of particulate; we wanted to discuss a wider range of pollutant gases that, come statistical inference, would allow us to answer our question with greater conviction.
3. 3 - 7 covers a few other sources as well that contain many relevant datasets for use. However, whether due to lack of scale, or indeed lack of applicability to the variables we were looking to analyse, we decided that the OpenWeather Air Pollution API proved to be the best dataset to answer our question and to truly examine the scale and efficacy of COP26, and be able to employ that geographical perspective as well.''')
    st.markdown('<ins>Our Chosen Datasets: </ins>', unsafe_allow_html=True)
    st.markdown('''Our chosen dataset: The OpenWeather Air Pollution API.
The OpenWeather API does a fantastic job of giving us access to an insanely comprehensive
dataset; monitoring and providing both present and historical air pollution data on any
coordinates, provided by latitude and longitude, in the world.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/7.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''We mentioned that there were indeed a few limitations from the point of view of the historical
reach of the data. As mentioned we wanted to initially look at a range of global climate initiatives
extending back some 30 years but were unable to do so because of precisely this issue. We
determined that by virtue of the data extending back to November 2020 and continuing to the
present day, examining 1 climate protocol, COP26, was the best way forward. This took place in
November 2021, which found itself in the middle of our timeline and, thus, opened up the
fantastic opportunity to analyse pollution metrics in uniform time windows before, during and
after the climate conference.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/8.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Our API returned data on our four variables of interest. As this covered all our chosen variables,
our choice of the OpenWeather Air Pollution API was unequivocal.
''')
    st.markdown('<ins>Making Use of Code:</ins>', unsafe_allow_html=True)
    st.markdown('''To make our code usable, we initially had to import in all of the libraries (requests, pandas,
numpy, json and matplotlib.), these gave us the critical tools we needed to ensure that we were
able to access all the tools needed in order to execute all required functions to our data.
We started by analysing OpenWeather’s Air Pollution API, seeing the total 9 variables and
began to decipher which ones could be used to universally answer our question. For some
obscure air pollutants like PM10, we had empty values for most countries so we had to withdraw
the prospect of any use of these.
Eventually we settled on using the pollutants Nitrous Oxide, Carbon Monoxide, Ozone as well
as PM2.5 particulates as our variables of interest. We created this flowchart that can be seen
below, to illustrate the scale, size and hierarchies involved with really finding ourselves with the
information that we wanted to illustrate in our visual analysis:''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/9.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''The OpenWeather API has an almost infinite amount of air pollution data that provides
information on a daily frequency over the past 2 years from all across the globe. We found that
each country had approximately 17,500 rows of data which across our 4 chosen variables postcleaning and 6 countries meant that we were processing calls and requests and dealing with
approximately 945,000 individual data points.

When we break this down into our clusters of 2 countries each, separated by their level of
economic development; low income countries, newly emerging economies and high income
countries found themselves with paginated data that was approximately equal in size at around
315,000 data points.

And then when splitting our 2 year time frame into 3 distinct and equal length periods of beforeCOP26, during-COP26 and after-COP26 we found ourselves with data points across our 4
chosen pollution metrics at about 105,000. Which surprisingly, at least compared to other
groups, was a lot more manageable than it had initially seemed.

We utilised the drop function to allow us to drop unnecessary columns. This allowed us to drop
the columns of the variables that we were not actually interested in (SO2, CH4).
Using the concat function, we merged the 6 dataframes into one, main, dataframe. This made
subsequent data operations a bit easier. We also utilised the .loc function to filter out the time
range that we needed (pre, during and post COP26).''')
    st.markdown('<ins>Use of Pandas:</ins>', unsafe_allow_html=True)
    st.markdown('''We used the pd.Dataframe function to create the data frame itself. We then made use of several
pandas functions such as concat (to merge the data frames together) and drop to remove
unnecessary columns. We utilised df.rank to do dataframe operations - finding which countries
were the largest contributors to pollution before the inception of COP26 and how these rankings
evolved with the advent of the initiative.''')
    st.markdown('<ins>Missing data:</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/10.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''We had to employ the use of the DropNA function for this. This allowed us to remove all NaN
values that, come data visualisation, would not be able to return anything meaningful and would
have produced many annoying errors. You’ll see this in practice in some of the correlation data
we will employ for Gaborone’s during and post COP26 data.
''')
    st.markdown('<ins>Joining Several Databases:</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/11.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''We used .concat which concatenated the 6 different data frames into a singular dataframe. We
then placed these multiple data frames into a singular list. The diagram towards the bottom on
the left illustrates this process.''')
    st.markdown('<ins>Preliminary Visualisation (Time Series):</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/12.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Briefly explaining some of the code we employed in the experimentation we started off with;
MatPlotLib provided the basis of our preliminary experimentation. This is something that we
have already dealt with through problem sets and on the few python courses we have done
ourselves. But, in essence we started off by plotting graphs of the same pollutant (on this page
you can see PM2.5) for our 6 different cities and timeframes; that being before, during and after
COP26.
Obviously plotting the designated start and end times for these periods on the x-axis and the
pollutant levels on the y-axis, we were able to access quite a comprehensive graph illustrating
air pollution levels over the course of a period for all cities and potentially a bit of a story
associated with this data.
The first graph demonstrates the PM2.5 levels before the advent of COP26. We can see huge
fluctuations in the level of PM2.5, especially with Delhi. Looking at the graph, it is very hard to
discern between the PM2.5 emissions of the HIC; they are covered by the other clusters, so we
decided to use a slightly different structure when we mapped out the PM2.5 emissions during
COP26 (second graph). We still see big fluctuations in Delhi’s levels of emissions, however
there is a visible and significant reduction in the emissions of São Paulo. This can be explained
by the firm commitment that Brazil made during the conference.
After the advent of COP26, Brazil’s emissions have reduced significantly compared to those
before the introduction of the initiative. Delhi seems to continue to have significant PM2.5
emissions - due to the soft commitments made in the short term.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/13.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Ozone emissions, similar to PM2.5, seemed to have large variations across the board in the
build up to COP26. Once again, India seems to be a big contributor, with Sao paulo and
gaborone also remaining big emitters of oxygen
trioxide.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/14.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''COP26 seems to have a far more significant reduction on Ozone emissions compared to PM2.5
- across the board, ozone emissions have dropped significantly for the different nations, with
significant drops for Port-Au-Prince and Gaborone - the conference ended up having significant
decreases in 03, and a comparatively larger impact than PM2.5
After COP26, the emissions have decreased across the board, but have increased slightly
compared to during COP26. This reflects almost a ‘wearing off’ of the effects of the conference,
with countries resorting back to their old ways as time goes on.
To highlight this aspect of firms resorting back to their old ways, we decided to graph the NO2
emissions during and after the conference - here too, it seems that as length of time since
cop26 increases, the effects it had start to wear off slightly - perhaps this is why so many
initiatives have been targeted over the last couple
decades.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/15.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('<ins>Further Preliminary Visualisation (Time Series):</ins>', unsafe_allow_html=True)
    st.markdown('''Further experimentation, as you can see over this slide and next, involved us plotting different
cities and air pollutants over the same distinct 3 time periods as before to examine the effects of
COP26 and seeing very clearly how these varied by the level of a country’s economic
development.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/16.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/17.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Much of this was aroused by focusing on one city, one air pollutant and one time frame in a
single graph as opposed to a range of them which we had seen in our preliminary
experimentation. Obviously we can see that some graphs share a lot more than others, so what
we really wanted to do at this point was refine our data visualisation, potentially even move
beyond MatPlotLib, to ultimately share a graph that definitively tells us something about the role
of COP26 in responding to climate change.''')

    st.markdown('<ins>More Refined Visualisation (Bar Charts):</ins>', unsafe_allow_html=True)
    st.markdown('''Expanding on our preliminary investigations, we went further in data visualisation to create more
sophisticated data visualisation models that provided us clearer identification of what patterns
were at plaIn this first graph, we see pollutant levels before, during and after COP26 in Sao
Paulo:''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/18.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''The first thing observable is that the Carbon Monoxide levels actually fell during the initiative.
However, after COP26, the levels started to increase again? Is this evidence of a time lag - with
countries resorting back to their initial behaviours once the initiative is no longer current?
We were very interested in seeing if this would be the case with other variables.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/19.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''These next few graphs map out the pollution levels for the other cities that we analysed -we sce
that time lags exist for the other countries as well, but interestingly it seems to be for different
variables - primarily No2 emissions.''')
    st.markdown('<ins>More Refined Visualisation (Pie Charts) [CO]:</ins>', unsafe_allow_html=True)
    st.markdown('''We then tried to visualise these lags in a slightly different way - using pie charts.''')
    st.markdown('''1. Before COP26, Delhi and Sao Paulo were the biggest carbon monoxide emitters. There seems to be a big diversity in emissions.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/20.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''2. During COP 26, Delhi increased their carbon monoxide emissions by 42% whilst Sao Paulo reduced their emissions by 96.5%. There are clearly huge differences in the response of different nations.

3. After COP26, Delhi found itself emitting similar carbon monoxide levels as pre-COP26. Sao Paulo increased emissions by 83%; the effects seem to wear off with time.''')

    st.markdown('<ins>More Refined Visualisation (Pie Charts) [O3]:</ins>', unsafe_allow_html=True)
    st.markdown('''1. Before the conference there seemed to be an asymmetry in the ozone pollutant levels, with most cities falling around the 20% region.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/21.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''2. The ozone levels seemed not to change too much during the conference. London reduced its emissions by 33%.
3. The COP26 conference seemed not to play a big role when it came to ozone emissions - Washington went back to precisely its pre-COP26 levels.''')    
    
    st.markdown('<ins>More Refined Visualisation (Pie Charts) [PM2.5]:</ins>', unsafe_allow_html=True)
    st.markdown('''1. Before COP26, Delhi had the highest PM2.5 emission levels.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/22.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''2. Delhi increased its PM2.5 emission levels by 27% - seems intuitively strange.
3. Once again, after COP26, the PM2.5 levels seem unchanged compared to before the conference.''')
    

    st.markdown('<ins>More Refined Visualisation (Pie Charts) [NO2]:</ins>', unsafe_allow_html=True)
    st.markdown('''1. Before COP26, Sao Paulo had the highest nitrous dioxide emission levels.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/23.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''2. Delhi increased its emissions by 50.3% whilst Sao Paulo managed to reduce their nitrous dioxide by 38.11%.
3. Delhi, Sao Paulo and London seemed to have returned to its pre-COP26 nitrous dioxide levels.''')


    st.markdown('<ins>Preparing Data For Advanced Heatmap Analysis:</ins>', unsafe_allow_html=True)
    st.markdown('''Step 1 - Cleaning the data:

Our first step of cleaning the data involved us firstly importing in all the libraries (requests,
pandas, numpy, json, matplotlib (to plot our data). We used Google Colab as we had to import
files (since it operates on the cloud). We then accessed all of this data through the API key we
received upon signing up to OpenWeather’s air pollution API. We then collected our data
using location - this involved using specific longitude and latitude information to access the data
we needed. The lon/lat functions specify the coordinates for each of the cities that we were
interested in. We added the start and end dates, to highlight pollution in the build-up, during and
post the introduction of the COP26 initiative. Using a Unix time converter, we converted the start
and end dates into the unix form. The API Documentation needed the unix code to process the
start dates. We then repeated this process for each of the other cities that we were interested
in.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/24.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Step 2 - Cleaning the Data:''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/25.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''Using our example of São Paulo, let’s walk you through each step behind the cleaning of the
data and then, moreover, how we employed this cleaning to pivot, melt and mutate our data:
1. We used the combine function to make the data frames into a single list and assigned it to the variable ‘combined,’ this allowed us to loop through the data frames; allowing us to execute the column dropping and concatenation as efficiently as possible.
2. For each value in the list of combined, we run a loop to change all unix code to datetime. Drop columns for main, components and dt.
3. Concatenating data frames, and merging them around axis 1 (the second axis) - admittedly, we needed to use our week 8 here.
4. We concatenate for each of the cities, merging the data frames together respectively (step 3-step 8)
5. Step 9 - made a new list containing the new data frames. Defined a new dataframe under the combined2 variable that brings together all the cleaned data frames into a single list.
6. Step 10 - dropping the columns for main, components and dt, this time for our new combined2 variable

As the outcome of this cleaning, which required a process of pivoting, melting and mutating our
data, can see when we visualise our same example of Sao Paulo, we have a much cleaner
dataframe.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/26.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''The dates for our 17,500 rows for this location over the total time we are able to access are very
clear, as are the pollutants we have a particular interest in which find their associated values
going down on the left hand side.''')

    st.markdown('<ins>Initial Heatmap</ins>', unsafe_allow_html=True)
    st.markdown('<ins>Exploration:</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/27.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''What does this clean data mean in terms of hard core data visualisation?
In week 8 of the course, we did a lot of work with MatPlotLib in order to produce some basic
continuous graphs of air pollutants across our 3 distinct time frames of pre, during and post
COP26 for all of our cities. But one of the biggest criticisms we had for ourselves was that we
wanted to be a little more creative, we wanted to be a little more advanced.

So we entered the wonderful world of heatmaps. Which, through a process of continuous
refinement as we will present over the next few slides, really ended up being a phenomenal way
to visualise, compare and contrast air pollution metrics across time periods.

The above here shows some of our initial efforts. We can see that our heatmaps are initially
quite obscure, and whilst showed an accurate reflection of variation in all of our pollution metrics
across all of our cities across the whole time period provided by the API, we were still unable to
get clear information out of this and moreover, information that could then provide the grounds
of summary stats in order to really help us answer the question at hand.''')

    st.markdown('<ins>Further Heatmap Exploration:</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/28.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''These more refined heatmaps try to elucidate what the real target areas had been during the
cop26 initiative. The X axis includes the days of the week, whilst the Y axis involves the different
months. We see that, for all of the countries (excluding Gaborone - the missing data which, as
explored through NAN values) didn't return us with a heatmap; we will explore this in Statistical
inference. There seems to be the highest pollution in the middle of the year, which ceases
slightly towards the latter points of the year. It seems intuitive, that there are short term time lags
at least whilst the plans are being introduced.''')

    st.markdown('<ins>Refining Our Heatmaps:</ins>', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/29.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''After our attempts, we really bolstered down our efforts to create a much clearer and more
representative heatmap.
After much persistence, we were able to do this; the following providing the steps:
In step number 1, we import the datetime module. This is the heart and essence of our ability to
break pollution data by time and date.

In step number 2, we rename our columns so that they make sense.

In step number 3, we proceed to concatenate all 6 of our locational data frames/

In step number 4 proceed to drop NaN values and you can see some of this in step number 5,
where when we visualise this dataframe, you can see a slew of 0s for the data concerning
gaborone, where we had a considerable problem with missing data.

In our final step, we then use calplot, which is a function that creates heatmaps from pandas
time series data. And enables us to structure our heatmaps such that they are colour coded by
calendar days.''')

    st.markdown('<ins>The Outcome Of Our Refinement:</ins>', unsafe_allow_html=True)
    st.markdown('''Below presents our final and refined heatmaps. It is clear that, through these, we are able to tell
a story. This is particularly relevant as we begin to examine the specific measures that were
undertaken by each respective country:
1. Washington: Washington, D.C. had moderate levels of air pollution before COP26. During the conference, the US government announced new plans to reduce emissions from the transportation sector. As a result, heat maps show a small decrease in pollution levels in Washington, D.C. during and after COP26.
2. Sao Paulo: Sao Paulo had high levels of air pollution before COP26. However, during the conference, the Brazilian government announced new plans to reduce emissions from the transportation and industrial sectors. As a result, heat maps show a moderate decrease in pollution levels in Sao Paulo during and after COP26.
3. Gaborone: Gaborone had relatively low levels of air pollution before COP26. However, during the conference, the Botswana government did not announce any major plans to reduce emissions. Heat maps show little to no change in pollution levels in Gaborone during and after COP26.
4. London: London had relatively low levels of air pollution before COP26. During the conference, the UK government announced new targets for reducing emissions from the power sector. As a result, heat maps show a small decrease in pollution levels in London during and after COP26.
5. Delhi: Delhi had high levels of air pollution before COP26. However, during the conference, the Indian government did not implement as many strict regulations. Heat maps show only a slight decrease in pollution levels in Delhi during and after COP26. 6. Port-au-Prince: Port-au-Prince had moderate levels of air pollution before COP26. However, during the conference, the Haitian government did not announce any major plans to reduce emissions. Heat maps show little to no change in pollution levels in Portau-Prince during and after COP26.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/30.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/31.jpg" class="center"  />', unsafe_allow_html=True)
       
    
    st.markdown('<ins>Statistical Inference:</ins>', unsafe_allow_html=True)
    st.markdown('''We wished to analyse the correlation between each of the pollutants before, during and after the
COP26 initiative. We see here that there is a very strong relationship between carbon monoxide
and no2 in Sao Paulo, during the pandemic this actually weakened - to 0.73 before slightly
increasing to 0.78 - it seems that the COP26 initiative actually changed the correlations between
each of the variables.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/32.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('''We have used the Seaborn Python data visualisation library, based on matplotlib, to develop
correlation data as summary statistics. The role of this is to shed light on our limitation last week
concerning causation vs correlation. Investigating correlations between all gases before, during
and after COP26 across all of our locations will allow us to explore whether or not the initiative
has affected the interrelations between a country’s pollutants. Pre-COP26, we noticed that ozone
emissions were strongly correlated with the carbon monoxide emissions in Gaborone (a
correlation of 0.36 existed between the two), which actually fell to 0.11 during the conference. It
did, however, slightly increase to 0.4 after the conference; perhaps once again indicating the time
lag.''')
    st.markdown('<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/33.jpg" class="center"  />', unsafe_allow_html=True)
    st.markdown('<ins>Our Verdict & Answer:</ins>', unsafe_allow_html=True)
    st.markdown('''As we discussed, we found different countries responded differently to the conference:
We saw the countries demonstrated time lags when it came to their emissions; they generally
decreased their emissions suddenly during COP26 then increased them again after COP26; this
was most notable for Brazil as noted. We found clear evidence of time lags when it came to their
response and concluded this is why so many climate initiatives have been implemented over the
last 30 years.
Delhi, in particular, seemed not to fit this trend - they actually increased their emissions during the
pandemic. Clearly, different countries respond in different ways contingent on their levels of
development.''')
    
page_names_to_funcs = {
    "Main Page": main_page,
    "Report PDF": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

