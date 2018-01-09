import os
import sys

if len(sys.argv) < 2:
    print "specify dir"
    sys.exit(1)

dn = sys.argv[1]

if not os.path.isdir(dn):
    print 'path', dn, 'does not exists'
    sys.exit(1)

widths = 0
heights = 0

count = 0
minw = 0
maxw = 0
minh = 0
maxh = 0
minx = 0
miny = 0
maxx = 0
maxy = 0

wvals = []
hvals = []

for fn in os.listdir(dn):
    fpath = os.path.join(dn, fn)
    lines = []

    try:
        with open(fpath, 'r') as fp:
            lines = fp.readlines()
    except:
        print 'cannot open', fp

    if len(lines) < 2:
        continue

    i = 0

    for lin in lines:
        if i == 0:
            i += 1
            continue

        cols = lin.split(' ')

        if len(cols) < 4:
            print "missing columns"
            continue

        x1 = int(cols[0])
        y1 = int(cols[1])
        x2 = int(cols[2])
        y2 = int(cols[3])

        if minx == 0 or x1 < minx: minx = x1
        if maxx == 0 or x2 > maxx: maxx = x2
        if miny == 0 or y1 < miny: miny = y1
        if maxy == 0 or y2 > maxx: maxy = y2

        w = x2 - x1
        h = y2 - y1

        hvals.append(h)
        wvals.append(w)

        print fn, w, h, x1, x2, y1, y2

        widths += w
        heights += h
        count += 1

        if minh == 0 or h < minh: minh = h
        if h > maxh: maxh = h

        if minw == 0 or w < minw: minw = w
        if w > maxw: maxw = w

if count == 0:
    print "count is zero"
    sys.exit(1)

meanw = float(widths) / count
meanh = float(heights) / count

hssum = 0
wssum = 0

for h in hvals:
    hssum += pow((h - meanh), 2)

for w in wvals:
    wssum += pow((w - meanw), 2)

print "mean w", meanw, "sigma", pow(wssum / (count - 1), 0.5), "minw", minw, "maxw", maxw, "minx", minx, "maxx", maxx
print "mean h", meanh, "sigma", pow(hssum / (count - 1), 0.5), "minh", minh, "maxh", maxh, "miny", miny, "maxy", maxy
