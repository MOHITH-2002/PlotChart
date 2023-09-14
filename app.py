import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px

st.image("logo.png", width=100)
st.header("PlotChart:rainbow[.]")

file = st.file_uploader("pick a csv or Excel file", type=['csv','XLSX'])

if file is not None:
    st.success("File uploaded successfully",icon='😅')
    
    
    
    df=pd.read_csv(file)
    dfFilter = df.columns

    
    fullView = st.checkbox(':blue[click me to view full data set]')
    if fullView:
        st.dataframe(df)
    else:
        st.dataframe(df.head())

    genre = st.radio(
    "Select type of chart/plots",
    [":rainbow[Plots]", ":rainbow[Pie chart]"])  
    st.header(genre)
    if genre == ':rainbow[Plots]':
        

        selected =  st.multiselect(':red[choose a v/s plots]', dfFilter,max_selections=3)
        plots = ['Pyplot','Barchart','Areachart','Linechart','plotly_chart']
        plots1 =['Pyplot','Barchart','Areachart','Linechart','plotly_chart','vega_lite_chart','altair_chart','bokeh_chart']
        #           0          1            2        3             4             5                 6            7
        
        if len(selected)>0:
            val=[selected]
            
            selectplt = st.multiselect(':red[choose a type of plots / charts]',plots1)
            pltval = [selectplt]
            # st.write(pltval)
            for i in range(len(selectplt)):
                if selectplt[i] == plots1[0]:
                   for j in range(0,2):
                        fig, ax = plt.subplots()
                  
                        plt.xlabel(selected[j])
                        
                        ax.hist(df[selected[j]],bins=20)
                        st.pyplot(fig)
                elif selectplt[i] ==plots1[1]:
                    st.bar_chart(df[selected])
                elif selectplt[i] ==plots1[2]:
                    st.area_chart(df[selected])
                elif selectplt[i] ==plots1[3]:
                    st.line_chart(df[selected])
                elif selectplt[i] ==plots1[4]:
                    
                    hist_data1=[]
                    group_labels=[] 

                    for i in range(0,len(selected)):
                        hist_data1.append(np.array(df[selected[i]]).flatten())
                    
                        group_labels.append(selected[i])
                        if len(hist_data1)>2:
                        
                    # Create distplot with custom bin_size
                            fig = ff.create_distplot(
                            hist_data1, group_labels)

                    # Plot!
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            fig = ff.create_distplot(
                            hist_data1, group_labels)

                    # Plot!
                            st.plotly_chart(fig, use_container_width=True)
                
                
                elif selectplt[i] == plots1[5]:
                    if len(selected)>2:
                        st.vega_lite_chart(df, {
                            'mark': {'type': 'circle', 'tooltip': True},
                            'encoding': {
                                'x': {'field': selected[0], 'type': 'quantitative'},
                                'y': {'field': selected[1], 'type': 'quantitative'},
                           
                            },
                        })
                        st.vega_lite_chart(df, {
                            'mark': {'type': 'circle', 'tooltip': True},
                            'encoding': {
                                'x': {'field': selected[1], 'type': 'quantitative'},
                                'y': {'field': selected[2], 'type': 'quantitative'},
                           
                            },
                        })
                        st.vega_lite_chart(df, {
                            'mark': {'type': 'circle', 'tooltip': True},
                            'encoding': {
                                'x': {'field': selected[2], 'type': 'quantitative'},
                                'y': {'field': selected[0], 'type': 'quantitative'},
                           
                            },
                        })
                        
                    else:
                            st.vega_lite_chart(df, {
                                'mark': {'type': 'circle', 'tooltip': True},
                                'encoding': {
                                    'x': {'field': selected[0], 'type': 'quantitative'},
                                    'y': {'field': selected[1], 'type': 'quantitative'},
                            
                                },
                            })
                    
                elif selectplt[i] == plots1[6]:
                    if len(selected)>2:
                        c = alt.Chart(df).mark_circle().encode(
                        x=selected[0], y=selected[1])

                        st.altair_chart(c, use_container_width=True)
                        
                        c = alt.Chart(df).mark_circle().encode(
                        x=selected[0], y=selected[2])

                        st.altair_chart(c, use_container_width=True)
                        c = alt.Chart(df).mark_circle().encode(
                        x=selected[1], y=selected[2])

                        st.altair_chart(c, use_container_width=True)
                    else:
                        c = alt.Chart(df).mark_circle().encode(
                        x=selected[0], y=selected[1])

                        st.altair_chart(c, use_container_width=True)
                        
                        
                elif selectplt[i] == plots1[7]:
                    p = figure(
                                        title=':rainbow[bokeh chart]',
                                        x_axis_label=selected[0],
                                        y_axis_label=selected[1])

                    p.line(df[selected[0]], df[selected[1]],legend_label='Trend', line_width=2)

                    st.bokeh_chart(p, use_container_width=True)
        else:
        
            plotSelected = st.multiselect(':red[choose a type of plots or charts]',plots)
            if len(plotSelected)>0:
                for i in range(0,len(plotSelected)):
                    if plotSelected[i] == plots[0]:
                        fig, ax = plt.subplots()
                        ax.hist(df)
                        st.pyplot(fig)
                    
                    elif plotSelected[i] == plots[1]:
                        st.bar_chart(df)
                    elif plotSelected[i] == plots[2]:
                        st.area_chart(df)
                    elif plotSelected[i] == plots[3]:
                        st.line_chart(df)
                    
                    elif plotSelected[i] == plots[4]:
                        hist_data1=[]
                        group_labels=[] 
                        select =  st.multiselect(':red[choose at least 3 category]', dfFilter)
                        for i in range(0,len(select)):
                            hist_data1.append(np.array(df[select[i]]).flatten())
                        
                        # hist_data = df1['#posts'],df1['private'],df1['#followers']
                            
                        
                        # # group_labels = dfFilter
                            
                            group_labels.append(select[i])
                            if len(hist_data1)>2:
                            
                        # Create distplot with custom bin_size
                                fig = ff.create_distplot(
                                hist_data1, group_labels)

                        # Plot!
                                st.plotly_chart(fig, use_container_width=True)
                
                
            else:
                        fig, ax = plt.subplots()
                        ax.hist(df)
                        st.pyplot(fig)
    
    # pi chart
    elif genre ==':rainbow[Pie chart]':
        
        number = st.slider(":blue[Select a range.] ", 0, len(df))
        if number > 10:
            labels = dfFilter
            sizes = np.array(np.sum(df.head(number))).flatten()
            fig = px.pie(df.head(number),values=sizes,names=labels)
            st.plotly_chart(fig)
        else:
            labels = dfFilter
            sizes = np.array(np.sum(df)).flatten()
            fig = px.pie(df,values=sizes,names=labels)
            st.plotly_chart(fig)