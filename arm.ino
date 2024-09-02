#include <AccelStepper.h>

// Define stepper motor connections and motor interface type
#define X_AXIS_STEP_PIN 2
#define X_AXIS_DIR_PIN 5
#define Y_AXIS_STEP_PIN 3
#define Y_AXIS_DIR_PIN 6
#define PEN_STEP_PIN 9
#define PEN_DIR_PIN 12

AccelStepper xAxisMotor(AccelStepper::DRIVER, X_AXIS_STEP_PIN, X_AXIS_DIR_PIN);
AccelStepper yAxisMotor(AccelStepper::DRIVER, Y_AXIS_STEP_PIN, Y_AXIS_DIR_PIN);
AccelStepper penMotor(AccelStepper::DRIVER, PEN_STEP_PIN, PEN_DIR_PIN);

// Constants for motor configuration
const int stepsPerMM = 100; // Adjust based on your stepper motor and driver configuration
const float drawingSpeed = 500.0; // Speed of drawing

void setup() {
    Serial.begin(9600);
    xAxisMotor.setMaxSpeed(drawingSpeed);
    xAxisMotor.setAcceleration(1000.0);
    yAxisMotor.setMaxSpeed(drawingSpeed);
    yAxisMotor.setAcceleration(1000.0);
    penMotor.setMaxSpeed(drawingSpeed);
    penMotor.setAcceleration(1000.0);
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');
        char command = data.charAt(0);
        data = data.substring(1);
        int commaIndex = data.indexOf(',');

        if (command == 'M') {
            int x = data.substring(0, commaIndex).toInt();
            int y = data.substring(commaIndex + 1).toInt();

            int xTarget = x * stepsPerMM;
            int yTarget = y * stepsPerMM;

            // Move motors to the desired position
            xAxisMotor.moveTo(xTarget);
            yAxisMotor.moveTo(yTarget);

            // Ensure both motors move to the desired position
            while (xAxisMotor.distanceToGo() != 0 || yAxisMotor.distanceToGo() != 0) {
                xAxisMotor.run();
                yAxisMotor.run();
                penMotor.run();
            }
        } else if (command == 'P') {
            // Lift or lower the pen based on the command (e.g., 'P1' for pen down, 'P0' for pen up)
            int penPosition = data.toInt() == 1 ? -100 : 100; // Adjust pen up/down positions
            penMotor.moveTo(penPosition);
            while (penMotor.distanceToGo() != 0) {
                penMotor.run();
            }
        }
    }
}
