import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

st.header(':green[Puquna]: Talleres STEAM :pill:' , divider='blue')

st.subheader('Jesus Alvarado Huayhuaz')

st.title('Cursos de especialización 2024 :books:' )

st.caption('Por favor _subscríbete_ a mi :red[canal]')

st.write(
    '''
    Capacítate en skills que potencian tu CV. 
    Implementa herramientas computacionales, 
    simulaciones, inteligencia artificial,
    prototipado con impresión 3D, y mucho más.
    '''
)

st.write (pd.DataFrame({
    'Names': ['Exploración in silico',
    'Revisión de papers con ia',
    'Simulaciones moleculares 2'],
    'Inicio': ["15 de enero",
    "24 de febrero",
    "28 de marzo"]
})
)

y = np.random.normal(0,1, size = 100)

#fig, ax = plt.subplots()

#ax.hist(y, bins = 15)

#st.write(fig)

###
code = '''
        #include 
        int main() {
        // printf() displays the string inside quotation
        printf("Hello, World!");
        return 0;
        }

'''

st.code(code, language= 'c')


st.text('Impresión de ecuación')

st.latex(
    r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)

    '''
)

###
st.write("Modifica el barplot")

st.slider("Mueve el slider", 0, 100, (25, 75))

###
df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

##
st.button("Reset", type="primary")
if st.button('Hello'):
    st.write('Hello there')
else :
    st.write('Good bye')

##
st.header('COntenido en Youtube', divider='rainbow')

st.link_button("Visit channel", "https://www.youtube.com/channel/UCm6lcnfmNS2stsUYVvrFOzg")

##
agree = st.checkbox('I Agree')
if agree:
    st.write('Thanks!')


on = st.toggle('Activate')
if on:
    st.write('Feature activated now!')


title = st.text_input('Movie title', ' ')
st.write('The current movie title is', title)

##
st.header('Welcome to our color picker web app',divider='green' )

color = st.color_picker('Pick A Color', '#00f900')
st.write('color is:   ', color)
