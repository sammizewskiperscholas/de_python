import xml.etree.ElementTree as ET
import re

tree= ET.parse('movies.xml')
root= tree.getroot()
print(root)
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

#print([elem.tag for elem in root.iter()])

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib, movie.text)

for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)

#b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
#print(b2tf)
#b2tf.attrib["title"]= "Back to the Future"
#print(b2tf.attrib)

for movie in root.findall("./genre/decade/movie"):
    print(movie.attrib)

#tree.write("movies.xml")

for movie in root.iter('movie'):
    print(movie.attrib, movie.text)


#use regex to pattern match and fix the multiples attributes
for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')

# Write out the tree to the file again
tree.write("movies.xml")

tree = ET.parse('movies.xml')
root = tree.getroot()

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)   

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)

action= root.find("./genre[@category='Action']")
new_dec= ET.SubElement(action, 'decade')
new_dec.attrib["years"]= '2000s'
print(ET.tostring(action, encoding='utf8').decode('utf8'))

xmen= root.find("./genre/decade/movie[@title='X-Men']")
dec2000s= root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s= root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)
print(ET.tostring(action, encoding='utf8').decode('utf8'))

tree.write("movies.xml")