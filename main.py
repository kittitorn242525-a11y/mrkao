alarm = 0
moisture = 0

def on_button_pressed_a():
    global alarm
    alarm = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global moisture
    basic.show_number(IdeaKitSmartFarm.query_data(DigitalPin.P8))
    moisture = pins.analog_read_pin(AnalogReadWritePin.P2)
    if moisture >= 350:
        basic.show_string("0ff")
        IdeaKitSmartFarm.motor_run(IdeaKitSmartFarm.Motors.M2A, 0)
    if moisture <= 100:
        basic.show_string("On")
        IdeaKitSmartFarm.motor_run(IdeaKitSmartFarm.Motors.M2A, 10)
basic.forever(on_forever)

def on_forever2():
    global alarm
    if IdeaKitSmartFarm.sonar_distance_loop(DigitalPin.P14, DigitalPin.P15, 5):
        alarm = 1
    basic.pause(alarm)
    if alarm == 1:
        music.ring_tone(262)
        basic.pause(200)
        music.stop_all_sounds()
        basic.pause(200)
    else:
        music.stop_all_sounds()
basic.forever(on_forever2)
