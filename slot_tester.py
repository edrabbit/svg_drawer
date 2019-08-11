import svgwrite

"""
Quick tool for generating slot testing cuts quickly.
The only downside is the text needs to be converted to outines before Glowforge will recognize it

|-----    -----|
|     |  |     |
|     |  |     |
|      --      |
|--------------|
"""


# all widths are in inches
canvas_width = "4in"
canvas_height = "4in"
filename = "slot_testers.svg"

def inches(coords):
  a = "%1.4fin" % coords[0]
  b = "%1.4fin" % coords[1]
  return (a,b)

def draw_line(dwg, start, end, stroke=svgwrite.rgb(10,10,16,'%')):
    start = inches(start)
    end = inches(end)
    stroke = stroke
    print("Start at %s, End at %s" % (start, end))
    dwg.add(dwg.line(start, end, stroke=stroke))

# the range here should be the size you want * 1000 i.e. 0.124 = 124 since range doesn't take floats
for slot_width in range(120, 130, 1):
    slot_width = slot_width/1000
    filename = "%1.4f - slot test.svg" % slot_width
    dwg = svgwrite.Drawing(filename, profile='tiny', height=canvas_height, width=canvas_width)

    slot_offset = (1-slot_width)/2

    x=1
    y=1
    draw_line(dwg, (x,y), (x, y+1)) # left side
    draw_line(dwg, (x,y+1), (x+1, y+1)) # bottom side
    draw_line(dwg, (x+1,y+1), (x+1, y)) # right side
    draw_line(dwg, (x,y), (x+slot_offset,y)) # left top
    draw_line(dwg, (x+1, y), (x+1-slot_offset, y)) # right top
    draw_line(dwg, (x+slot_offset, y), (x+slot_offset, y+0.5)) # down
    draw_line(dwg, (x+slot_offset, y+0.5), (x+slot_offset+slot_width, y+0.5)) # over
    draw_line(dwg, (x+slot_offset+slot_width, y+0.5), (x+slot_offset+slot_width, y)) # up

    dwg.add(dwg.textArea(text="%f" % slot_width, fill="red", x='1.1in', y='1.6in', profile="tiny"))

    dwg.save()