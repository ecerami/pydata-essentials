# A Hello, World Bokeh Application, illustrated with the Iris Data Set

import pandas as pd
from bokeh.layouts import row, widgetbox
from bokeh.models import Select
from bokeh.charts import Histogram
from bokeh.plotting import curdoc

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data", 
    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()

# Create the main plot
def create_figure():
    current_feature_name = feature_name.value
    p = Histogram(iris_df, current_feature_name, title=current_feature_name, color='Species', 
        legend='top_right', width=600, height=400)

    # Set the x axis label
    p.xaxis.axis_label = current_feature_name

    # Set the y axis label
    p.yaxis.axis_label = 'Count'
    return p

# Update the plot
def update(attr, old, new):
    layout.children[1] = create_figure()

# Controls
feature_name = Select(title="Iris Feature:", options=feature_names, value=feature_names[0])
feature_name.on_change('value', update)
controls = widgetbox([feature_name], width=200)
layout = row(controls, create_figure())

curdoc().add_root(layout)
curdoc().title = "Iris Data Set"

# To run this app:  bokeh serve bokeh_iris_app.py