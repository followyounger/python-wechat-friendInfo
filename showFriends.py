# coding=gbk
import itchat
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]

provincesName = []
for item in friends:
	provincesName.append(item['Province'])
provinces = set(provincesName)
provinces = list(provinces)
numbers = []
for item in provinces:
	plot_province = {
	    'value':provincesName.count(item),
	    'label':item
	}
	numbers.append(plot_province)

provinces = ['未设置' if x=='' else x for x in provinces]
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 2000

chart = pygal.Bar(my_config,style=my_style)
chart.title = '我的好友省分布'
chart.x_labels = provinces
chart.add('人数',numbers)
chart.render_to_file('friends.svg')

