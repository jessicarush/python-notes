'''Bokeh - Python Interactive Data Visualization Library'''

# Bokeh is a Python interactive visualization library that targets modern web
# browsers for presentation. Its goal is to provide elegant, concise
# construction of graphics in the style of D3.js, and to extend this capability
# with high-performance interactivity over very large or streaming datasets.
# Bokeh is good for creating interactive plots, dashboards & data applications.

# pip3 install bokeh

# https://bokeh.pydata.org/en/latest/
# https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html

# Bokeh has 2 different interfaces for generating models.
#  – bokeh.models: used by application developers, it's a low-level interface
#  – bokeh.plotting: a medium-level interface with room for customizing


# bk.plotting
# -----------------------------------------------------------------------------

from bokeh.plotting import figure, output_file, show


c = ['red', 'olive', 'darkred', 'goldenrod', 'skyblue', 'orange', 'salmon']

# create a figure object
p = figure(plot_width=600, plot_height=400, title='Practice Plot')

# figure attributes can also be added like this:
p.title.text_color = c[6]
p.title.text_font = 'Helvetica'
p.title.text_font_size = '16pt'
p.title.text_font_style = 'normal'
p.yaxis.minor_tick_line_color = c[4]
p.xaxis.minor_tick_line_color = None
p.yaxis.axis_label = 'y axis label'
p.xaxis.axis_label = 'x axis label'
p.axis.axis_label_text_font_style = 'normal'
p.axis.axis_label_text_color = c[1]

# add 'glyphs' to the figure object
p.circle([1, 2, 3, 4, 5], [10, 3, 8, 4, 7], size=12, color=c[6], alpha=0.5)

# Note, you're not limited to circles, you can also use other markers such as:
# – asterisk()
# – circle()
# – circle_cross()
# – circle_x()
# – cross()
# – diamond()
# – diamond_cross()
# – inverted_triangle()
# – square()
# – square_cross()
# – square_x()
# – triangle()
# – x()

# you can also pass a list of sizes to be applied to each plot
p.x([1, 2, 3], [5, 6, 2], size=[10, 15, 20], color=c[5], alpha=0.7)

# define an output file
output_file('scatter_plot1.html')

# show the plot
# show(p)


# regarding output_file('file.html')
# -----------------------------------------------------------------------------
# Note that there is a mode parameter that you can pass to the output_file
# function that will determine whether the html creates links to the
# necessary javascript and css or whether these files are created and saved to
# your working directory. The default mode is 'cdn' which stands for
# 'content delivery network'. It links to css and javascript files on a remote
# server. The options are as follows:

# – cdn
# – relative
# – absolute
# – inline

# output_file('scatter_plot2.html', mode='relative')

# Both relative and absolute will link to files located in the bokeh package
# directory. For me this is:
# Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/
# site-packages/bokeh/server/static/css/bokeh.min.css

# the inline option will dump all the css and js into the html doc (ew!).


# bk.plotting with pandas, and more bokeh style examples
# -----------------------------------------------------------------------------

from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_excel('data/verlegenhuken.xlsx', sheet_name=0)

print(df.columns)
# Index(['Year', 'Month', 'Day', 'Hour', 'Temperature', 'Pressure'],...)

temperatures = df.Temperature/10  # <class 'pandas.core.series.Series'>
pressure = df.Pressure/10
toools = "pan, wheel_zoom, box_zoom, reset"

p2 = figure(plot_width=900, plot_height=600, tools=toools)
p2.title.text = 'Temperature and Air Pressure - Verlegenhuken'
p2.yaxis.axis_label = 'Pressure (hPa)'
p2.xaxis.axis_label = 'Temperature (ºC)'
p2.toolbar_location = 'right'  # below, above, left, right, None

p2.circle(temperatures, pressure, size=3, color=c[5], alpha=0.2)
output_file('scatter_plot2.html')

# show(p2)


# Time series plots
# -----------------------------------------------------------------------------
# The data for this plot comes from:
# https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory
# https://www.cryptocompare.com/coins/neo/charts/BTC?p=ALL

from bokeh.plotting import figure, output_file, show
import pandas


df = pandas.read_csv('data/neo_btc.csv', parse_dates=['timeDate'])
dates = df.timeDate
close = df.close

p3 = figure(x_axis_type='datetime', sizing_mode='stretch_both')
p3.title.text = 'Neo Coin - Historical data'
p3.yaxis.axis_label = 'Close Price (BTC)'
# p3.xaxis.axis_label = 'Date'
p3.title.text_color = 'black'
p3.title.text_font = 'Helvetica'
p3.title.text_font_size = '16pt'
p3.title.text_font_style = 'normal'
p3.axis.axis_label_text_font_style = 'bold'
p3.axis.axis_label_text_font_size = '10pt'
p3.axis.axis_label_text_color = 'black'
p3.toolbar_location = None
p3.ygrid.minor_grid_line_color = 'navy'
p3.ygrid.minor_grid_line_alpha = 0.05
p3.xgrid.grid_line_color = None
p3.xaxis.minor_tick_line_color = 'black'
p3.xaxis[0].ticker.desired_num_ticks = 10
p3.min_border_bottom = 100
p3.min_border_top = 50

p3.line(dates, close, line_width=2, color=c[5], alpha=0.9)

output_file('line_plot1.html')

# show(p3)


# Hover tools
# -----------------------------------------------------------------------------
# The data for this plot comes from:
# https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory
# https://www.cryptocompare.com/coins/neo/charts/BTC?p=ALL

from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource
import pandas


df = pandas.read_csv('data/neo_usd.csv', parse_dates=['Date'])
dates = df['Date']
close = df['Close']

p4 = figure(x_axis_type='datetime', sizing_mode='stretch_both')
p4.title.text = 'Neo Coin - Historical data'
p4.yaxis.axis_label = 'Close Price (USD)'
p4.title.text_color = 'black'
p4.title.text_font = 'Helvetica'
p4.title.text_font_size = '16pt'
p4.title.text_font_style = 'normal'
p4.axis.axis_label_text_font_style = 'bold'
p4.axis.axis_label_text_font_size = '10pt'
p4.axis.axis_label_text_color = 'black'
p4.toolbar_location = None
p4.ygrid.minor_grid_line_color = 'navy'
p4.ygrid.minor_grid_line_alpha = 0.05
p4.xgrid.grid_line_color = None
p4.xaxis.minor_tick_line_color = 'black'
p4.xaxis[0].ticker.desired_num_ticks = 10
p4.min_border_bottom = 100
p4.min_border_top = 50

cds = ColumnDataSource(df)
df['Date_str'] = df['Date'].dt.strftime('%m-%d-%Y')
hover = HoverTool(tooltips=[('Date', '@Date_str'), ('Close price', '@Close')])
p4.add_tools(hover)

p4.line(x="Date", y="Close", line_width=2, color=c[4], alpha=0.9, source=cds)

output_file('line_plot2.html')

show(p4)
