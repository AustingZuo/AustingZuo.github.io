import pandas as pd
from jinja2 import Template

# 读取包含属性数据的表格文件
data = pd.read_csv('D:/我的文档/Desktop/化学计量学/2023.01/diff_zeo/properties.csv')


'''
# 遍历分子筛名称，生成 option 元素的 HTML
options = ""
for name in data["ZEOTYPE"]:
    options += '<option value="{}">{}</option>\n'.format(name, name)

# 将生成的 HTML 写入文件
with open("output.html", "w") as f:
    f.write('<select>\n{}\n</select>'.format(options))


# 创建Jinja2模板对象
template = Template(open('test.html',encoding='utf-8').read())

# 遍历每行数据，并生成HTML文件
for i, row in data.iterrows():
    # 生成HTML文件名
    file_name = f'{row["ZEOTYPE"]}.html'
    
    # 渲染模板
    html = template.render(
        zeo=row['ZEOTYPE'],
        fdsi=row['FDSi'],
        lrs=row['Largest_Ring_Sizes'],
        mda=row['MDa'],
        mdb=row['MDb'],
        mdc=row['MDc'],
        mdi=row['Mdi'],
        cd=row['CD']
    )
    
    # 将HTML写入文件
    with open(file_name, 'w',encoding='utf-8') as f:
        f.write(html)
'''