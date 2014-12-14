import svgfig
baseDir = "C:\\Users\\ewew\\Dropbox\\_PROJECTS\\2014.08.24 Kruglendar_2015\\python\\"

# read in the "SVGFig" text I typed and converted into paths
dayShapes = svgfig.load(baseDir+"dayShapes.svg")
print repr(dayShapes)
weekdayShape = ''
weekendShape = ''
for ti, s in dayShapes:
    try:
        for pair in s.attr.items():
            if pair[0] == u'id':
                if pair[1] == u'weekday':
                    weekdayShape = s
                    print "yo1"
                elif pair[1] == u'weekend':
                    weekendShape = s
                    print "yo2"
    except Exception, e:
        continue

if weekdayShape == '':
    print("Weekday not found in svg")
elif weekendShape == '':
    print("Weekend not found in svg")

print repr(weekdayShape)
print repr(weekendShape)

#dayShape = SVG("rect", x=10, y=10, width=60, height=60, fill="red")
#dayShape.load(baseDir+"day-shape.svg")

#s = SVG("rect", x=10, y=10, width=60, height=60, fill="red")
#s2= SVG("rect", x=30, y=30, width=60, height=60, fill="blue")
#g = SVG("g", s, s2, fill_opacity="50%")
#g.save(baseDir + "tmp.svg")
