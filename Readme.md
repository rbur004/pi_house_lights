# Control House lights from a Web page

Simple Python Flask example, using an SVG drawing of a house with coloured circles representing the lights

# SVG_ID2URL
SVG elements with an onclick="window.parent.exec_url(this.id)" will call the javascript exec_url() function in the main html. This then uses Ajax to go to the URL, and look for a json response.

* Function exec_url() uses the svg_id2url.js array to map SVG ids to URLs. 
* The array also holds light name mappings to svg_id, as we may have more than one clickable SVG item, mapping to a light.
* The array also tells the status callback handler, which items to alter the colour of.

# Called with
http://127.0.0.1:5000/house.html
