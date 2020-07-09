'''Data visualization using a web API'''


# A program that downloads current information about the most-starred
# Python projects in GitHub. Some helpful links:

# https://api.github.com
# https://developer.github.com/v3/search/
# https://help.github.com/articles/searching-repositories/
# https://help.github.com/articles/understanding-the-search-syntax/
# http://docs.python-requests.org

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Processing an API response
# -----------------------------------------------------------------------------

# make an API call and store the requests:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# It's always go to check the status - use these to make some asserts.
print('Status code:', r.status_code)
print('Headers:', r.headers['content-type'])
print('Encoding:', r.encoding)
# Status code: 200  (a status code of 200 indicates a successful response)
# Headers: application/json; charset=utf-8
# Encoding: utf-8

# Store API response in a variable. The API returns info in JSON format so we
# use the json() method to convert to a python dict.
response_dict = r.json()
print(type(response_dict))  # -> <class 'dict'>

# process results:
print(response_dict.keys())
print('Total repositories:', response_dict['total_count'])
print('Incomplete results:', response_dict['incomplete_results'])
print('Repositories returned:', len(response_dict['items']))
# dict_keys(['total_count', 'incomplete_results', 'items'])
# Incomplete results: False
# Total repositories: 2077471
# Repositories returned: 30

repo_dicts = response_dict['items']

# examine the first repo:
# repo_dict1 = repo_dicts[0]
# print('\nKeys:', len(repo_dict1))
# for key in sorted(repo_dict1.keys()):
#     print(key, '–', repo_dict1[key])


# Summarizing the top repos
# -----------------------------------------------------------------------------

print('\nSome information about the top 30 repository:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])


# Monitoring API rate limits
# -----------------------------------------------------------------------------

# most APIs are rate-limited, which means there's a limit to how many requests
# you can make in a certain amount of time. To see if you're approaching
# GitHub's limits: https://api.github.com/rate_limit


# Prep the data for plotting:
# -----------------------------------------------------------------------------
#
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

# NOTE: You can add custom tooltips by passing a list of dictionaries instead
# of a list of values to chart.add() like so:
# plot_dict = [
#     {'value': 1314, 'label': 'Description...'},
#     {'value': 5670, 'label': 'Description...'},
#     {'value': 3224, 'label': 'Description...'},]

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # get the description if one is available:
    description = repo_dict['description']
    if not description:
        description = 'No description provided'
    if len(description) > 118:
        description = description[:118] + '...'

# NOTE: pygal uses the value given for 'xlink' to turn each bar into an active
# link to the given url. You can also add links to the legend. See the docs:
# http://pygal.org/en/stable/documentation/configuration/value.html#legend

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink' : repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)


# Visualizing the repos with pygal
# -----------------------------------------------------------------------------

my_style = LS('#25bec4', base_style=LCS)
my_style.title_font_family = 'Helvetica'

# NOTE: google fonts will only render when the svg is embedded because the
# google stylesheet is added in the XML processing.
# my_style.title_font_family = 'googlefont:Slabo'

my_style.title_font_size = 14
my_style.foreground = '#586e75'
my_style.foreground_strong = '#334145'
my_style.foreground_subtle = '#fdca32'
my_style.label_font_size = 9
my_style.major_label_font_size = 12
my_style.tooltip_font_size = 11

my_config = pygal.Config()
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000

my_config.y_labels = list(range(0, 42000, 2000))
my_config.y_labels_major_count = 3
my_config.x_labels = names
my_config.x_label_rotation = 45

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"

# chart.add('', stars)
chart.add('', plot_dicts)
chart.render_to_file('api_pygal_example.svg')
