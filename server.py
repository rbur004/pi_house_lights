#!/usr/bin/python3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__,static_folder='static',static_url_path='')

# Record state of a light
class LightState:
    def __init__(self, light_name):
        self.on = False
        self.dimmable = False
        self.level = 255
        self.light_name = light_name

    def toggle(self):
        self.on = not self.on

    def on(self):
        self.on = True

    def off(self):
        self.off = False


@app.route("/light/<light_name>/toggle", methods=["GET"])
def toggle(light_name):
    global lights
    # Check we have a light name that we know

    if light_name in lights:
        print("Found Light ", light_name)
        data = {}
        lights[light_name].toggle()
        data[light_name] = {"on": lights[light_name].on, "name": light_name}
        return jsonify({"result": True, "status": data})

    return jsonify({"result": False, "error": "Unknown light {}".format(light_name)})


@app.route("/light/<light_name>/on", methods=["GET"])
def on(light_name):
    global lights
    # Check we have a light name that we know
    if light_name in lights:
        data = {}
        lights[light_name].on()
        data[light_name] = {"on": lights[light_name].on, "name": light_name}
        return jsonify({"result": True, "status": data})

    return jsonify({"result": False, "error": "Unknown light {}".format(light_name)})


@app.route("/light/<light_name>/off", methods=["GET"])
def off(light_name):
    global lights
    # Check we have a light name that we know
    if light_name in lights:
        data = {}
        lights[light_name].off()
        data[light_name] = {"on": lights[light_name].on, "name": light_name}
        return jsonify({"result": True, "status": data})

    return jsonify({"result": False, "error": "Unknown light {}".format(light_name)})


@app.route("/lights/status", methods=["GET"])
def status():
    if request.method == "GET":
        data = {}
        for name, l in lights.items():
            data[name] = {"on": l.on, "name": l.light_name}

        return jsonify({"result": True, "status": data})

    return jsonify({"result": False, "error": "Use GET"})


if __name__ == "__main__":
    lights = {
        "l1": LightState("l1"),
        "l2": LightState("l2"),
        "l3": LightState("l3"),
        "l4": LightState("l4"),
        "l5": LightState("l5"),
        "l6": LightState("l6"),
        "l7": LightState("l7"),
        "l8": LightState("l8"),
        "l9": LightState("l9"),
        "l10": LightState("l10"),
        "l11": LightState("l11"),
        "l12": LightState("l12"),
        "l13": LightState("l13"),
        "l14": LightState("l14"),
        "l15": LightState("l15"),
        "l16": LightState("l16"),
        "l17": LightState("l17"),
        "l18": LightState("l18"),
        "l19": LightState("l19"),
        "l20": LightState("l20"),
        "l21": LightState("l21"),
    }
    app.run()
