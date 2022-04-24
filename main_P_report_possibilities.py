from  main_functions import *

def page_report_possibilities():
    ############################### LOADING DATA
    data = np.arange(-1000, 1000, 1, dtype=int)
    df = pd.DataFrame(data, columns=['ArrangedBase'])
    df['Arranged'] = df['ArrangedBase']

    ################################################################################
    options = ['DASHBOARD 1', 'DASHBOARD 2']
    option = st.sidebar.selectbox('OPTIONS', (options), 0)
    st.header(option)

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')\

    def button_download_dataframe(df):
        csv = convert_df(df)
        st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='example_file.csv',
        mime='text/csv',
    )

    ################################# OPTION 1 - linear
    if option == options[0]:
        a_x = a_slider(min=-200, max=200, start=8, denominal=10000)
        b_x = b_slider(min=-100, max=100, start=0)
        n_x = n_slider(min=0, max=10, start=3)
        plot_data = df_function_polynomial(df, 'Arranged', a_x, b_x, n_x)
        plot_chart_of_data(plot_data)
        st.dataframe(df)
        button_download_dataframe(df)

    ################################# OPTION 1 -polynomial
    if option == options[1]:
        st.header('Incredible chart')
        a_x = a_slider(min = -100, max = 100, start = 10, denominal = 10)
        b_x = b_slider(min = -100, max = 100, start = 0)
        plot_data = df_function_linear(df, 'Arranged', a_x, b_x)
        plot_chart_of_data(plot_data)
        st.dataframe(df)
        button_download_dataframe(df)
