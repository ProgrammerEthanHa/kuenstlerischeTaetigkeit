import streamlit as st
import pandas as pd
import altair as alt

st.header("Freizeit-Beschäftigung 'Künstlerisch tätig sein'")
st.subheader("Anteil der Befragten, die in ihrer Freizeit musizieren/schreiben/dichten/malen, nach Lebensphase in Deutschland im Jahr 2021")

source = pd.DataFrame({
        'Anteil(%)': [37, 29, 22, 28, 15, 14],
        'Altersgruppe': ['Junge Erwachsene', 'Singles', 'Paare', 'Familien', 'Jungsenioren', 'Ruheständler']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Altersgruppe:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 3000 Befragte in Deutschland; August 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  BAT Stiftung für Zukunftsfragen")