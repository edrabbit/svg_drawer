import svgwrite

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


# all widths are in inches
canvas_width = "20in"
canvas_height = "12in"

# Draftboard dividers
material = "draftboard"
slot_width = 0.124

# Acrylic dividers
#material = "acrylic"
#slot_width = 0.108

dd_length = 16.7 # same as width
dd_height = 5.38
slot_height = dd_height / 2
end_spacer = .5  # how wide is the last tab on each side?
num_of_slots = 7
slot_spacing = (-(slot_width * num_of_slots)-(2*end_spacer)+dd_length)/(num_of_slots-1)

filename = ("%s drawer_divider %sx%s - %d slots - %s slot width - %1.4f spacing - %s end tabs.svg"
            % (material, dd_length, dd_height, num_of_slots, slot_width, slot_spacing, end_spacer))
# offset to start drawing
x = 1
y = 1

dwg = svgwrite.Drawing(filename, profile='tiny', height=canvas_height, width=canvas_width)

lines = [
    ((x,y), (x,y+dd_height)), # Left side vertical line
    ((x+dd_length,y), (x+dd_length,y+dd_height)), # right side, vertical line
    ((x,y+dd_height), (x+dd_length, y+dd_height)), # bottom edge
    ((x,y), (x+end_spacer, y)), # left side, first tab
    ((x+dd_length, y), (x+dd_length-end_spacer, y)), # right side, last tab
]

for line in lines:
    draw_line(dwg, line[0], line[1])

# offset the width of the first tab
xx = x+end_spacer

print("draw first slot")
draw_line(dwg, (xx, y), (xx, y+slot_height))  # down
draw_line(dwg, (xx, y+slot_height), (xx+slot_width, y+slot_height))  # over
draw_line(dwg, (xx+slot_width, y+slot_height), (xx+slot_width, y))  # up
xx = xx + slot_width

for i in range(1,num_of_slots):
    print("draw %s slot" % (i+1))
    draw_line(dwg, (xx, y), (xx+slot_spacing, y)) # tab
    xx = xx+slot_spacing
    draw_line(dwg, (xx, y), (xx, y+slot_height)) # down
    draw_line(dwg, (xx,y+slot_height), (xx+slot_width, y+slot_height)) # over
    draw_line(dwg, (xx+slot_width, y+slot_height), (xx+slot_width, y)) # up
    xx = xx+slot_width

dwg.save()
