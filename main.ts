let alarm = 0
let moisture = 0
input.onButtonPressed(Button.A, function () {
    alarm = 0
})
basic.forever(function () {
    basic.showNumber(IdeaKitSmartFarm.queryData(DigitalPin.P8))
    moisture = pins.analogReadPin(AnalogReadWritePin.P2)
    if (moisture >= 350) {
        basic.showString("0ff")
        IdeaKitSmartFarm.MotorRun(IdeaKitSmartFarm.Motors.M2A, 0)
    }
    if (moisture <= 100) {
        basic.showString("On")
        IdeaKitSmartFarm.MotorRun(IdeaKitSmartFarm.Motors.M2A, 255)
    }
})
basic.forever(function () {
    if (IdeaKitSmartFarm.sonarDistanceLoop(DigitalPin.P14, DigitalPin.P15, 5)) {
        alarm = 1
    }
    basic.pause(alarm)
    if (alarm == 1) {
        music.ringTone(262)
        basic.pause(200)
        music.stopAllSounds()
        basic.pause(200)
    } else {
        music.stopAllSounds()
    }
})
