# Pollution and Emissions: Analysing & Visualising The Efficacy of COP26 Through Data 
## _An outlook into our project, our journey and our dynamic Streamlit application extending our research & analysis to the whole world_
---
<style>
    .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
    }
</style>

### __Executive Summary__ 💼


In a fast-paced world, governed by digitalisation and technology, an absolutely unequivocal pressure has been placed on the environment. The planet’s surface temperature is up 1.90 ˚F since the pre-industrial period and each and every year, the topic of climate change dominates the news headlines. 

It is very much in this vein that last year, we saw the United Nations Climate Change Conference, dubbed COP26, take place in Glasgow. Even despite the many controversies associated with the conference, it brought together some of the world’s most powerful countries in the name of climate change. However, COP26 is not the first in the way of international conferences targeting the issue of climate change. In fact, the very first world climate conference (FWCC) took place in February 1973. Even 50 years later, the pervasive issue of climate change continues to dominate.

We know that climate change has very serious implications for both the future and the health of young people. The chart below shows the rise in the number of young people feeling concerned about climate change – in each of these nations, only an average of 4.7% of people feel not worried about the issue. Recently, with the likes of Greta Thunberg challenging world leaders to take immediate action to deal with this pervasive issue, young people like us feel empowered. It was this innate interest for uncovering exactly why we are seeing so many climate conferences that drove us to this project. We wanted to investigate what impacts these conferences having on climate change – do we see time lags take place, with countries ‘forgetting’ the lessons of the conference, are the impacts multilateral or are they contingent on the level of development?




<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/2.jpg" class="center"  />



We wanted to look at several conferences and understand how they differ in their efficacy, but unfortunately with our API restrictions, we decided to focus solely on COP26. 

To help us answer this question, we initially began by dividing cities into three global clusters 🌎:

1.	__A cluster with higher income cities__ _(London and Washington DC)_
2.	__A cluster with emerging cities__ _(Delhi and São Paulo)_
3.	__A cluster with lower income cities__ _(Gaborone and Port-Au-Prince)_

We wanted to investigate how COP26 affected the emissions of four key pollutants 💨:

1.	__Carbon Monoxide__: carbon monoxide occurs primarily from the emissions of fossil-fuel powered engines.
2.	__Oxygen Trioxide__: when inhaled, this pollutant can cause severe damage to the lungs.
3.	__Nitrous Dioxide__: occurs primarily from cars, trucks, and buses. It reacts to form Nitric acid – leading to the acidification of water bodies and causing biodiversity loss.
4.	__PM2.5 Particulates__: exposure to PM2.5 has been said to cause premature mortality.

To help us assess the impacts that COP26 had on emissions we used the OpenWeatherMap’s API to access data relating to each of our time periods – pre, during and post the conference. We defined these periods as:

1.  We accessed data __before__ the COP26 conference __(01/12/20 – 31/10/21)__
2.  We accessed data __during__ the COP26 conference __(01/11/21 – 30/11/21)__
3.	We accessed data __after__ the COP26 conference __(01/12/21 – 01/12/22)__

We wanted to see whether, with the help of graphs and summary statistics, we would be able to uncover if there were any trends that we would be able to discern. While we initially wanted to investigate exactly how these cities changed their emissions of these pollutants, we soon realised that, to get a complete picture, it was worth analysing each and every country individually for every possible pollutant. __This is the rationale behind our Dynamic Streamlit Application, providing a complete depiction of the changes in emissions.__

We investigated a number of trends - whether certain pollutants were more susceptible to change during and after the conference, whether time lags did indeed exist with respect to the pollutants and if the response of a country depended on its level of development. We collected data on 249 countries, with 757 JSON files. Each file contained an awful lot of data points, and after parsing the data points we can summarise as:

1.	The data __before__ the COP26 conference had __2,000,000 data points__ (this classification had the __longest duration__)
2.	The data __during__ the COP26 conference had __173,000 data points__
3.	The data __after__ the COP26 conference had __221,000 data points__

If time lags do exist, it can explain why so many conferences have taken place. However, it also suggests that systemic change needs to be made with respect to how the issue of climate change is being dealt with. If the level of development of a country does, indeed, affect the extent to which pollution can be curtailed, it provides evidence for Ha-Joon Chang’s argument that the richer nations are ’Kicking Away The Ladder,’ for the less developed countries. 🪜


---


### __Our Streamlit Dynamic Application: Analysing & Visualising _All_ Pollutants Across _All_ Worldwide Countries__ 💻



<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/1.jpg" class="center"  />

As mentioned, in order to truly grasp the patterns and, potentially, causal relationships within our data; we realised at the end of our journey that in order to truly tell the tale of the efficacy of COP26 across different demographies, we needed to convey our data across much larger geographical regions - __so we went with the whole world.__ 😁

However, this required us to go beyond the remit of the project as this markdown site (as required by the project) is purely static and simply doesn't allow for any dyanmic usage. Given that we wanted our data visualisation to be interactive, we had to resort to other methods of utilising our comprehensive GitHub repository and connecting this with an app framework (that preferably supported Python lanaguage and libraries) in order to establish this interactivity.

Streamlit was a fantastic app framework that enabled this, and allowed us to connect our repo and API to an interface that includes phenomenal tools of data visualisation, including a world heatmap, linegraphs and stacked barcharts for our 3 chosen periods (before, during and after COP26) for __every country__ and __every pollutant__ provided by our API.

We will reveal more on our journey in creating this app further down on this page, but to get a preliminary glimpse; please see below:

### Click on the hyperlink below to see our dynamic Streamlit application 👇
[Our Dynamic Streamlit Application](https://amandeepn-cop26-analysis-app-05i6n6.streamlit.app)

### Click on the hyperlink below to see an introductory video 👇
[A Video Introduction To Our Dynamic Streamlit Application](https://www.youtube.com)

---


### __Our Motivations: What Made Us So Curious?__ 🤔



As briefly aforementioned, our motivation for this project stemmed from our passion for the environment. We have seen, with our own eyes, how pervasive the issue of climate change is. We initially wanted to investigate multiple conferences (we identified the Kyoto Protocol as one of particular interest), but the API would not go that far back, and instead settled on COP26 (we could get data on emissions before, during and after the protocol). Data science has been a phenomenal tool in helping climate scientists critically understand the ambiguities and uncertainties inherent in climate data – we wanted to emanate this in our own project!

Through investigating the different factors that affected climate change, we wanted to identify any trends or patterns that could explain the last 50 years of inefficiency. As climate concerns continue to remain very pertinent, we were really interested in exploring this topic to see if there were any factors affecting pollution that we hadn’t previously considered. We are both Economists at heart, noting that pollution was a negative externality. By its very nature, pollution is something that affects all of us and it is very important that we critically analyse the policies that aim to reduce it! We wanted to go one step above and examine how the degree of response to climate change varies based on the level of economic development of the nation. Data science presents us with the opportunity to examine the uncertainty of climate models, visualising the issue at hand.

In fact, we were immediately presented with an almost external validation of our project, with the advent of COP27 where our very own Minouche Shafik spoke in November 2022!




<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/3.jpg" class="center"  />

---


### __Preliminary Targets__ 🎯


Our initial targets following our complete change of project centred around investigating the efficacy of the climate initiatives. We have seen, over the last few decades, countless environmental initiatives being introduced. We were very interested in learning exactly what effect these initiatives had on the pollution levels of different countries. 



<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/4.jpg" class="center"  />




Given our API restrictions (will be examined further), we decided to focus on COP26.

We are interested in answering the following questions to help us further examine the efficacy of climate initiatives (COP26) and, moreover, ask ourselves exactly what the implications of this are for the environment: 🌱

- _Why have so many different climate initiatives been introduced over time?_
- _Did COP26 in particular turn out to be successful?_
- _What did the initiative have the largest impact on?_
- _Do different countries respond differently to these initiatives?_
- _Do discrepancies in the response of emerging and developed nations exist?_
- _What impacts have these initiatives had on the Air Quality Index and other polluting gasses?_
- _What time lags are associated with these initiatives?_
- _What are the short, medium and long-term effects of COP26 on the environment?_


---

## Methodology



### __Our Dataset’s Chosen Locations__ 📍


Before we expanded our data to the whole world _(through our interactive application)_, we decided to investigate the effects of COP26 on the emissions of the six cities aforementioned _(London, Washington DC, Delhi, São Paulo, Gaborone and Port-Au-Prince)_. As also mentioned, we decided to put the cities into three clusters:


<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/6.jpg" class="center"  />


It is important to note that we initially wanted to explore the impact on Beijing, but inputting the longitude/latitude into the API return a NaN value (will be explored further), and we decided instead to investigate the effects of COP26 on the pollution in São Paulo instead - which is at a similar stage in its economic development.

The choice of our 6 cities was entirely orientated around the fact that we wanted to have a dimension of our findings that examined the extent of environmental response, and how this depended on the level of economic growth that was encountered by a country. Our 6 locations allowed us to gather good intel on a range of countries that were epitomes of their economic categories.


### Economic theory produces 5 fundamental reasons why the level of environmental response might vary by how wealthy a country is: 💸


1. __Financial resources:__ Wealthy countries typically have more financial resources to invest in environmental protection and sustainability initiatives. They can afford to implement more expensive and advanced technologies to reduce pollution and protect natural resources.

2. __Economic priorities:__ Developing countries may prioritise economic growth over environmental protection, as they may see environmental regulations as a hindrance to economic development. On the other hand, developed countries may have a stronger emphasis on environmental protection as their economy has already been established.

3. __Political will:__ Wealthy countries may have a stronger political will to address environmental issues, as they have the resources and stability to implement policies and regulations to protect the environment. Developing countries may have less political will to address environmental issues due to lack of resources and other pressing concerns.

4. __Public awareness:__ Developed countries generally have higher levels of education and more access to information, which can lead to greater public awareness and concern about environmental issues. This can lead to greater pressure on governments and businesses to take action to protect the environment.

5. __Technological capabilities:__ Wealthy countries typically have greater technological capabilities to address environmental issues, including the ability to monitor and assess the state of the environment, the ability to develop and implement new technologies to reduce pollution and protect natural resources, and the ability to adapt to the impacts of climate change.

We want to see how these fundamental tenets in the relationship between level of economic wealth and responsiveness to climate change can be visualised and scrutinised with data science. 

Our initial choice of these 6 cities enabled us to do exactly this. Furthermore (and perhaps more fundamentally) when it came to deciding which countries to use as part of our analysis we first identified the signatories of COP26. All of these countries had, to different extents,committed to the conference and made pledges. ✍️


<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/5.jpg" class="center"  />



---



### __Our Choice of Further Variables (Dates and Pollutants)__ 📅 💨



Dates (or, perhaps more accurately, our lack of them) were wholly based on our limited choice of data sets - we will examine this further in the next section. As for our choice of pollutants, we had quickly discerned that we required a range of different pollutants in order to avoid the impacts of any selection bias that could have arisen from selecting only one pollution metric. 

Descriptions for our chosen pollutants are as follows:

- The first polluting gas we looked at was __Carbon Monoxide.__ Carbon monoxide occurs primarily from emissions by fossil-fuel powered engines. We decided to look into Carbon Monoxide as one of our pollutants of interest as the API was able to return data on it. It seemed natural to focus on the evolution of this gas with the advent of the climate initiative

- We then decided to look at __Ozone/ Oxygen Trioxide.__ When inhaled, ozone causes severe damage to the lungs. Ozone absorbs radiation, consequently acting as a greenhouse gas. As such a big contributor to the greenhouse effect, we felt it logical to investigate its evolution.

- __NO2 or Nitrous Dioxide__ occurs primarily from cars, buses and trucks. It gets into the atmosphere, reacting to form Nitric acid (acid rain). This acid rain causes damage to buildings and causes the acidification of water bodies, contributing to biodiversity loss.

- We also examined the __fine particulates (PM2.5)__. These appear in the air, reducing the visibility. Exposure to PM2.5 has been said to cause premature mortality - so we chose to investigate this as our fourth metric of interest. 



---



### __Potential Datasets - Our Options__ 📊



We found out a lot of data was available online to address our objective. Below are the sources we found, with the
respective numbers of datasets that each source held:

1. __Open Weather Map’s API__
2. __WHO GHO OData API__
3. __European Environment Agency had 227 datasets available for use__
4. __Data.gov had 12 datasets available for use__
5. __Data.gov.uk had 7 datasets available for use__
6. __UKCOP26 had 4 datasets available for use__
7. __Local Government Associate had 5 datasets available for use__


Based on our options above, the following provided our general consensus:


- __OpenWeather Air Pollution API__ - this was a phenomenal API that had a wealth of historical data covering 20 years of air pollution information across 9 different metrics from all across the world, bar a few key examples like Beijing.

- OpenWeather’s main alternative that we were looking at: the __WHO GHO OData API__. This proved to be a weaker option as the Air Pollution API by OpenWeather had a much more comprehensive repository of historical data than the WHO’s OData API. Although the WHO’s OData API covered a far larger number of years stemming from 2010-2019, it had actually taken an annual mean of each year of that data. Meaning that this API only provided 9 rows of historical data. We were initially attracted to this as we thought it would be a good idea to perhaps look at a range of climate protocols: the kyoto protocol of 1997, the Paris Agreement of 2016; but ultimately we realised given the severe lack of data, this wouldn’t be feasible. We ended up focusing on COP26 of 2021 and made the most of the OpenWeather Historical API to make use of the very comprehensive data it provided from over the past 2 years. Secondly and more briefly, the WHO’s OData API only provided data on PM2.5, a type of particulate; we wanted to discuss a wider range of pollutant gases that, come statistical inference, would allow us to answer our question with greater conviction.

- __3 - 7__ covers a few other sources as well that contain many relevant datasets for use. However, whether due to __lack of scale__, or indeed __lack of applicability__ to the variables we were looking to analyse, we decided that the OpenWeather Air Pollution API proved to be the best dataset to answer our question and to truly examine the scale and efficacy of COP26, and be able to employ that geographical perspective as well.



---



### __Our Chosen Dataset__ 👌



Our chosen dataset: [The OpenWeather Air Pollution API](https://openweathermap.org/api)


The OpenWeather API does a fantastic job of giving us access to an insanely comprehensive dataset; monitoring and providing both present and historical air pollution data on any coordinates, _provided by latitude and longitude_, in the world.



<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/7.jpg" class="center"  />



We mentioned that there were indeed a few limitations from the point of view of the historical reach of the data. As mentioned we wanted to initially look at a range of global climate initiatives extending back some 30 years but were unable to do so because of precisely this issue. We determined that by virtue of the data extending back to November 2020 and continuing to the present day, examining 1 climate protocol, COP26, was the best way forward. This took place in November 2021, which found itself in the middle of our timeline and, thus, opened up the fantastic opportunity to analyse pollution metrics in uniform time windows before, during and after the climate conference.


<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/8.jpg" class="center"  />


Our API returned data on our __four variables of interest.__ As this covered all our chosen variables, __our choice of the OpenWeather Air Pollution API was unequivocal.__


---



### __Making Use of Code__ 👨‍💻



To make our code usable, we initially had to import in all of the libraries (requests, pandas, numpy, json and matplotlib.), these gave us the critical tools we needed to ensure that we were able to access all the tools needed in order to execute all required functions to our data.

We started by analysing OpenWeather’s Air Pollution API, seeing the total 9 variables and began to decipher which ones could be used to universally answer our question. For some obscure air pollutants like PM10, we had empty values for most countries so we had to withdraw the prospect of any use of these.

Eventually we settled on using the pollutants Nitrous Oxide, Carbon Monoxide, Ozone as well as PM2.5 particulates as our variables of interest. 

We created this flowchart that can be seen below, to illustrate the _scale, size and hierarchies_ involved with the information that we wanted to illustrate in our visual analysis:



<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/9.jpg" class="center"  />



Within our time frame _(approx. past 2 years)_, we found that each country had approximately __17,500 rows__ of data which across our __4 chosen variables__ postcleaning and 6 countries meant that we were processing calls and requests and dealing with approximately __945,000 individual data points__ - pretty big! 🤯 

When we break this down into our clusters of 2 countries each, separated by their level of economic development; low income countries, newly emerging economies and high income countries found themselves with paginated data that was approximately equal in size at around __315,000 data points.__

And then when splitting our 2 year time frame into 3 distinct and equal length periods of beforeCOP26, during-COP26 and after-COP26 we found ourselves with data points across our 4 chosen pollution metrics at about 105,000. Which surprisingly, at least compared to other groups, was a lot more manageable than it had initially seemed.

We utilised the drop function to allow us to drop unnecessary columns. This allowed us to drop the columns of the variables that we were not actually interested in (SO2, CH4). Using the concat function, we merged the 6 dataframes into one, main, dataframe. This made subsequent data operations a bit easier. We also utilised the .loc function to filter out the timerange that we needed (pre, during and post COP26).


---


### __Use of Pandas__ 🐼


We used the pd.Dataframe function to create the data frame itself. We then made use of several pandas functions such as concat (to merge the data frames together) and drop to remove unnecessary columns. We utilised df.rank to do dataframe operations. This enabled us to find which countries were the largest contributors to pollution before the inception of COP26 and how these rankings evolved with the advent of the initiative.


---


### __Missing data__ 🔍


We had to employ the use of the __DropNA function__ for this. 

<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/10.jpg" class="center"  />


This allowed us to remove all NaN values that, come data visualisation, would not be able to return anything meaningful and would have produced many annoying errors. You’ll see this _in practice_ in some of the correlation data we will employ for Gaborone’s 'during' and 'post' COP26 data.


---


### __Joining Several Databases__ 🧑‍🤝‍🧑 


We used .concat which concatenated the 6 different data frames into a singular dataframe. We then placed these multiple data frames into a singular list. 


<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/11.jpg" class="center"  />


The diagram above _illustrates_ this process.


---


<ins>Preliminary Visualisation (Time Series):</ins>
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/12.jpg" class="center"  />
Briefly explaining some of the code we employed in the experimentation we started off with;
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
emissions - due to the soft commitments made in the short term.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/13.jpg" class="center"  />
Ozone emissions, similar to PM2.5, seemed to have large variations across the board in the
build up to COP26. Once again, India seems to be a big contributor, with Sao paulo and
gaborone also remaining big emitters of oxygen
trioxide.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/14.jpg" class="center"  />
COP26 seems to have a far more significant reduction on Ozone emissions compared to PM2.5
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
decades.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/15.jpg" class="center"  />
<ins>Further Preliminary Visualisation (Time Series):</ins>
Further experimentation, as you can see over this slide and next, involved us plotting different
cities and air pollutants over the same distinct 3 time periods as before to examine the effects of
COP26 and seeing very clearly how these varied by the level of a country’s economic
development.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/16.jpg" class="center"  />
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/17.jpg" class="center"  />
Much of this was aroused by focusing on one city, one air pollutant and one time frame in a
single graph as opposed to a range of them which we had seen in our preliminary
experimentation. Obviously we can see that some graphs share a lot more than others, so what
we really wanted to do at this point was refine our data visualisation, potentially even move
beyond MatPlotLib, to ultimately share a graph that definitively tells us something about the role
of COP26 in responding to climate change.
<ins>More Refined Visualisation (Bar Charts):</ins>
Expanding on our preliminary investigations, we went further in data visualisation to create more
sophisticated data visualisation models that provided us clearer identification of what patterns
were at plaIn this first graph, we see pollutant levels before, during and after COP26 in Sao
Paulo:
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/18.jpg" class="center"  />
The first thing observable is that the Carbon Monoxide levels actually fell during the initiative.
However, after COP26, the levels started to increase again? Is this evidence of a time lag - with
countries resorting back to their initial behaviours once the initiative is no longer current?
We were very interested in seeing if this would be the case with other variables.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/19.jpg" class="center"  />
These next few graphs map out the pollution levels for the other cities that we analysed -we sce
that time lags exist for the other countries as well, but interestingly it seems to be for different
variables - primarily No2 emissions.
<ins>More Refined Visualisation (Pie Charts) [CO]:</ins>
We then tried to visualise these lags in a slightly different way - using pie charts.
1. Before COP26, Delhi and Sao Paulo were the biggest carbon monoxide emitters. There seems to be a big diversity in emissions.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/20.jpg" class="center"  />
2. During COP 26, Delhi increased their carbon monoxide emissions by 42% whilst Sao Paulo reduced their emissions by 96.5%. There are clearly huge differences in the response of different nations.

3. After COP26, Delhi found itself emitting similar carbon monoxide levels as pre-COP26. Sao Paulo increased emissions by 83%; the effects seem to wear off with time.
<ins>More Refined Visualisation (Pie Charts) [O3]:</ins>
1. Before the conference there seemed to be an asymmetry in the ozone pollutant levels, with most cities falling around the 20% region.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/21.jpg" class="center"  />
2. The ozone levels seemed not to change too much during the conference. London reduced its emissions by 33%.
3. The COP26 conference seemed not to play a big role when it came to ozone emissions - Washington went back to precisely its pre-COP26 levels.
<ins>More Refined Visualisation (Pie Charts) [PM2.5]:</ins>
1. Before COP26, Delhi had the highest PM2.5 emission levels.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/22.jpg" class="center"  />
2. Delhi increased its PM2.5 emission levels by 27% - seems intuitively strange.
3. Once again, after COP26, the PM2.5 levels seem unchanged compared to before the conference.
<ins>More Refined Visualisation (Pie Charts) [NO2]:</ins>
1. Before COP26, Sao Paulo had the highest nitrous dioxide emission levels.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/23.jpg" class="center"  />
2. Delhi increased its emissions by 50.3% whilst Sao Paulo managed to reduce their nitrous dioxide by 38.11%.
3. Delhi, Sao Paulo and London seemed to have returned to its pre-COP26 nitrous dioxide levels.
<ins>Preparing Data For Advanced Heatmap Analysis:</ins>
Step 1 - Cleaning the data:

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
in.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/24.jpg" class="center"  />
Step 2 - Cleaning the Data:
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/25.jpg" class="center"  />
Using our example of São Paulo, let’s walk you through each step behind the cleaning of the
data and then, moreover, how we employed this cleaning to pivot, melt and mutate our data:
1. We used the combine function to make the data frames into a single list and assigned it to the variable ‘combined,’ this allowed us to loop through the data frames; allowing us to execute the column dropping and concatenation as efficiently as possible.
2. For each value in the list of combined, we run a loop to change all unix code to datetime. Drop columns for main, components and dt.
3. Concatenating data frames, and merging them around axis 1 (the second axis) - admittedly, we needed to use our week 8 here.
4. We concatenate for each of the cities, merging the data frames together respectively (step 3-step 8)
5. Step 9 - made a new list containing the new data frames. Defined a new dataframe under the combined2 variable that brings together all the cleaned data frames into a single list.
6. Step 10 - dropping the columns for main, components and dt, this time for our new combined2 variable

As the outcome of this cleaning, which required a process of pivoting, melting and mutating our
data, can see when we visualise our same example of Sao Paulo, we have a much cleaner
dataframe.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/26.jpg" class="center"  />
The dates for our 17,500 rows for this location over the total time we are able to access are very
clear, as are the pollutants we have a particular interest in which find their associated values
going down on the left hand side.
<ins>Initial Heatmap</ins>
<ins>Exploration:</ins>
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/27.jpg" class="center"  />
What does this clean data mean in terms of hard core data visualisation?
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
of summary stats in order to really help us answer the question at hand.
<ins>Further Heatmap Exploration:</ins>
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/28.jpg" class="center"  />
These more refined heatmaps try to elucidate what the real target areas had been during the
cop26 initiative. The X axis includes the days of the week, whilst the Y axis involves the different
months. We see that, for all of the countries (excluding Gaborone - the missing data which, as
explored through NAN values) didn't return us with a heatmap; we will explore this in Statistical
inference. There seems to be the highest pollution in the middle of the year, which ceases
slightly towards the latter points of the year. It seems intuitive, that there are short term time lags
at least whilst the plans are being introduced.
<ins>Refining Our Heatmaps:</ins>
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/29.jpg" class="center"  />
After our attempts, we really bolstered down our efforts to create a much clearer and more
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
calendar days.
<ins>The Outcome Of Our Refinement:</ins>
Below presents our final and refined heatmaps. It is clear that, through these, we are able to tell
a story. This is particularly relevant as we begin to examine the specific measures that were
undertaken by each respective country:
1. Washington: Washington, D.C. had moderate levels of air pollution before COP26. During the conference, the US government announced new plans to reduce emissions from the transportation sector. As a result, heat maps show a small decrease in pollution levels in Washington, D.C. during and after COP26.
2. Sao Paulo: Sao Paulo had high levels of air pollution before COP26. However, during the conference, the Brazilian government announced new plans to reduce emissions from the transportation and industrial sectors. As a result, heat maps show a moderate decrease in pollution levels in Sao Paulo during and after COP26.
3. Gaborone: Gaborone had relatively low levels of air pollution before COP26. However, during the conference, the Botswana government did not announce any major plans to reduce emissions. Heat maps show little to no change in pollution levels in Gaborone during and after COP26.
4. London: London had relatively low levels of air pollution before COP26. During the conference, the UK government announced new targets for reducing emissions from the power sector. As a result, heat maps show a small decrease in pollution levels in London during and after COP26.
5. Delhi: Delhi had high levels of air pollution before COP26. However, during the conference, the Indian government did not implement as many strict regulations. Heat maps show only a slight decrease in pollution levels in Delhi during and after COP26. 6. Port-au-Prince: Port-au-Prince had moderate levels of air pollution before COP26. However, during the conference, the Haitian government did not announce any major plans to reduce emissions. Heat maps show little to no change in pollution levels in Portau-Prince during and after COP26.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/30.jpg" class="center"  />
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/31.jpg" class="center"  />
<ins>Statistical Inference:</ins>
We wished to analyse the correlation between each of the pollutants before, during and after the
COP26 initiative. We see here that there is a very strong relationship between carbon monoxide
and no2 in Sao Paulo, during the pandemic this actually weakened - to 0.73 before slightly
increasing to 0.78 - it seems that the COP26 initiative actually changed the correlations between
each of the variables.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/32.jpg" class="center"  />
We have used the Seaborn Python data visualisation library, based on matplotlib, to develop
correlation data as summary statistics. The role of this is to shed light on our limitation last week
concerning causation vs correlation. Investigating correlations between all gases before, during
and after COP26 across all of our locations will allow us to explore whether or not the initiative
has affected the interrelations between a country’s pollutants. Pre-COP26, we noticed that ozone
emissions were strongly correlated with the carbon monoxide emissions in Gaborone (a
correlation of 0.36 existed between the two), which actually fell to 0.11 during the conference. It
did, however, slightly increase to 0.4 after the conference; perhaps once again indicating the time
lag.
<img src="https://github.com/AmandeepN/COP26-Analysis/raw/main/images/33.jpg" class="center"  />
<ins>Our Verdict & Answer:</ins>
As we discussed, we found different countries responded differently to the conference:
We saw the countries demonstrated time lags when it came to their emissions; they generally
decreased their emissions suddenly during COP26 then increased them again after COP26; this
was most notable for Brazil as noted. We found clear evidence of time lags when it came to their
response and concluded this is why so many climate initiatives have been implemented over the
last 30 years.
Delhi, in particular, seemed not to fit this trend - they actually increased their emissions during the
pandemic. Clearly, different countries respond in different ways contingent on their levels of
development.

---

## Appendix
- [Reference 1](https://www.youtube.com)
- [Reference 2](https://www.youtube.com)
- [Reference 3](https://www.youtube.com)
- [Reference 4](https://www.youtube.com)