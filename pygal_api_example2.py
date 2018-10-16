'''Exploring API Calls'''


# The following call returns information about an article on hacker news:
# https://hacker-news.firebaseio.com/v0/item/9884165.json

# The dictionary contains of number of useful keys like title, url, score.
# The 'descendants' key contains the number of comments an article has.

import json
from operator import itemgetter

import requests
import pygal
from pygal.style import DefaultStyle as DS, LightenStyle as LS


# Make an API call and store the response:
# -----------------------------------------------------------------------------

# This API returns a list containing the IDs of top 500 articles on HN:
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

print('Status code:', r.status_code)
print('Headers:', r.headers['content-type'])
print('Encoding:', r.encoding)


# Process information about each submission:
# -----------------------------------------------------------------------------

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:100]:
    # make a separate API call for each submission:
    url = ('https://hacker-news.firebaseio.com/v0/item/'
            + str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    submission_dict = {
        'title' : response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),
        'id' : str(submission_id)
        }
    submission_dicts.append(submission_dict)


# Store the dict as a JSON to reuse while testing:
# -----------------------------------------------------------------------------

with open('hacker_news_api.json', 'w') as fob:
    json.dump(submission_dicts, fob)

with open('hacker_news_api.json') as fob:
    submission_dicts = json.load(fob)


# Sort the information:
# -----------------------------------------------------------------------------

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

submission_dicts = list(submission_dicts[15:0:-1])

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    if len(title) > 100:
        title = title[:100] + '...'
    titles.append(title)

    plot_dict = {
        'value': submission_dict['comments'],
        'label': submission_dict['id'],
        'xlink' : submission_dict['link'],
        'title' : title
        }
    plot_dicts.append(plot_dict)



# Style info:
# -----------------------------------------------------------------------------

style = LS('#25bec4', base_style=DS)

# style.plot_background = '#586e75'
# style.background = '#586e75'
style.foreground = '#586e75'             # all labels, guides
style.foreground_strong = '#13434f'      # major labels and title
# style.foreground_subtle = '#fdca32'    # minor guides

# style.font_family = 'Helvetica'
style.title_font_family = 'Helvetica'
style.label_font_family = 'Helvetica'
# style.major_label_font_family = 'Helvetica'
# style.value_font_family = 'Helvetica'
# style.value_label_font_family = 'Helvetica'
# style.tooltip_font_family = 'Helvetica'
# style.legend_font_family = 'Helvetica'
# style.no_data_font_family = 'Helvetica'

style.title_font_size = 18
style.label_font_size = 13
style.major_label_font_size = 10
# style.value_font_size = 8
# style.value_label_font_size = 8
# style.tooltip_font_size = 11
# style.legend_font_size = 10
# style.no_data_font_size = 48

# style.guide_stroke_dasharray = '2, 4'
style.major_guide_stroke_dasharray = '2, 4'
style.opacity = '.6'
style.opacity_hover = '.9'
# style.transition = '150ms'
# style.colors = ('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53')
# style.value_colors = ()


# Config info:
# -----------------------------------------------------------------------------

config = pygal.Config()
config.width = 1200
# config.height = 500
# config.spacing = 50
# config.x_title = 'x-axis'
# config.y_title = 'y-axis'
# config.human_readable = True   # for complex or large numbers
# config.stroke = False          # for line graphs
# config.fill = True             # for line graphs
# config.show_dots = False       # for line graphs
# config.dots_size = 5           # for line graphs
# config.rounded_bars = 20       # for bar graphs
# config.half_pie = True         # for pie charts
# config.inner_radius = .6       # for pie charts

# config.margin = 0
# config.margin_top = 10
config.margin_right = 100
# config.margin_bottom = 10
config.margin_left = -40

config.show_legend = False
# config.truncate_legend = -1
# config.legend_box_size = 15
# config.legend_at_bottom = True
# config.legend_at_bottom_columns = 4

config.show_x_labels = True
config.x_labels = titles
# config.x_label_rotation = 45
# config.x_labels_major = [0, 5, 10]
# config.x_labels_major_every = 3
# config.x_labels_major_count = 5
# config.show_minor_x_labels = True

config.show_y_labels = True
# config.y_labels = names
# config.y_label_rotation = 45
# config.y_labels_major = [0, 50, 100]
config.y_labels_major_every = 1
# config.y_labels_major_count = 2
config.show_minor_y_labels = True

# config.truncate_label = 15

# config.inverse_y_axis = True
# config.inverse_x_axis = True
# config.print_values = True
# config.dynamic_print_values = True
# config.tooltip_border_radius = 3
# config.show_y_guides = True
# config.show_x_guides = True


# Create and populate the plot:
# -----------------------------------------------------------------------------

chart = pygal.HorizontalBar(config, style=style)
chart.title = "Most-commented articles on Hacker News top 100"

chart.add('', plot_dicts)

chart.render_to_file('hacker_news_api.svg')
