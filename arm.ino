#include <AccelStepper.h>

// Define stepper motor connections and motor interface type
#define BASE_STEP_PIN 2
#define BASE_DIR_PIN 5
#define SHOULDER_STEP_PIN 3
#define SHOULDER_DIR_PIN 6
#define ELBOW_STEP_PIN 4
#define ELBOW_DIR_PIN 7
#define WRIST_STEP_PIN 8
#define WRIST_DIR_PIN 11
#define PEN_STEP_PIN 9
#define PEN_DIR_PIN 12

AccelStepper baseMotor(AccelStepper::DRIVER, BASE_STEP_PIN, BASE_DIR_PIN);
AccelStepper shoulderMotor(AccelStepper::DRIVER, SHOULDER_STEP_PIN, SHOULDER_DIR_PIN);
AccelStepper elbowMotor(AccelStepper::DRIVER, ELBOW_STEP_PIN, ELBOW_DIR_PIN);
AccelStepper wristMotor(AccelStepper::DRIVER, WRIST_STEP_PIN, WRIST_DIR_PIN);
AccelStepper penMotor(AccelStepper::DRIVER, PEN_STEP_PIN, PEN_DIR_PIN);

// Constants for motor configuration
const int stepsPerMM = 100; // Adjust based on your stepper motor and driver configuration
const float drawingSpeed = 500.0; // Speed of drawing

void setup() {
    Serial.begin(9600);
    baseMotor.setMaxSpeed(drawingSpeed);
    baseMotor.setAcceleration(1000.0);
    shoulderMotor.setMaxSpeed(drawingSpeed);
    shoulderMotor.setAcceleration(1000.0);
    elbowMotor.setMaxSpeed(drawingSpeed);
    elbowMotor.setAcceleration(1000.0);
    wristMotor.setMaxSpeed(drawingSpeed);
    wristMotor.setAcceleration(1000.0);
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

            // Example of using motors to draw
            baseMotor.moveTo(xTarget);
            shoulderMotor.moveTo(yTarget);

            // Ensure all motors move to the desired position
            while (baseMotor.distanceToGo() != 0 || shoulderMotor.distanceToGo() != 0) {
                baseMotor.run();
                shoulderMotor.run();
                elbowMotor.run();
                wristMotor.run();
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
