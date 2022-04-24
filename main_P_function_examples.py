from  main_functions import *

def page_function_examples():
    ############################### LOADING DATA
    data = np.arange(-1000, 1000, 1, dtype=int)
    df = pd.DataFrame(data, columns=['ArrangedBase'])
    df['Arranged'] = df['ArrangedBase']

    ################################################################################
    options = ['linear functions', 'polynomial functions',  'sinusoidal functions']
    option = st.sidebar.selectbox('OPTIONS', (options), 2)
    st.header(option)

    ################################# OPTION 1 - linear
    if option == options[0]:
        a_x = a_slider(min = -100, max = 100, start = 10, denominal = 10)
        b_x = b_slider(min = -100, max = 100, start = 0)
        plot_data = df_function_linear(df, 'Arranged', a_x, b_x)
        plot_chart_of_data(plot_data)

    ################################# OPTION 1 -polynomial
    if option == options[1]:
        a_x = a_slider(min = -200, max = 200, start = 8, denominal = 10000)
        b_x = b_slider(min = -100, max = 100, start = 0)
        n_x = n_slider(min = 0, max = 10, start = 3)
        plot_data = df_function_polynomial(df, 'Arranged', a_x, b_x, n_x)
        plot_chart_of_data(plot_data)


    if option == options[2]:
        types = ['sinus', 'cosinus',  'tangent']
        type_ = st.sidebar.selectbox('FUNCTION TYPE', (types), 0)
        a_x = a_slider(min=-1000, max=1000, start=100, denominal=100)
        b_sigm_x = b_sigm_slider(min=-1000, max=1000, start=200, denominal=100)
        plot_data = df_function_sinusoid(df, 'Arranged', a_x, type_, b_sigm_x)
        #plot_chart_of_data(plot_data)
        fig = px.line(plot_data, x='Arranged', y='functionResult'
                      , range_x=[-30, 30], range_y=[-3, 3]
                      )
        fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
        fig.update_traces(line_color='rgb(255, 128, 0)', line_width=10)
        fig.update_layout(width=1000, height=550)
        st.write(fig)