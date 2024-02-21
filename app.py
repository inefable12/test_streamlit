import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

##############
st.sidebar.image("Captura de pantalla de 2024-02-13 17-38-24.png",
                 caption="Bienvenidx")



##############Pagina 1##############

def Home():
    st.markdown("# Home :books:")
    st.sidebar.markdown("# Home :books:")
    image = Image.open("Captura de pantalla de 2024-02-13 17-38-24.png")
    st.image(image, caption='Est')
    
    image = Image.open("membrana.png")
    st.image(image, caption='Sim')

#st.header(':green[Puquna]: Talleres STEAM :pill:' , divider='blue')
#st.subheader('Jesus Alvarado Huayhuaz')

##############Pagina 2##############
def page2():
    st.markdown("# Cursos")
    st.sidebar.markdown("# Cursos")
    
    image = Image.open("membrana.png")
    st.image(image, caption='Cursos_')
    
    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Talleres presenciales',icon=":stars:")
        st.write('''Capacítate en skills que potencian tu CV.
        Implementa herramientas computacionales, simulaciones, 
        inteligencia artificial, prototipado con impresión 3D, y mucho más.''')
    with total2:
        st.info('Talleres virtuales',icon=":stars:")
        st.write (pd.DataFrame({'Names': ['Exploración in silico',
                                          'Revisión de papers con ia', 
                                          'Simulaciones moleculares 2'], 
                                'Inicio': ["15 de enero", "24 de febrero", 
                                           "28 de marzo"]})
)

##############Pagina 3##############
def page3():
    st.markdown("# Productos STEAM")
    st.sidebar.markdown("# Productos STEAM")
        
    y = np.random.normal(0,1, size = 100)
    ###
    code = '''
            #include 
            int main() {
            // printf() displays the string inside quotation
            printf("Hello, World!");
            return 0;
            }'''
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
    
    
    #st.title('Cursos de especialización 2024 :books:' )
    
    #st.caption('Por favor _subscríbete_ a mi :red[canal]')





#y = np.random.normal(0,1, size = 100)

#fig, ax = plt.subplots()

#ax.hist(y, bins = 15)

#st.write(fig)

page_names_to_funcs = {
  "Home": Home,
  "Cursos": page2,
  "Productos STEAM": page3
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
