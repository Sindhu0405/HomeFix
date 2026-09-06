# ============================================================
# HOMEFIX - SMART DIAGNOSIS SERVICE
# ============================================================
#
# Supports:
# Refrigerator       - 10 problems
# Washing Machine    - 10 problems
# AC                 - 10 problems
# TV                 - 10 problems
# Microwave          - 8 problems
# Fan                - 7 problems
# Oven               - 8 problems
# Dishwasher         - 8 problems
# Water Heater       - 7 problems
# Vacuum Cleaner     - 7 problems
#
# Total: 85 common customer problems
# ============================================================


# ============================================================
# HELPER
# ============================================================

def rule(causes, checks, repair_range, recommendation=None):
    return {
        "causes": causes,
        "checks": checks,
        "range": repair_range,
        "recommendation": recommendation
        or "If the safe checks do not resolve the issue, professional inspection may be required."
    }


# ============================================================
# DIAGNOSIS RULES
# ============================================================

RULES = {

    # ========================================================
    # REFRIGERATOR
    # ========================================================

    "refrigerator": {

        "not_cooling": rule(
            [
                {"cause": "Incorrect temperature setting", "likelihood": "Medium"},
                {"cause": "Blocked airflow inside the refrigerator", "likelihood": "Medium"},
                {"cause": "Dirty condenser area", "likelihood": "Medium"},
                {"cause": "Cooling-system or compressor problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the refrigerator temperature is set correctly.",
                "Make sure internal air vents are not blocked by food.",
                "Check that the door closes completely.",
                "Do not attempt to handle refrigerant or open sealed cooling components."
            ],
            "₹300 – ₹8,000+"
        ),

        "cooling_weak": rule(
            [
                {"cause": "Dirty or blocked airflow path", "likelihood": "Medium"},
                {"cause": "Incorrect temperature setting", "likelihood": "Medium"},
                {"cause": "Door seal allowing warm air inside", "likelihood": "Medium"},
                {"cause": "Cooling-system fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the temperature setting.",
                "Avoid overloading the refrigerator.",
                "Make sure air vents are not blocked.",
                "Check whether the door seal is closing properly."
            ],
            "₹300 – ₹6,000"
        ),

        "too_much_ice_frost": rule(
            [
                {"cause": "Door being left open or poor door sealing", "likelihood": "High"},
                {"cause": "Blocked airflow", "likelihood": "Medium"},
                {"cause": "Defrost-system problem", "likelihood": "Medium"},
                {"cause": "Temperature setting too low", "likelihood": "Medium"},
            ],
            [
                "Check that the door closes properly.",
                "Check the door gasket for visible damage.",
                "Do not chip ice using sharp objects.",
                "Follow the manufacturer's defrost instructions."
            ],
            "₹300 – ₹5,000"
        ),

        "water_leaking": rule(
            [
                {"cause": "Blocked or frozen drain", "likelihood": "High"},
                {"cause": "Drain tray or drain pipe issue", "likelihood": "Medium"},
                {"cause": "Door seal problem", "likelihood": "Medium"},
                {"cause": "Internal water-line issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check where the water is collecting.",
                "Check for a visibly blocked drain if accessible according to the manual.",
                "Check that the refrigerator is positioned correctly.",
                "Do not remove sealed or electrical components."
            ],
            "₹300 – ₹4,000"
        ),

        "unusual_noise": rule(
            [
                {"cause": "Fan contacting ice or another component", "likelihood": "Medium"},
                {"cause": "Refrigerator not level", "likelihood": "Medium"},
                {"cause": "Compressor or motor noise", "likelihood": "Low/Medium"},
                {"cause": "Loose internal component", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the refrigerator is standing level.",
                "Check whether the noise changes when the door is opened.",
                "Make sure the refrigerator is not touching the wall or nearby furniture.",
                "Do not attempt to open the compressor compartment."
            ],
            "₹300 – ₹8,000+"
        ),

        "not_turning_on": rule(
            [
                {"cause": "Power outlet or plug issue", "likelihood": "High"},
                {"cause": "Power cord problem", "likelihood": "Medium"},
                {"cause": "Thermostat or control problem", "likelihood": "Medium"},
                {"cause": "Electrical component failure", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the power plug is connected securely.",
                "Check the wall outlet using another safe appliance.",
                "Check whether the refrigerator display or interior light works.",
                "Do not open electrical components."
            ],
            "₹300 – ₹5,000"
        ),

        "compressor_not_working": rule(
            [
                {"cause": "Compressor start component problem", "likelihood": "Medium"},
                {"cause": "Control system fault", "likelihood": "Medium"},
                {"cause": "Compressor failure", "likelihood": "Low/Medium"},
            ],
            [
                "Check whether the refrigerator has power.",
                "Listen for repeated clicking or starting sounds.",
                "Check the temperature and display indicators.",
                "Do not attempt compressor or refrigerant repair yourself."
            ],
            "₹1,500 – ₹10,000+",
            "A compressor-related issue normally requires professional diagnosis before replacement."
        ),

        "door_not_sealing": rule(
            [
                {"cause": "Dirty door gasket", "likelihood": "High"},
                {"cause": "Damaged or deformed gasket", "likelihood": "Medium"},
                {"cause": "Door alignment problem", "likelihood": "Medium"},
                {"cause": "Obstruction inside the refrigerator", "likelihood": "Medium"},
            ],
            [
                "Clean the accessible door gasket.",
                "Check that food containers are not preventing the door from closing.",
                "Inspect the gasket for visible damage.",
                "Do not force or bend the door hardware."
            ],
            "₹300 – ₹2,500"
        ),

        "bad_smell": rule(
            [
                {"cause": "Spoiled or uncovered food", "likelihood": "High"},
                {"cause": "Dirty shelves or interior", "likelihood": "High"},
                {"cause": "Blocked drain with residue", "likelihood": "Medium"},
                {"cause": "Unusual electrical smell from a component", "likelihood": "Low"},
            ],
            [
                "Remove spoiled or expired food.",
                "Clean accessible shelves and interior surfaces.",
                "Check for food or liquid around the drain area.",
                "If the smell is burning or electrical, unplug the appliance if safe and seek professional help."
            ],
            "₹200 – ₹1,500"
        ),

        "light_not_working": rule(
            [
                {"cause": "Failed bulb or LED module", "likelihood": "High"},
                {"cause": "Door switch problem", "likelihood": "Medium"},
                {"cause": "Control or wiring issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check whether the refrigerator is otherwise operating normally.",
                "Check the door switch for visible damage.",
                "Replace a user-replaceable bulb only according to the manual.",
                "Do not open electrical wiring."
            ],
            "₹200 – ₹1,500"
        ),
    },


    # ========================================================
    # WASHING MACHINE
    # ========================================================

    "washing machine": {

        "not_starting": rule(
            [
                {"cause": "Power supply or plug issue", "likelihood": "High"},
                {"cause": "Door/lid not properly closed", "likelihood": "Medium"},
                {"cause": "Control panel problem", "likelihood": "Medium"},
                {"cause": "Electronic control board fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the power plug is connected securely.",
                "Make sure the door or lid is fully closed.",
                "Check the display for an error code.",
                "Do not open electrical components."
            ],
            "₹300 – ₹2,500"
        ),

        "not_spinning": rule(
            [
                {"cause": "Unbalanced laundry load", "likelihood": "High"},
                {"cause": "Door/lid lock issue", "likelihood": "Medium"},
                {"cause": "Drainage problem", "likelihood": "Medium"},
                {"cause": "Drive system or motor problem", "likelihood": "Low/Medium"},
            ],
            [
                "Redistribute the clothes evenly.",
                "Make sure the door or lid closes correctly.",
                "Check whether water has drained from the drum.",
                "Do not attempt motor or electrical repairs."
            ],
            "₹500 – ₹4,000"
        ),

        "not_draining_water": rule(
            [
                {"cause": "Blocked drain filter", "likelihood": "High"},
                {"cause": "Blocked drain hose", "likelihood": "Medium"},
                {"cause": "Drain pump problem", "likelihood": "Medium"},
            ],
            [
                "Check the drain hose for visible kinks.",
                "Check the drain filter only according to the manufacturer's instructions.",
                "Never reach into a moving drum.",
                "Do not open electrical components."
            ],
            "₹500 – ₹2,500"
        ),

        "not_filling_water": rule(
            [
                {"cause": "Water supply turned off", "likelihood": "High"},
                {"cause": "Blocked inlet hose or filter", "likelihood": "Medium"},
                {"cause": "Water inlet valve problem", "likelihood": "Medium"},
                {"cause": "Control system problem", "likelihood": "Low"},
            ],
            [
                "Check that the water tap is turned on.",
                "Check the inlet hose for visible kinks.",
                "Check for an error code.",
                "Do not dismantle the water inlet valve."
            ],
            "₹300 – ₹3,000"
        ),

        "water_leaking": rule(
            [
                {"cause": "Loose or damaged hose connection", "likelihood": "High"},
                {"cause": "Door gasket problem", "likelihood": "Medium"},
                {"cause": "Detergent drawer overflow", "likelihood": "Medium"},
                {"cause": "Internal component leak", "likelihood": "Low/Medium"},
            ],
            [
                "Stop the cycle if water is leaking heavily.",
                "Check accessible hose connections.",
                "Check the door gasket for visible damage.",
                "Keep water away from electrical connections."
            ],
            "₹300 – ₹4,000"
        ),

        "excessive_vibration": rule(
            [
                {"cause": "Unbalanced load", "likelihood": "High"},
                {"cause": "Machine not level", "likelihood": "High"},
                {"cause": "Installation or flooring problem", "likelihood": "Medium"},
                {"cause": "Suspension component problem", "likelihood": "Low/Medium"},
            ],
            [
                "Redistribute the clothes.",
                "Check whether the machine is level.",
                "Make sure the machine is standing firmly.",
                "Stop using it if severe movement creates a safety risk."
            ],
            "₹300 – ₹3,500"
        ),

        "making_loud_noise": rule(
            [
                {"cause": "Foreign object in the drum", "likelihood": "Medium"},
                {"cause": "Unbalanced load", "likelihood": "Medium"},
                {"cause": "Bearing or drive-system problem", "likelihood": "Low/Medium"},
                {"cause": "Loose component", "likelihood": "Low/Medium"},
            ],
            [
                "Check pockets and remove loose objects from clothing.",
                "Run an appropriate empty or light cycle if recommended by the manual.",
                "Observe whether the sound occurs only during spinning.",
                "Do not open the machine to inspect internal parts."
            ],
            "₹500 – ₹5,000+"
        ),

        "clothes_not_cleaned": rule(
            [
                {"cause": "Overloading the washing machine", "likelihood": "High"},
                {"cause": "Incorrect detergent quantity", "likelihood": "Medium"},
                {"cause": "Incorrect wash program", "likelihood": "Medium"},
                {"cause": "Dirty drum or filter", "likelihood": "Medium"},
            ],
            [
                "Avoid overloading the machine.",
                "Use the recommended detergent quantity.",
                "Select a suitable wash program.",
                "Clean accessible filters and the drum according to the manual."
            ],
            "₹200 – ₹2,000"
        ),

        "door_not_opening": rule(
            [
                {"cause": "Water still present in the drum", "likelihood": "High"},
                {"cause": "Cycle or safety lock still active", "likelihood": "High"},
                {"cause": "Door lock mechanism problem", "likelihood": "Medium"},
            ],
            [
                "Wait for the cycle to finish and unlock normally.",
                "Check whether water remains inside.",
                "Do not force the door open.",
                "Follow the manual's emergency door-release procedure if available."
            ],
            "₹500 – ₹3,000"
        ),

        "error_code": rule(
            [
                {"cause": "The displayed code may indicate a specific appliance fault", "likelihood": "High"},
                {"cause": "Water supply or drainage issue", "likelihood": "Medium"},
                {"cause": "Door or control-system issue", "likelihood": "Medium"},
            ],
            [
                "Write down the exact error code.",
                "Check the manufacturer's manual for that code.",
                "Try only the reset procedure recommended by the manufacturer.",
                "Do not bypass safety systems."
            ],
            "₹300 – ₹5,000+",
            "The exact error code is needed for a more specific diagnosis."
        ),
    },


    # ========================================================
    # AC
    # ========================================================

    "ac": {

        "not_cooling": rule(
            [
                {"cause": "Dirty air filter", "likelihood": "High"},
                {"cause": "Incorrect temperature or mode setting", "likelihood": "Medium"},
                {"cause": "Blocked airflow", "likelihood": "Medium"},
                {"cause": "Refrigerant or cooling-system problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the AC is in cooling mode.",
                "Check and clean the accessible air filter according to the manual.",
                "Make sure air vents are not blocked.",
                "Do not handle refrigerant yourself."
            ],
            "₹300 – ₹8,000+"
        ),

        "cooling_weak": rule(
            [
                {"cause": "Dirty air filter", "likelihood": "High"},
                {"cause": "Blocked indoor or outdoor airflow", "likelihood": "Medium"},
                {"cause": "Incorrect temperature setting", "likelihood": "Medium"},
                {"cause": "Refrigerant or system issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check the cooling mode and temperature.",
                "Clean the accessible air filter.",
                "Keep indoor and outdoor airflow paths clear.",
                "Arrange professional service if cooling remains weak."
            ],
            "₹300 – ₹6,000+"
        ),

        "blowing_warm_air": rule(
            [
                {"cause": "Incorrect mode setting", "likelihood": "Medium"},
                {"cause": "Dirty filter", "likelihood": "Medium"},
                {"cause": "Outdoor unit problem", "likelihood": "Medium"},
                {"cause": "Refrigerant or compressor issue", "likelihood": "Low/Medium"},
            ],
            [
                "Confirm that cooling mode is selected.",
                "Check the temperature setting.",
                "Clean the accessible filter.",
                "Do not open the refrigerant system."
            ],
            "₹300 – ₹8,000+"
        ),

        "water_leaking": rule(
            [
                {"cause": "Blocked condensate drain", "likelihood": "High"},
                {"cause": "Dirty filter or coil causing excess condensation", "likelihood": "Medium"},
                {"cause": "Drain hose problem", "likelihood": "Medium"},
                {"cause": "Installation or internal drainage issue", "likelihood": "Low/Medium"},
            ],
            [
                "Turn off the AC if water is reaching electrical areas.",
                "Check the accessible drain outlet for obvious blockage.",
                "Check and clean the air filter according to the manual.",
                "Arrange professional service if leaking continues."
            ],
            "₹300 – ₹4,000"
        ),

        "unusual_noise": rule(
            [
                {"cause": "Loose panel or component", "likelihood": "Medium"},
                {"cause": "Fan obstruction", "likelihood": "Medium"},
                {"cause": "Fan motor problem", "likelihood": "Low/Medium"},
                {"cause": "Compressor-related problem", "likelihood": "Low"},
            ],
            [
                "Check whether the noise comes from the indoor or outdoor unit.",
                "Make sure there are no visible obstructions.",
                "Do not open the AC housing.",
                "Turn the unit off if the noise is severe or accompanied by burning smell."
            ],
            "₹500 – ₹8,000+"
        ),

        "not_turning_on": rule(
            [
                {"cause": "Power supply problem", "likelihood": "High"},
                {"cause": "Remote control or battery issue", "likelihood": "Medium"},
                {"cause": "Circuit or control-board problem", "likelihood": "Medium"},
                {"cause": "Internal electrical fault", "likelihood": "Low"},
            ],
            [
                "Check the power supply.",
                "Check the remote batteries.",
                "Try the AC's manual power button if the model provides one.",
                "Do not open electrical components."
            ],
            "₹300 – ₹5,000"
        ),

        "bad_smell": rule(
            [
                {"cause": "Dirty air filter", "likelihood": "High"},
                {"cause": "Dust or moisture buildup", "likelihood": "Medium"},
                {"cause": "Drain or microbial buildup", "likelihood": "Medium"},
                {"cause": "Electrical overheating", "likelihood": "Low"},
            ],
            [
                "Clean the accessible filter.",
                "Check for visible moisture around the indoor unit.",
                "Arrange professional cleaning if the smell continues.",
                "If there is a burning/electrical smell, switch off the AC and seek professional help."
            ],
            "₹300 – ₹3,000"
        ),

        "remote_not_working": rule(
            [
                {"cause": "Weak or dead batteries", "likelihood": "High"},
                {"cause": "Blocked remote sensor", "likelihood": "Medium"},
                {"cause": "Remote control fault", "likelihood": "Medium"},
                {"cause": "AC receiver problem", "likelihood": "Low"},
            ],
            [
                "Replace the remote batteries.",
                "Clean the remote sensor area.",
                "Point the remote directly toward the indoor unit.",
                "Use manual controls if available."
            ],
            "₹150 – ₹2,000"
        ),

        "ice_forming": rule(
            [
                {"cause": "Restricted airflow from dirty filter", "likelihood": "High"},
                {"cause": "Low refrigerant", "likelihood": "Medium"},
                {"cause": "Evaporator or fan problem", "likelihood": "Medium"},
            ],
            [
                "Switch off cooling and allow visible ice to thaw.",
                "Check and clean the accessible air filter.",
                "Do not scrape ice using sharp objects.",
                "Arrange professional service if ice returns."
            ],
            "₹300 – ₹7,000+"
        ),

        "high_electricity_consumption": rule(
            [
                {"cause": "Dirty filter or coil", "likelihood": "High"},
                {"cause": "Incorrect temperature setting", "likelihood": "Medium"},
                {"cause": "Poor room insulation or excessive heat load", "likelihood": "Medium"},
                {"cause": "Refrigeration-system efficiency problem", "likelihood": "Low/Medium"},
            ],
            [
                "Clean the accessible filter.",
                "Avoid setting the temperature unnecessarily low.",
                "Keep doors and windows closed while cooling.",
                "Arrange servicing if electricity consumption suddenly increases."
            ],
            "₹300 – ₹6,000+"
        ),
    },


    # ========================================================
    # TV
    # ========================================================

    "tv": {

        "not_turning_on": rule(
            [
                {"cause": "Power outlet or cable issue", "likelihood": "High"},
                {"cause": "Remote or battery issue", "likelihood": "Medium"},
                {"cause": "Power board or internal electrical fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power cable.",
                "Check the wall outlet using another safe device.",
                "Try the TV's physical power button.",
                "Do not open the TV."
            ],
            "₹300 – ₹5,000+"
        ),

        "no_picture": rule(
            [
                {"cause": "Incorrect input/source selected", "likelihood": "High"},
                {"cause": "Cable or connected-device problem", "likelihood": "Medium"},
                {"cause": "Backlight or display hardware issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check the selected input/source.",
                "Reconnect external HDMI or video cables.",
                "Try another input if available.",
                "Do not open the TV panel."
            ],
            "₹300 – ₹12,000+"
        ),

        "no_sound": rule(
            [
                {"cause": "Muted or low volume", "likelihood": "High"},
                {"cause": "Incorrect audio output setting", "likelihood": "Medium"},
                {"cause": "Connected audio device issue", "likelihood": "Medium"},
                {"cause": "Speaker or audio-board fault", "likelihood": "Low"},
            ],
            [
                "Check volume and mute settings.",
                "Check the selected audio output.",
                "Disconnect external audio devices and test again.",
                "Do not open the TV."
            ],
            "₹300 – ₹6,000"
        ),

        "screen_flickering": rule(
            [
                {"cause": "Loose or faulty video cable", "likelihood": "Medium"},
                {"cause": "Signal/source problem", "likelihood": "Medium"},
                {"cause": "Display panel or backlight issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check HDMI or other video connections.",
                "Try another source or input.",
                "Restart the TV.",
                "Arrange professional inspection if flickering remains."
            ],
            "₹300 – ₹12,000+"
        ),

        "lines_on_screen": rule(
            [
                {"cause": "Signal or cable problem", "likelihood": "Medium"},
                {"cause": "Display panel fault", "likelihood": "Medium/High"},
                {"cause": "Internal display connection issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check whether the lines appear on every input.",
                "Restart the TV.",
                "Try another source.",
                "Do not press or bend the screen."
            ],
            "₹500 – ₹20,000+"
        ),

        "remote_not_working": rule(
            [
                {"cause": "Dead or weak batteries", "likelihood": "High"},
                {"cause": "Blocked or dirty TV sensor", "likelihood": "Medium"},
                {"cause": "Remote control fault", "likelihood": "Medium"},
            ],
            [
                "Replace the remote batteries.",
                "Make sure nothing blocks the TV sensor.",
                "Clean the remote sensor and buttons gently.",
                "Try the TV's physical controls."
            ],
            "₹150 – ₹2,000"
        ),

        "hdmi_not_working": rule(
            [
                {"cause": "Faulty or loose HDMI cable", "likelihood": "High"},
                {"cause": "Incorrect TV input", "likelihood": "Medium"},
                {"cause": "External device output problem", "likelihood": "Medium"},
                {"cause": "HDMI port fault", "likelihood": "Low/Medium"},
            ],
            [
                "Select the correct HDMI input.",
                "Reconnect the HDMI cable.",
                "Try another HDMI cable.",
                "Try another HDMI port if available."
            ],
            "₹200 – ₹4,000"
        ),

        "wifi_not_connecting": rule(
            [
                {"cause": "Incorrect Wi-Fi password", "likelihood": "High"},
                {"cause": "Weak Wi-Fi signal", "likelihood": "Medium"},
                {"cause": "Router or network problem", "likelihood": "Medium"},
                {"cause": "TV network hardware/software issue", "likelihood": "Low"},
            ],
            [
                "Check the Wi-Fi password.",
                "Restart the router and TV.",
                "Move the router closer if possible.",
                "Check whether other devices can connect to the same network."
            ],
            "₹0 – ₹3,000"
        ),

        "apps_not_opening": rule(
            [
                {"cause": "Internet connection problem", "likelihood": "High"},
                {"cause": "Outdated TV software", "likelihood": "Medium"},
                {"cause": "App service or account issue", "likelihood": "Medium"},
                {"cause": "TV storage/software problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check the TV's internet connection.",
                "Restart the TV.",
                "Check for software and app updates.",
                "Try another app to determine whether the issue is app-specific."
            ],
            "₹0 – ₹3,000"
        ),

        "restarting_automatically": rule(
            [
                {"cause": "Power connection problem", "likelihood": "Medium"},
                {"cause": "Software or firmware issue", "likelihood": "Medium"},
                {"cause": "Overheating", "likelihood": "Medium"},
                {"cause": "Power-board fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power cable and outlet.",
                "Make sure ventilation openings are not blocked.",
                "Check for software updates.",
                "If repeated restarting continues, arrange professional inspection."
            ],
            "₹300 – ₹6,000+"
        ),
    },


    # ========================================================
    # MICROWAVE
    # ========================================================

    "microwave": {

        "not_heating": rule(
            [
                {"cause": "Incorrect cooking settings", "likelihood": "Medium"},
                {"cause": "Door not closing correctly", "likelihood": "Medium"},
                {"cause": "Heating component or control fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the selected power and cooking mode.",
                "Make sure the door closes fully.",
                "Test with a suitable microwave-safe container.",
                "Do not open or repair the microwave yourself."
            ],
            "₹500 – ₹5,000+"
        ),

        "not_turning_on": rule(
            [
                {"cause": "Power outlet or plug issue", "likelihood": "High"},
                {"cause": "Door safety switch issue", "likelihood": "Medium"},
                {"cause": "Internal electrical fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power outlet.",
                "Check that the door closes completely.",
                "Check the display for signs of power.",
                "Do not open the microwave casing."
            ],
            "₹300 – ₹4,000"
        ),

        "sparking_inside": rule(
            [
                {"cause": "Metal object or unsuitable container", "likelihood": "High"},
                {"cause": "Food residue or grease inside the cavity", "likelihood": "Medium"},
                {"cause": "Damaged internal waveguide cover or cavity", "likelihood": "Low/Medium"},
            ],
            [
                "Stop the microwave immediately.",
                "Remove any metal or unsuitable container after it is safe to do so.",
                "Clean accessible food residue after the appliance is unplugged.",
                "Do not use the microwave if sparking continues."
            ],
            "₹300 – ₹4,000+",
            "Stop using the microwave if sparking continues and arrange professional inspection."
        ),

        "unusual_noise": rule(
            [
                {"cause": "Turntable or roller problem", "likelihood": "Medium"},
                {"cause": "Loose or unsuitable container", "likelihood": "Medium"},
                {"cause": "Internal motor or electrical component issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the turntable is seated correctly.",
                "Remove loose objects from inside.",
                "Stop use if the noise is accompanied by sparks or burning smell.",
                "Do not open the microwave."
            ],
            "₹300 – ₹4,000"
        ),

        "turntable_not_rotating": rule(
            [
                {"cause": "Turntable not seated correctly", "likelihood": "High"},
                {"cause": "Dirty or obstructed roller ring", "likelihood": "Medium"},
                {"cause": "Turntable motor problem", "likelihood": "Medium"},
            ],
            [
                "Check that the glass tray is positioned correctly.",
                "Clean the accessible roller ring.",
                "Check whether the turntable coupling is visibly obstructed.",
                "Do not dismantle the appliance."
            ],
            "₹300 – ₹2,500"
        ),

        "door_not_closing": rule(
            [
                {"cause": "Food or object blocking the door", "likelihood": "High"},
                {"cause": "Door latch problem", "likelihood": "Medium"},
                {"cause": "Door alignment or hinge issue", "likelihood": "Medium"},
            ],
            [
                "Check for objects blocking the door.",
                "Clean the accessible door area.",
                "Do not force the door.",
                "Do not operate the microwave if the door does not close securely."
            ],
            "₹300 – ₹3,000"
        ),

        "buttons_not_working": rule(
            [
                {"cause": "Control panel lock enabled", "likelihood": "Medium"},
                {"cause": "Dirty or damaged buttons", "likelihood": "Medium"},
                {"cause": "Control panel fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check whether the child/control lock is enabled.",
                "Follow the manual's unlock procedure.",
                "Clean the accessible control panel.",
                "Do not open the control panel."
            ],
            "₹300 – ₹3,000"
        ),

        "burning_smell": rule(
            [
                {"cause": "Food or grease residue", "likelihood": "Medium"},
                {"cause": "Overheated food or container", "likelihood": "Medium"},
                {"cause": "Electrical component overheating", "likelihood": "Low/Medium"},
            ],
            [
                "Stop using the microwave.",
                "If safe, unplug it.",
                "Check for burned food residue after the appliance has cooled.",
                "Do not use it again if the smell appears electrical or continues."
            ],
            "₹300 – ₹5,000+",
            "A persistent burning or electrical smell requires professional inspection."
        ),
    },


    # ========================================================
    # FAN
    # ========================================================

    "fan": {

        "not_turning_on": rule(
            [
                {"cause": "Power supply problem", "likelihood": "High"},
                {"cause": "Switch or remote problem", "likelihood": "Medium"},
                {"cause": "Motor or capacitor issue", "likelihood": "Medium"},
                {"cause": "Internal electrical fault", "likelihood": "Low"},
            ],
            [
                "Check the power supply.",
                "Check the wall switch.",
                "If it has a remote, check the batteries.",
                "Do not open the motor housing."
            ],
            "₹200 – ₹2,500"
        ),

        "running_slowly": rule(
            [
                {"cause": "Low power or regulator setting", "likelihood": "Medium"},
                {"cause": "Dust buildup", "likelihood": "Medium"},
                {"cause": "Capacitor problem", "likelihood": "Medium"},
                {"cause": "Motor problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check the speed setting.",
                "Clean accessible dust from the fan.",
                "Check whether the fan starts slowly or remains slow.",
                "Electrical component replacement should be done by a qualified technician."
            ],
            "₹300 – ₹2,000"
        ),

        "making_noise": rule(
            [
                {"cause": "Loose screws or housing", "likelihood": "Medium"},
                {"cause": "Dust or obstruction", "likelihood": "Medium"},
                {"cause": "Bearing or motor problem", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off the fan before inspecting it.",
                "Check for visible loose parts.",
                "Clean accessible dust after disconnecting power.",
                "Do not open the motor assembly."
            ],
            "₹300 – ₹2,500"
        ),

        "not_changing_speed": rule(
            [
                {"cause": "Remote or regulator setting issue", "likelihood": "Medium"},
                {"cause": "Regulator/control fault", "likelihood": "Medium"},
                {"cause": "Capacitor or motor issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check the selected speed.",
                "If using a remote, replace its batteries.",
                "Try the manual controls if available.",
                "Do not open electrical controls."
            ],
            "₹300 – ₹2,000"
        ),

        "oscillation_not_working": rule(
            [
                {"cause": "Oscillation control not engaged", "likelihood": "High"},
                {"cause": "Mechanical linkage problem", "likelihood": "Medium"},
                {"cause": "Oscillation motor/gear problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check that the oscillation function is enabled.",
                "Switch off the fan before checking for visible obstruction.",
                "Do not force the oscillating mechanism."
            ],
            "₹300 – ₹2,000"
        ),

        "remote_not_working": rule(
            [
                {"cause": "Dead batteries", "likelihood": "High"},
                {"cause": "Remote control fault", "likelihood": "Medium"},
                {"cause": "Receiver problem", "likelihood": "Low/Medium"},
            ],
            [
                "Replace the batteries.",
                "Point the remote directly toward the fan receiver.",
                "Check whether manual controls work.",
                "Keep the receiver area unobstructed."
            ],
            "₹150 – ₹1,500"
        ),

        "overheating": rule(
            [
                {"cause": "Motor working under excessive load", "likelihood": "Medium"},
                {"cause": "Dust buildup", "likelihood": "Medium"},
                {"cause": "Motor or electrical component problem", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off the fan and allow it to cool.",
                "Check for visible dust buildup after power is disconnected.",
                "Do not continue operating if there is burning smell or smoke.",
                "Arrange professional inspection if overheating returns."
            ],
            "₹300 – ₹3,000+",
            "Stop using the fan if it becomes excessively hot or produces a burning smell."
        ),
    },


    # ========================================================
    # OVEN
    # ========================================================

    "oven": {

        "not_heating": rule(
            [
                {"cause": "Incorrect cooking mode or temperature", "likelihood": "Medium"},
                {"cause": "Power supply issue", "likelihood": "Medium"},
                {"cause": "Heating element problem", "likelihood": "Medium"},
                {"cause": "Control or thermostat fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the selected cooking mode.",
                "Check the temperature setting.",
                "Make sure the oven receives power.",
                "Do not touch or replace heating components while powered."
            ],
            "₹500 – ₹5,000+"
        ),

        "heating_unevenly": rule(
            [
                {"cause": "Incorrect rack position", "likelihood": "Medium"},
                {"cause": "Overcrowding the oven", "likelihood": "Medium"},
                {"cause": "Dirty or obstructed heating area", "likelihood": "Medium"},
                {"cause": "Heating element or fan problem", "likelihood": "Low/Medium"},
            ],
            [
                "Use the recommended rack position.",
                "Avoid overcrowding the oven.",
                "Check that air circulation is not blocked.",
                "Arrange professional inspection if heating remains uneven."
            ],
            "₹300 – ₹5,000"
        ),

        "not_turning_on": rule(
            [
                {"cause": "Power supply issue", "likelihood": "High"},
                {"cause": "Control or timer setting", "likelihood": "Medium"},
                {"cause": "Internal electrical fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power supply.",
                "Check whether the timer or control lock is active.",
                "Check the display for error messages.",
                "Do not open electrical components."
            ],
            "₹300 – ₹5,000"
        ),

        "temperature_incorrect": rule(
            [
                {"cause": "Incorrect temperature setting", "likelihood": "Medium"},
                {"cause": "Thermostat/sensor issue", "likelihood": "Medium"},
                {"cause": "Heating system problem", "likelihood": "Low/Medium"},
            ],
            [
                "Confirm the selected temperature.",
                "Avoid opening the door repeatedly while cooking.",
                "Compare behavior with the manufacturer's guidance.",
                "Arrange professional inspection if temperature remains incorrect."
            ],
            "₹500 – ₹4,000"
        ),

        "making_unusual_noise": rule(
            [
                {"cause": "Cooling or circulation fan noise", "likelihood": "Medium"},
                {"cause": "Loose rack or tray", "likelihood": "Medium"},
                {"cause": "Fan motor or internal component issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check that racks and trays are positioned correctly.",
                "Determine whether the sound occurs during heating or cooling.",
                "Do not open the oven while hot.",
                "Arrange professional inspection for persistent abnormal noise."
            ],
            "₹300 – ₹4,000"
        ),

        "door_not_closing": rule(
            [
                {"cause": "Obstruction around the door", "likelihood": "High"},
                {"cause": "Damaged door seal", "likelihood": "Medium"},
                {"cause": "Hinge or alignment problem", "likelihood": "Medium"},
            ],
            [
                "Check for objects blocking the door.",
                "Inspect the accessible seal for visible damage.",
                "Do not force the door.",
                "Avoid using the oven if the door cannot close safely."
            ],
            "₹300 – ₹4,000"
        ),

        "burning_smell": rule(
            [
                {"cause": "Food residue or grease", "likelihood": "Medium"},
                {"cause": "Burned food or unsuitable material", "likelihood": "Medium"},
                {"cause": "Electrical component overheating", "likelihood": "Low"},
            ],
            [
                "Stop using the oven if the smell is unusual or strong.",
                "Allow the oven to cool before cleaning.",
                "Remove accessible food residue.",
                "If there is smoke or electrical smell, switch off power if safe and seek professional help."
            ],
            "₹300 – ₹5,000+"
        ),

        "timer_not_working": rule(
            [
                {"cause": "Incorrect timer setting", "likelihood": "Medium"},
                {"cause": "Control panel issue", "likelihood": "Medium"},
                {"cause": "Electronic control fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the timer settings in the manual.",
                "Check whether control lock is enabled.",
                "Restart the oven according to manufacturer instructions.",
                "Do not open the control panel."
            ],
            "₹300 – ₹3,000"
        ),
    },


    # ========================================================
    # DISHWASHER
    # ========================================================

    "dishwasher": {

        "not_starting": rule(
            [
                {"cause": "Power supply issue", "likelihood": "High"},
                {"cause": "Door not properly closed", "likelihood": "High"},
                {"cause": "Control panel or cycle setting issue", "likelihood": "Medium"},
                {"cause": "Electronic fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power connection.",
                "Make sure the door is fully closed.",
                "Check for an error code.",
                "Do not open electrical components."
            ],
            "₹300 – ₹3,500"
        ),

        "not_filling_water": rule(
            [
                {"cause": "Water supply turned off", "likelihood": "High"},
                {"cause": "Inlet hose blockage", "likelihood": "Medium"},
                {"cause": "Water inlet valve problem", "likelihood": "Medium"},
                {"cause": "Control system issue", "likelihood": "Low"},
            ],
            [
                "Check that the water supply is turned on.",
                "Check the inlet hose for visible kinks.",
                "Check for an error code.",
                "Do not dismantle the water inlet system."
            ],
            "₹300 – ₹3,500"
        ),

        "not_draining": rule(
            [
                {"cause": "Clogged filter", "likelihood": "High"},
                {"cause": "Blocked drain hose", "likelihood": "Medium"},
                {"cause": "Drain pump problem", "likelihood": "Medium"},
            ],
            [
                "Check the filter according to the manufacturer's instructions.",
                "Check the drain hose for visible kinks.",
                "Remove standing water carefully if the manual permits.",
                "Do not open electrical components."
            ],
            "₹500 – ₹3,500"
        ),

        "dishes_not_clean": rule(
            [
                {"cause": "Blocked spray arms", "likelihood": "High"},
                {"cause": "Overloading", "likelihood": "High"},
                {"cause": "Incorrect detergent", "likelihood": "Medium"},
                {"cause": "Low water temperature or circulation problem", "likelihood": "Medium"},
            ],
            [
                "Avoid overcrowding dishes.",
                "Check that spray arms can rotate freely.",
                "Clean accessible filters.",
                "Use the recommended dishwasher detergent."
            ],
            "₹200 – ₹3,000"
        ),

        "water_leaking": rule(
            [
                {"cause": "Door seal problem", "likelihood": "Medium"},
                {"cause": "Loose hose connection", "likelihood": "Medium"},
                {"cause": "Overloading or incorrect detergent", "likelihood": "Medium"},
                {"cause": "Internal leak", "likelihood": "Low/Medium"},
            ],
            [
                "Stop the dishwasher if leaking is significant.",
                "Check the door seal for visible damage.",
                "Check accessible hose connections.",
                "Keep water away from electrical connections."
            ],
            "₹300 – ₹4,000"
        ),

        "making_noise": rule(
            [
                {"cause": "Dish or utensil contacting spray arm", "likelihood": "High"},
                {"cause": "Foreign object in pump area", "likelihood": "Medium"},
                {"cause": "Pump or motor issue", "likelihood": "Low/Medium"},
            ],
            [
                "Check that dishes are loaded securely.",
                "Make sure spray arms can rotate.",
                "Check accessible filters according to the manual.",
                "Arrange professional service for persistent grinding or mechanical noise."
            ],
            "₹300 – ₹5,000"
        ),

        "dishes_not_drying": rule(
            [
                {"cause": "Drying setting not selected", "likelihood": "Medium"},
                {"cause": "Rinse-aid issue", "likelihood": "Medium"},
                {"cause": "Incorrect loading", "likelihood": "Medium"},
                {"cause": "Heating/drying system fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the drying setting.",
                "Use rinse aid if recommended by the manufacturer.",
                "Avoid nesting cups and containers.",
                "Arrange service if drying remains poor."
            ],
            "₹300 – ₹4,000"
        ),

        "bad_smell": rule(
            [
                {"cause": "Food residue in filter", "likelihood": "High"},
                {"cause": "Standing water", "likelihood": "Medium"},
                {"cause": "Dirty interior or seals", "likelihood": "Medium"},
                {"cause": "Drainage problem", "likelihood": "Medium"},
            ],
            [
                "Clean accessible filters.",
                "Remove food residue.",
                "Wipe accessible door seals.",
                "Check whether water remains after a cycle."
            ],
            "₹200 – ₹2,000"
        ),
    },


    # ========================================================
    # WATER HEATER
    # ========================================================

    "water heater": {

        "no_hot_water": rule(
            [
                {"cause": "Power supply issue", "likelihood": "High"},
                {"cause": "Temperature setting issue", "likelihood": "Medium"},
                {"cause": "Heating element problem", "likelihood": "Medium"},
                {"cause": "Thermostat/control fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power indicator if available.",
                "Check the temperature setting.",
                "Check whether the power supply is switched on.",
                "Do not open the heater or electrical connections."
            ],
            "₹500 – ₹5,000+"
        ),

        "not_heating_enough": rule(
            [
                {"cause": "Temperature setting too low", "likelihood": "Medium"},
                {"cause": "Heavy hot-water usage", "likelihood": "Medium"},
                {"cause": "Heating element scaling or fault", "likelihood": "Medium"},
                {"cause": "Thermostat problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check the temperature setting.",
                "Allow sufficient heating time.",
                "Check whether the issue occurs consistently.",
                "Arrange professional service if heating remains inadequate."
            ],
            "₹500 – ₹5,000+"
        ),

        "overheating": rule(
            [
                {"cause": "Thermostat setting or fault", "likelihood": "Medium"},
                {"cause": "Temperature control problem", "likelihood": "Medium"},
                {"cause": "Heating system fault", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off the heater if water becomes dangerously hot.",
                "Do not continue using it if overheating occurs.",
                "Do not open the heater.",
                "Contact a qualified technician."
            ],
            "₹500 – ₹5,000+",
            "Stop using the water heater if it overheats and arrange professional inspection."
        ),

        "water_leaking": rule(
            [
                {"cause": "Pipe or connection leak", "likelihood": "Medium"},
                {"cause": "Pressure-related issue", "likelihood": "Medium"},
                {"cause": "Tank or internal component problem", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off the heater if water is reaching electrical areas.",
                "Turn off the water supply if safe and appropriate.",
                "Do not open the tank.",
                "Arrange professional service for persistent leakage."
            ],
            "₹500 – ₹8,000+",
            "Water and electricity can create a serious safety risk. Professional inspection is recommended."
        ),

        "making_noise": rule(
            [
                {"cause": "Mineral scale buildup", "likelihood": "High"},
                {"cause": "Water pressure or heating-related noise", "likelihood": "Medium"},
                {"cause": "Internal component issue", "likelihood": "Low/Medium"},
            ],
            [
                "Observe whether the noise occurs during heating.",
                "Check for any visible leakage.",
                "Do not open the tank or electrical components.",
                "Arrange professional servicing if noise persists."
            ],
            "₹500 – ₹5,000"
        ),

        "not_turning_on": rule(
            [
                {"cause": "Power supply issue", "likelihood": "High"},
                {"cause": "Switch or breaker issue", "likelihood": "Medium"},
                {"cause": "Thermostat or control fault", "likelihood": "Medium"},
                {"cause": "Internal electrical fault", "likelihood": "Low"},
            ],
            [
                "Check whether power is supplied to the heater.",
                "Check the external switch or indicator.",
                "Do not repeatedly reset a tripping safety device.",
                "Do not open electrical components."
            ],
            "₹300 – ₹5,000"
        ),

        "power_indicator_not_working": rule(
            [
                {"cause": "Indicator lamp/LED failure", "likelihood": "High"},
                {"cause": "Power supply issue", "likelihood": "Medium"},
                {"cause": "Control circuit problem", "likelihood": "Low/Medium"},
            ],
            [
                "Check whether the heater is otherwise producing hot water.",
                "Check the external power switch.",
                "Do not open the electrical panel.",
                "Arrange service if the heater also fails to heat."
            ],
            "₹200 – ₹2,500"
        ),
    },


    # ========================================================
    # VACUUM CLEANER
    # ========================================================

    "vacuum cleaner": {

        "not_turning_on": rule(
            [
                {"cause": "Power supply or plug issue", "likelihood": "High"},
                {"cause": "Battery depleted on cordless model", "likelihood": "High"},
                {"cause": "Overheating protection activated", "likelihood": "Medium"},
                {"cause": "Motor or electrical fault", "likelihood": "Low/Medium"},
            ],
            [
                "Check the power connection.",
                "For cordless models, charge the battery.",
                "Allow the vacuum to cool if it recently overheated.",
                "Do not open the motor or electrical housing."
            ],
            "₹300 – ₹4,000"
        ),

        "weak_suction": rule(
            [
                {"cause": "Full dust container or bag", "likelihood": "High"},
                {"cause": "Blocked hose or filter", "likelihood": "High"},
                {"cause": "Brush blockage", "likelihood": "Medium"},
                {"cause": "Motor or suction-system fault", "likelihood": "Low/Medium"},
            ],
            [
                "Empty the dust container or replace the bag.",
                "Clean accessible filters according to the manual.",
                "Check the hose for visible blockage.",
                "Remove hair or debris from the brush if safely accessible."
            ],
            "₹200 – ₹3,000"
        ),

        "making_unusual_noise": rule(
            [
                {"cause": "Object stuck in the brush or hose", "likelihood": "Medium"},
                {"cause": "Loose component", "likelihood": "Medium"},
                {"cause": "Motor or bearing problem", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off and unplug the vacuum.",
                "Check the accessible brush and hose.",
                "Remove visible debris safely.",
                "Do not open the motor."
            ],
            "₹300 – ₹4,000"
        ),

        "overheating": rule(
            [
                {"cause": "Blocked filter", "likelihood": "High"},
                {"cause": "Full dust container or bag", "likelihood": "High"},
                {"cause": "Blocked hose or brush", "likelihood": "Medium"},
                {"cause": "Motor problem", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off the vacuum and allow it to cool.",
                "Empty the dust container or replace the bag.",
                "Clean accessible filters.",
                "Check the hose and brush for blockage."
            ],
            "₹200 – ₹4,000",
            "Stop using the vacuum if overheating returns after cleaning and arrange professional inspection."
        ),

        "brush_not_rotating": rule(
            [
                {"cause": "Hair or debris wrapped around brush", "likelihood": "High"},
                {"cause": "Brush blockage", "likelihood": "Medium"},
                {"cause": "Brush motor or belt problem", "likelihood": "Low/Medium"},
            ],
            [
                "Switch off and disconnect the vacuum.",
                "Remove visible hair and debris from the brush.",
                "Check the brush according to the manufacturer's instructions.",
                "Do not dismantle the motorized brush unless the manual specifically permits it."
            ],
            "₹300 – ₹3,000"
        ),

        "dust_escaping": rule(
            [
                {"cause": "Dust container or bag not fitted correctly", "likelihood": "High"},
                {"cause": "Damaged filter", "likelihood": "Medium"},
                {"cause": "Full dust container", "likelihood": "Medium"},
                {"cause": "Seal problem", "likelihood": "Low/Medium"},
            ],
            [
                "Empty the dust container.",
                "Check that the bag/container is installed correctly.",
                "Clean or replace filters according to the manual.",
                "Check accessible seals for visible damage."
            ],
            "₹200 – ₹2,500"
        ),

        "battery_not_charging": rule(
            [
                {"cause": "Charger or power outlet problem", "likelihood": "Medium"},
                {"cause": "Charging contacts dirty", "likelihood": "Medium"},
                {"cause": "Battery degradation", "likelihood": "Medium"},
                {"cause": "Charging circuit fault", "likelihood": "Low"},
            ],
            [
                "Check the charger and power outlet.",
                "Clean accessible charging contacts.",
                "Make sure the charger is the correct one for the vacuum.",
                "Do not open or repair the battery pack."
            ],
            "₹500 – ₹5,000+"
        ),
    },
}


# ============================================================
# WORDING / ALIASES
# ============================================================
#
# This lets customers use normal language instead of having
# to type the exact problem name.
# ============================================================

ALIASES = {

    "not_cooling": [
        "not cooling",
        "isn't cooling",
        "isnt cooling",
        "doesn't cool",
        "doesnt cool",
        "not getting cold",
        "not cold",
        "fridge is warm",
        "refrigerator is warm",
        "no cooling",
    ],

    "cooling_weak": [
        "cooling is weak",
        "weak cooling",
        "cooling weak",
        "not cooling properly",
        "cooling is less",
        "cooling is low",
        "cooling poorly",
    ],

    "too_much_ice_frost": [
        "too much ice",
        "too much frost",
        "ice buildup",
        "ice build up",
        "frost buildup",
        "frost build up",
        "excess ice",
        "freezing too much",
    ],

    "water_leaking": [
        "water leaking",
        "water leak",
        "leaking water",
        "water is leaking",
        "leaks water",
    ],

    "unusual_noise": [
        "unusual noise",
        "strange noise",
        "weird noise",
        "making noise",
        "making a noise",
        "loud noise",
        "noisy",
    ],

    "not_turning_on": [
        "not turning on",
        "doesn't turn on",
        "doesnt turn on",
        "won't turn on",
        "wont turn on",
        "not switching on",
        "doesn't switch on",
        "doesnt switch on",
        "no power",
        "not powering on",
        "dead",
    ],

    "compressor_not_working": [
        "compressor not working",
        "compressor isn't working",
        "compressor is not working",
        "compressor stopped",
        "compressor not running",
    ],

    "door_not_sealing": [
        "door not sealing",
        "door seal problem",
        "door seal",
        "door gasket",
        "door not closing properly",
        "door doesn't seal",
        "door doesnt seal",
    ],

    "bad_smell": [
        "bad smell",
        "bad odour",
        "bad odor",
        "smells bad",
        "strange smell",
        "foul smell",
        "smelly",
    ],

    "light_not_working": [
        "light not working",
        "light doesn't work",
        "light doesnt work",
        "bulb not working",
        "inside light not working",
    ],

    "not_starting": [
        "not starting",
        "won't start",
        "wont start",
        "doesn't start",
        "doesnt start",
        "not start",
        "machine won't start",
        "machine wont start",
        "washer won't start",
        "washer wont start",
    ],

    "not_spinning": [
        "not spinning",
        "won't spin",
        "wont spin",
        "doesn't spin",
        "doesnt spin",
        "not rotating",
        "drum not spinning",
    ],

    "not_draining_water": [
        "not draining water",
        "not draining",
        "water not draining",
        "won't drain",
        "wont drain",
        "doesn't drain",
        "doesnt drain",
        "water stays inside",
    ],

    "not_filling_water": [
        "not filling water",
        "not filling",
        "water not filling",
        "doesn't fill",
        "doesnt fill",
        "won't fill",
        "wont fill",
        "not taking water",
        "not getting water",
    ],

    "excessive_vibration": [
        "excessive vibration",
        "vibrating too much",
        "too much vibration",
        "shaking",
        "machine shaking",
        "moving around",
        "jumping",
    ],

    "making_loud_noise": [
        "making loud noise",
        "loud noise",
        "very noisy",
        "very loud",
        "strange loud noise",
        "grinding noise",
        "banging noise",
    ],

    "clothes_not_cleaned": [
        "clothes not cleaned",
        "clothes not clean",
        "not cleaning clothes",
        "clothes still dirty",
        "washing not cleaning",
        "not washing properly",
    ],

    "door_not_opening": [
        "door not opening",
        "door won't open",
        "door wont open",
        "door doesn't open",
        "door doesnt open",
        "washing machine door stuck",
        "washer door stuck",
    ],

    "error_code": [
        "error code",
        "error",
        "error message",
        "error showing",
        "displaying error",
        "code showing",
    ],

    "blowing_warm_air": [
        "blowing warm air",
        "blowing hot air",
        "warm air",
        "hot air",
        "air is warm",
        "air is hot",
    ],

    "remote_not_working": [
        "remote not working",
        "remote doesn't work",
        "remote doesnt work",
        "remote won't work",
        "remote wont work",
        "remote not responding",
    ],

    "ice_forming": [
        "ice forming",
        "ice forming on ac",
        "ac has ice",
        "ice on ac",
        "ice buildup on ac",
        "coil freezing",
        "ac freezing",
    ],

    "high_electricity_consumption": [
        "high electricity consumption",
        "electricity bill high",
        "power consumption high",
        "using too much electricity",
        "electricity usage high",
        "bill increased",
        "high power consumption",
    ],

    "no_picture": [
        "no picture",
        "no display",
        "screen blank",
        "black screen",
        "picture not showing",
        "display not working",
    ],

    "no_sound": [
        "no sound",
        "no audio",
        "sound not working",
        "audio not working",
        "no voice",
    ],

    "screen_flickering": [
        "screen flickering",
        "screen flickers",
        "display flickering",
        "flickering screen",
        "screen blinking",
    ],

    "lines_on_screen": [
        "lines on screen",
        "lines on display",
        "vertical lines",
        "horizontal lines",
        "screen has lines",
    ],

    "hdmi_not_working": [
        "hdmi not working",
        "hdmi doesn't work",
        "hdmi doesnt work",
        "hdmi no signal",
        "hdmi not detecting",
    ],

    "wifi_not_connecting": [
        "wifi not connecting",
        "wi-fi not connecting",
        "wifi doesn't connect",
        "wifi doesnt connect",
        "tv wifi not working",
        "tv won't connect to wifi",
        "tv wont connect to wifi",
    ],

    "apps_not_opening": [
        "apps not opening",
        "app not opening",
        "apps don't open",
        "apps dont open",
        "netflix not opening",
        "youtube not opening",
        "apps not working",
    ],

    "restarting_automatically": [
        "restarting automatically",
        "tv keeps restarting",
        "tv restarts",
        "keeps restarting",
        "turns off and on",
        "restarts by itself",
    ],

    "not_heating": [
        "not heating",
        "not getting hot",
        "not hot",
        "doesn't heat",
        "doesnt heat",
        "not heating properly",
    ],

    "sparking_inside": [
        "sparking inside",
        "sparks inside",
        "microwave sparking",
        "sparking",
        "sparks",
    ],

    "turntable_not_rotating": [
        "turntable not rotating",
        "turntable not turning",
        "plate not rotating",
        "plate not turning",
        "microwave plate not moving",
    ],

    "door_not_closing": [
        "door not closing",
        "door won't close",
        "door wont close",
        "door doesn't close",
        "door doesnt close",
    ],

    "buttons_not_working": [
        "buttons not working",
        "buttons don't work",
        "buttons dont work",
        "keypad not working",
        "button not responding",
    ],

    "burning_smell": [
        "burning smell",
        "burnt smell",
        "smell of burning",
        "electrical smell",
        "burning odor",
        "burning odour",
    ],

    "running_slowly": [
        "running slowly",
        "running slow",
        "fan is slow",
        "fan speed low",
        "fan rotating slowly",
    ],

    "making_noise": [
        "making noise",
        "fan making noise",
        "strange fan noise",
        "fan noisy",
        "fan sounds strange",
    ],

    "not_changing_speed": [
        "not changing speed",
        "speed not changing",
        "fan speed not changing",
        "cannot change speed",
        "can't change speed",
    ],

    "oscillation_not_working": [
        "oscillation not working",
        "oscillation doesn't work",
        "oscillation doesnt work",
        "fan not oscillating",
        "fan not moving side to side",
    ],

    "overheating": [
        "overheating",
        "overheats",
        "getting too hot",
        "becoming hot",
        "fan gets hot",
        "vacuum gets hot",
    ],

    "heating_unevenly": [
        "heating unevenly",
        "uneven heating",
        "not heating evenly",
        "food heating unevenly",
    ],

    "temperature_incorrect": [
        "temperature incorrect",
        "temperature wrong",
        "temperature not correct",
        "oven temperature wrong",
        "oven too hot",
        "oven not hot enough",
    ],

    "timer_not_working": [
        "timer not working",
        "timer doesn't work",
        "timer doesnt work",
        "oven timer not working",
    ],

    "dishes_not_clean": [
        "dishes not clean",
        "dishes not cleaned",
        "not cleaning dishes",
        "plates not clean",
        "dishwasher not cleaning",
    ],

    "dishes_not_drying": [
        "dishes not drying",
        "dishes are wet",
        "not drying dishes",
        "dishwasher not drying",
    ],

    "no_hot_water": [
        "no hot water",
        "no hot water coming",
        "water is cold",
        "heater not giving hot water",
        "no warm water",
    ],

    "not_heating_enough": [
        "not heating enough",
        "water not hot enough",
        "hot water not hot enough",
        "heating is weak",
        "water only warm",
    ],

    "power_indicator_not_working": [
        "power indicator not working",
        "indicator light not working",
        "power light not working",
        "indicator not working",
    ],

    "weak_suction": [
        "weak suction",
        "low suction",
        "suction is weak",
        "not sucking properly",
        "vacuum not sucking",
        "poor suction",
    ],

    "brush_not_rotating": [
        "brush not rotating",
        "brush not turning",
        "brush stopped",
        "roller not rotating",
        "roller not turning",
    ],

    "dust_escaping": [
        "dust escaping",
        "dust coming out",
        "dust blowing out",
        "dust leaking",
        "vacuum releasing dust",
    ],

    "battery_not_charging": [
        "battery not charging",
        "battery won't charge",
        "battery wont charge",
        "vacuum not charging",
        "charger not charging",
    ],
}


# ============================================================
# CATEGORY NORMALIZATION
# ============================================================

CATEGORY_ALIASES = {

    "fridge": "refrigerator",
    "refrigerator": "refrigerator",
    "refrigerators": "refrigerator",

    "washer": "washing machine",
    "washing machine": "washing machine",
    "washing machines": "washing machine",
    "washingmachine": "washing machine",

    "air conditioner": "ac",
    "air conditioning": "ac",
    "a/c": "ac",
    "ac": "ac",

    "television": "tv",
    "smart tv": "tv",
    "tv": "tv",

    "microwave oven": "microwave",
    "microwave": "microwave",

    "fan": "fan",
    "ceiling fan": "fan",
    "table fan": "fan",

    "oven": "oven",
    "electric oven": "oven",

    "dish washer": "dishwasher",
    "dishwasher": "dishwasher",

    "water heater": "water heater",
    "water heater machine": "water heater",
    "geyser": "water heater",
    "heater": "water heater",

    "vacuum": "vacuum cleaner",
    "vacuum cleaner": "vacuum cleaner",
    "vacuumcleaner": "vacuum cleaner",
}


# ============================================================
# FIND MATCH
# ============================================================

def find_problem(category_key: str, symptom_key: str):

    category_rules = RULES.get(category_key, {})

    # --------------------------------------------------------
    # First: check aliases
    # --------------------------------------------------------

    matches = []

    for problem_key in category_rules.keys():

        aliases = ALIASES.get(problem_key, [])

        for phrase in aliases:

            if phrase in symptom_key:
                matches.append(
                    (len(phrase), problem_key)
                )

    # Prefer the longest matching phrase.
    # This helps avoid short words matching the wrong problem.
    if matches:

        matches.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return category_rules[matches[0][1]]

    # --------------------------------------------------------
    # Second: direct keyword matching
    # --------------------------------------------------------

    for problem_key, data in category_rules.items():

        readable = problem_key.replace("_", " ")

        if readable in symptom_key:
            return data

    return None


# ============================================================
# MAIN DIAGNOSIS FUNCTION
# ============================================================

def diagnose(category: str, symptom: str):

    category_original = category or ""
    symptom_original = symptom or ""

    category_key = (
        category_original
        .strip()
        .lower()
    )

    symptom_key = (
        symptom_original
        .strip()
        .lower()
    )

    # Normalize category
    category_key = CATEGORY_ALIASES.get(
        category_key,
        category_key
    )

    # --------------------------------------------------------
    # Find matching problem
    # --------------------------------------------------------

    selected = find_problem(
        category_key,
        symptom_key
    )

    # --------------------------------------------------------
    # UNKNOWN PROBLEM
    # --------------------------------------------------------

    if not selected:

        return {
            "category": category_original,
            "symptom": symptom_original,

            "possible_causes": [
                {
                    "cause": "The exact cause could not be determined from the information provided.",
                    "likelihood": "Unknown"
                }
            ],

            "safe_checks": [
                "Check the appliance display for an error code.",
                "Check the power supply and basic settings if safe to do so.",
                "Check the user manual for the exact symptom.",
                "Avoid opening electrical, sealed, gas, refrigerant, or high-voltage components.",
                "Contact a qualified technician if the problem continues."
            ],

            "estimated_repair_range": "Inspection required",

            "recommendation": (
                "Please provide more details about the symptom, "
                "or arrange professional inspection if the appliance "
                "is unsafe or the problem continues."
            )
        }

    # --------------------------------------------------------
    # KNOWN PROBLEM
    # --------------------------------------------------------

    return {
        "category": category_original,
        "symptom": symptom_original,

        "possible_causes": selected["causes"],

        "safe_checks": selected["checks"],

        "estimated_repair_range": selected["range"],

        "recommendation": selected["recommendation"]
    }