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

@app.route("/fan/<fan_name>/toggle", methods=["GET"])
def toggle_fan(fan_name):
    global lights
    # Check we have a light name that we know

    if fan_name in lights:
        print("Found Light ", fan_name)
        data = {}
        lights[fan_name].toggle()
        data[fan_name] = {"on": lights[fan_name].on, "name": fan_name}
        return jsonify({"result": True, "status": data})

    return jsonify({"result": False, "error": "Unknown light {}".format(fan_name)})



if __name__ == "__main__":
    lights = {
        "bedroom_4": LightState("bedroom_4"),
        "l2": LightState("l2"),
        "bedroom_3": LightState("bedroom_3"),
        "ds_bath_light": LightState("ds_bath_light"),
        "hall": LightState("hall"),
        "bedroom_2": LightState("bedroom_2"),
        "office": LightState("office"),
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

        "fan1": LightState("fan1"),
        "fan2": LightState("fan2"),
        "fan3": LightState("fan3"),
        "fan4": LightState("fan4"),
        "ds_bath_fan": LightState("ds_bath_fan"),
    }
    app.run()
