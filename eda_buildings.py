import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

st.title('EDA - buildings dataset')


df = pd.read_csv("buildings.csv")

st.sidebar.header('Apply Filters')
# Add a selectbox for size
bdg_size = st.sidebar.multiselect(
    'Select Building Size',      
    df['Size'].unique(),
    default = df['Size'].unique()
 )

df1 = df[df.Size.isin(bdg_size)]
#st.write('df1 ', df1.shape)

# Add a selectbox for ispublic
bdg_public = st.sidebar.multiselect(
    'Is it a Public buildings?',     
    df['IsPublic'].unique(),
    default = df['IsPublic'].unique()
)
df2 = df1[df1.IsPublic.isin(bdg_public)]
#st.write('df2 ', df2.shape)

# Add a selectbox for chiller type
bdg_chiller_type = st.sidebar.multiselect(
    'Select Chiller Type',     
    df['ChillerType'].unique(),
    default = df['ChillerType'].unique()
)
df3 = df2[df2.ChillerType.isin(bdg_chiller_type)]
st.write('After filtering ', df1.shape, df2.shape, df3.shape)


vars = ['GFA', 'AirconFA', 'Occupancy', 'ChillerAge', 'ChillerEff', 
 'ChillerAudit', 'LED', 'EUI', 'Age', 'TotalEnergy', 'NonAirconFA']

st.sidebar.header('Univariate Analysis - Histogram')
# Add a selectbox for 
var1 = st.sidebar.selectbox(
    'Select a variable1',     
    vars
)
fig, ax = plt.subplots()
ax.hist(df3[var1], bins=20)
st.pyplot(fig)


st.sidebar.header('Univariate Analysis - Boxplot')
# Add a selectbox for 
var2 = st.sidebar.selectbox(
    'Select a variable2',     
    vars
)
fig, ax = plt.subplots()
ax.boxplot(df3[var2])
st.pyplot(fig)

st.sidebar.header('Bivariate Analysis - Scatterplot')
# Add a selectbox for 
var3 = st.sidebar.selectbox(
    'Select a variable3',     
    vars
)

# Add a selectbox for 
var4 = st.sidebar.selectbox(
    'Select a variable4',     
    vars
)

#df_scatter = df3[[var3, var4]]
#st.plotly_chart(df_scatter)

fig, ax = plt.subplots()
ax.scatter(df3[var3], df3[var4])
st.pyplot(fig)


st.sidebar.header('Correlation Analysis')
st.dataframe(df3.corr())


st.write(df3.head(20))
st.dataframe(df3.head(15).style.highlight_max(axis=0))
st.table(df3.head(10))

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.scatter_chart(chart_data)

#st.dataframe(df_scatter.head(10))






# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

#st.line_chart(df1[['GFA', 'AirconFA']].head(N))

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x, bdg_size, type(bdg_size))


# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option


# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")



