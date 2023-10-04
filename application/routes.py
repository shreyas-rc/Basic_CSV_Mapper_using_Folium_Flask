from application import app
from flask import render_template, url_for
import pandas as pd
import folium


@app.route("/")
def main():
    # Create a Folium map centered at a specific location
    df = pd.read_csv("D://Assignment_Garudalytics//application//static//OCO-2_2014_11_1.csv")

    m = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=10)

    # Add markers for each location with popups showing temperature values
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"Carbon dioxide values: {row['xco2']} PPM"
        ).add_to(m)

    # Add some markers or other elements to the map as needed
    #folium.Marker(location=[12.97160, 77.59456], popup='Bengaluru').add_to(m)

    # Convert the Folium map to HTML
    map_html = m._repr_html_()

    return render_template("layout.html", map_html=map_html, title="Home")

@app.route("/add_csv")
def index():
    return render_template("add_csv.html", title="Add_CSV")

