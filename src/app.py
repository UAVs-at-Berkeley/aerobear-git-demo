import json
import os
import sys

from flask import Flask, request
app = Flask(__name__)


html = """
<html>
<head>
<script type="text/javascript" src="paper.js"></script>
<script type="text/paperscript" canvas="myCanvas">
// Adapted from the following Processing example:
// http://processing.org/learning/topics/follow3.html
// The amount of points in the path:


var points = {point};

// The distance between the points:
var length = {length};

var path = new Path({
	strokeColor: '#E4141B',
	strokeWidth: 20,
	strokeCap: 'round'
});

var start = view.center / [10, 1];
for (var i = 0; i < points; i++)
	path.add(start + new Point(i * length, 0));

function onMouseMove(event) {
	path.firstSegment.point = event.point;
	for (var i = 0; i < points - 1; i++) {
		var segment = path.segments[i];
		var nextSegment = segment.next;
		var vector = segment.point - nextSegment.point;
		vector.length = length;
                nextSegment.point = segment.point - vector;
	}
	path.smooth({ type: 'continuous' });
}

function onMouseDown(event) {
	path.fullySelected = true;
	path.strokeColor = '#e08285';
}

function onMouseUp(event) {
	path.fullySelected = false;
	path.strokeColor = '#e4141b';
}
</script>
<body>
<marquee scrollamount="10">{names}</marquee>
<canvas style="height:100%;" id="myCanvas" resize></canvas>
</head>
</body>
</html>
"""

@app.route('/')
def hello():
    text = []
    parent_path = os.path.expanduser('~/git-demo/data/')
    files = [f for f in os.listdir(parent_path)]

    for f in files:
        with open(os.path.join(parent_path, f)) as _data:
            data = json.load(_data)
            text.extend([str(data['name'])])
    return html.replace("{point}", "20").replace("{length}", "45").replace("{names}", str(text))

if __name__ == '__main__':
    app.run()
