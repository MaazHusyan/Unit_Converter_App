import streamlit as st
from streamlit_option_menu import option_menu
import time

st.set_page_config(page_icon="📝", page_title="Unit Converter")

# Styling
css = """
<style>
    .title {
        text-align: center;
        background: linear-gradient(60deg, rgb(36 11 54), rgb(195 20 50), rgb(36 11 54));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
    }
    .elms {
        text-align: left;
        background: linear-gradient(60deg, rgb(195 20 50), rgb(36 11 54), rgb(36 11 54));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Select conversion type
conversion_type = option_menu(
    menu_title=None,
    options=["Weight","Length"],
    orientation="horizontal",
    icons=["arrow-90deg-down","arrow-90deg-down"],
    default_index=0,
    styles={
        "container": {"padding":"5px","background-color":"rgb(46 11 45)"},
        "icon":{"color":"white","font-size":"25px"},
        "nav-link":{"font-size":"25px",
               "text-align":"left",
               "margin":"2px",
                },
        "nav-link-selected":{"background-color":"rgb(195 20 50)"}
    }
)

if conversion_type == "Length":
    st.markdown('<h1 class="title">UNIT CONVERTER " LENGTH "</h1>', unsafe_allow_html=True)
    units = ('foot', 'yard', 'inch', 'metre', 'kilometre', 'centimetre', 'millimetre')
    conversion_factors = {
        ('inch', 'centimetre'): 2.54, ('centimetre', 'inch'): 1 / 2.54,
        ('millimetre', 'inch'): 1 / 25.4, ('inch', 'millimetre'): 25.4,
        ('inch', 'metre'): 1 / 39.3701, ('metre', 'inch'): 39.3701,
        ('foot', 'yard'): 1 / 3, ('yard', 'foot'): 3,
        ('yard', 'metre'): 1 / 1.09361, ('metre', 'yard'): 1.09361,
        ('yard', 'centimetre'): 91.44, ('centimetre', 'yard'): 1 / 91.44,
        ('foot', 'inch'): 12, ('inch', 'foot'): 1 / 12,
        ('centimetre', 'metre'): 1 / 100, ('metre', 'centimetre'): 100,
        ('millimetre', 'metre'): 1 / 1000, ('metre', 'millimetre'): 1000,
        ('kilometre', 'metre'): 1000, ('metre', 'kilometre'): 1 / 1000
    }
elif conversion_type == "Weight":
    st.markdown('<h1 class="title">UNIT CONVERTER " WEIGHT "</h1>', unsafe_allow_html=True)
    units = ('kilogram', 'gram', 'milligram', 'pound', 'ounce')
    conversion_factors = {
        ('kilogram', 'gram'): 1000, ('gram', 'kilogram'): 1 / 1000,
        ('kilogram', 'milligram'): 1000000, ('milligram', 'kilogram'): 1 / 1000000,
        ('gram', 'milligram'): 1000, ('milligram', 'gram'): 1 / 1000,
        ('kilogram', 'pound'): 2.20462, ('pound', 'kilogram'): 1 / 2.20462,
        ('pound', 'ounce'): 16, ('ounce', 'pound'): 1 / 16
    }

# User input
st.markdown('<h4 class="elms">INSERT</h4>', unsafe_allow_html=True)
user_slt = st.number_input(" ", placeholder="Enter", min_value=0)
opt_1 = st.selectbox(' ', units, index=None, placeholder="Select")
st.markdown('<h4 class="elms">TO</h4>', unsafe_allow_html=True)
opt_2 = st.selectbox('', units, index=None, placeholder="Select")

# Conversion calculation
result = ""
if opt_1 and opt_2 and opt_1 != opt_2:
    factor = conversion_factors.get((opt_1, opt_2))
    if factor:
        result = f"{user_slt * factor} {opt_2}"

if st.button("Calculate"):
    with st.spinner("Just a sec..."):
        time.sleep(1)
    if result:
        st.success(result)
    else:
        st.error("Invalid conversion selected!")
