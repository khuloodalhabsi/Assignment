# -*- coding: utf-8 -*-
"""Assigment_applid_khulod_rawa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yBWMbaO4NLtjqIe9Ayyv5h5sYxH5ux2r
"""

!pip install streamlit==1.14.0

# Commented out IPython magic to ensure Python compatibility.
# %%writefile Airplan.py
# import altair as alt
# import pandas as pd
# import streamlit as st 
# import matplotlib.pyplot as plt
# import plotly.express as px
# import graphviz
# page = st.sidebar.selectbox("Choose the page", ["Page 1", "Page 2", "Page 3", "Page 4"])
# 
# 
# Airpalne = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv')
# 
# 
# 
# Airpalne = Airpalne.dropna()
# a = Airpalne.head(30)
# 
# 
# if page == "Page 1":
#       st.title('Airplane Crashesand Fatalities Since 1908')
#       st.write("Introduction")
#       st.write("This dataset contains information about airplane crashes around the world. The data spans September 1908 to August 2008. A variety of entities broadcast data about the air crashes, including country, continent, operator, fatality, aircraft type and reason for the accident. This dataset currently contains 5268 records of air crashes.")
# 
#       st.markdown("""This app performs simple webscrapting of Airpalne crashes!
#       * **Python libraties:** base64, pandas, streamlit
#       * **Data source:**(https://www.kaggle.com/datasets/thedevastator/airplane-crashes-and-fatalities""")
# 
# 
#       st.write('khulood nasser alhabsi- 16j171143')
#       st.write('Rawa juma alsaifi -16s1551')
#       
# 
# 
# 
# 
# 
#       st.header('Dataframe of Airpalne crashes in 1908')
#       Airpalne =pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv')
#       Airpalne= Airpalne.fillna(0)
#       st.sidebar.header('User features')
# 
# 
# 
#       unique_Route	=['Demonstration','Test flight','New York - Paris','Paris - Prague','Moscow - Volograd','Goma - Walikale']
#       selected_Route	= st.sidebar.multiselect('Route',unique_Route,unique_Route)
#       df_selected_Route	 =Airpalne[(Airpalne['Route'].isin(selected_Route))]
# 
#       st.header('Display Route')
# 
#       st.write('Data Dimension: '+ str(df_selected_Route.shape[0]) + 'rows and '+ str(df_selected_Route.shape[1]) + ' columns.')
#       st.dataframe(df_selected_Route)
# 
# 
# 
#     
# 
# 
# 
# elif page == "Page 2":
#     
#     st.title('Airpalne Download Data')
#     
# 
#     st.markdown(""" <style> .font {
#           font-size:35px ; font-family: 'Cooper Black'; color: #FF7773;} 
#           </style> """, unsafe_allow_html=True)
#     st.markdown('<p class="font">showing Data</p>', unsafe_allow_html=True)
#       
#     df = pd.DataFrame(Airpalne)
#     @st.cache
#     def convert_df(df):
#           return df.to_csv().encode('utf-8')
# 
#     csv = convert_df(df)
# 
#     st.download_button(
#           label="Download data as CSV",
#           data=csv,
#           file_name='download.csv',
#           mime='text/csv',
#       )
#     st.dataframe(df)
# 
# 
# 
# elif page == "Page 3":
#  
#     st.title('Airpalne chart')
# 
# 
#     Airpalne1 = st.selectbox("Select your Airpalne",Airpalne['Type'].unique())
#     st.write(Airpalne1)
# 
# 
#     plot_type=st.radio("select the plot type",['scatter','line','area'])
#     if plot_type == 'scatter':
# 
#          pl = alt.Chart(Airpalne[Airpalne['Type'] == Airpalne1]).mark_circle().encode(
#               x='Fatalities',
#               y='Aboard',
# 
#               tooltip=['Fatalities', 'Aboard']
#           ).interactive()
# 
#    
# 
#          st.altair_chart(pl)
#     elif plot_type == 'line':
#         pl = alt.Chart(Airpalne[Airpalne['Type']==Airpalne1]).mark_line().encode(
#         x = 'Fatalities', y='Aboard',  tooltip = ['Fatalities','Aboard']
#         ).interactive()
#         st.altair_chart(pl)
# 
#     elif plot_type == 'area':
#         pl = alt.Chart(Airpalne[Airpalne['Type']==Airpalne1]).mark_area().encode(
#         x = 'Fatalities', y='Aboard',  tooltip = ['Fatalities','Aboard']
#         ).interactive()
#         st.altair_chart(pl)
#     
#       
# elif page == "Page 4":
#      st.title('chart')
#      Airpalne= Airpalne.fillna(0)
#      Bar_plot = st.checkbox("Bar chart")
#      Pie_plot = st.checkbox("Pie chart")
# 
#      if Bar_plot:
#        st.subheader('Bar chart')
#        Airpalne=Airpalne.head(20)
#        bar = alt.Chart(Airpalne).mark_bar().encode(x = 'Operator',y = 'mean(cn/In)',color = 'Aboard')
#        bar
# 
#      if Pie_plot:
#        st.subheader('Pie chart')
#        base = alt.Chart(Airpalne).encode(
# 
#        theta=alt.Theta("Type", stack=True),
# 
#        radius=alt.Radius("Location", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
# 
#      color="Operator",)
#      c1 = base.mark_arc(innerRadius=20, stroke="#fff")
# 
#      c2 = base.mark_text(radiusOffset=10).encode(text="values:Q")
# 
#      c1 + c2 
#       
# 
# elif page == "Page 5":
#   options = ['Graphviz Chart']
# 
#   selected_options = st.multiselect("Select your option:", options)
# 
#   for option in selected_options:   	
#        if option == 'Graphviz Chart':
#             
#             graph = graphviz.Digraph()
#             graph.edge('Location', 'Tienen, Belgium')
#             graph.edge('Tienen, Belgium', 'Military- German Navy	')
#             graph.edge('Military- German Navy', '(airship)')
#             graph.edge('Location', 'AtlantiCity, New Jersey')
#             graph.edge('AtlantiCity, New Jersey', 'Military - U.S. Navy')
#             graph.edge('Military - U.S. Navy', 'Dirigible')
# 
# 
#             st.graphviz_chart(graph)  
# 
# 
#    
#

!streamlit run Airplan.py &>/dev/null&
!npx localtunnel --port 8501