import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import webbrowser
import math

def function_linear(x, a_x, b_x):
    a = a_x
    b = b_x
    y = a*x+b
    return y
def df_function_linear(x_dataFrame, columnname, a_x, b_x):
    df_temp = x_dataFrame
    df_temp['functionResult'] = function_linear(df_temp[columnname], a_x, b_x)
    return df_temp

#'''''''''''''''''''''''''''POLYNOMIAL
def function_polynomial(x, a, b, n):
    y = a*(x**n)+b
    return y
def df_function_polynomial(x_dataFrame, columnname, a, b, n):
    df_temp = x_dataFrame
    df_temp['functionResult'] = function_polynomial(df_temp[columnname], a, b, n)
    return df_temp

#'''''''''''''''''''''''''''SINUSOID

def df_function_sinusoid(x_dataFrame, columnname, a, type_, b_sigm):
    df_temp = x_dataFrame
    df_temp[columnname] = df_temp[columnname]/10
    sigm_tans = 1/b_sigm
    #type_ = str(type_)
    if type_ == 'sinus':
        df_temp['functionResult'] =  a * np.sin(sigm_tans*df_temp[columnname])
    if type_ == 'cosinus':
        df_temp['functionResult'] =  a * np.cos(sigm_tans*df_temp[columnname])
    if type_ == 'tangent':
        df_temp['functionResult'] =  a * np.tanh(sigm_tans*df_temp[columnname])

    return df_temp

def a_slider(min, max, start, denominal):
    a_x = st.sidebar.slider('a - direction of the x in 1/%s'%denominal, min, max, start)
    a_x = a_x / denominal
    return a_x

def b_slider(min, max, start):
    b_x = (st.sidebar.slider('b - independent element', min, max, start))
    return b_x

def n_slider(min, max, start):
    n_x = (st.sidebar.slider('n - to which power', min, max, start))
    return n_x

def b_sigm_slider(min, max, start, denominal):
    a_x = st.sidebar.slider('b_sigm - spread of sin in 1/%s'%denominal, min, max, start)
    b_sigm_x = a_x / denominal
    return b_sigm_x

def plot_chart_of_data(plot_data):
    fig = px.line(plot_data, x='Arranged', y='functionResult'
                  , range_x=[-100, 100], range_y=[-100, 100]
                  )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(line_color='rgb(255, 128, 0)', line_width=10)
    fig.update_layout(width=1000, height=550)
    st.write(fig)
