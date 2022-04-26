from main_functions import *
from main_css_html import *
from main_P_about_me import *
from main_P_function_examples import *
from main_P_report_possibilities import *

st.set_page_config(layout="wide")

################################ HTML ADJUSTMENT
m = css_html()

################################ CREATING DASHBOARDS
dashboards = ['ABOUT ME', 'FUNCTION EXAMPLES', 'REPORTING POSSIBILITIES']
dashboard = st.sidebar.selectbox('', (dashboards), 1) #, 'STOCK ANALYSIS', 'VISUALISATION EXAMPLES'

if dashboard == dashboards[0]:
    page_about_me()

if dashboard == dashboards[1]:
    page_function_examples()

if dashboard == dashboards[2]:
    page_report_possibilities()


