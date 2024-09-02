# Robotic Drawing Arm
## Overview
This project aims to develop an AI-powered system that can generate realistic sketches from photographs and use a robotic arm to draw these sketches with a calligraphy pen. The system leverages advanced computer vision and deep learning techniques to convert digital images into line drawings, capturing essential features and details while minimizing unnecessary noise. This project combines the fields of computer vision, AI, and robotics to create a unique and innovative application for artistic and practical purposes.

## Project Workflow
The project workflow consists of several modules, each responsible for a specific stage of the process:

**Camera Module:** Captures the input image of a person's face. This image serves as the starting point for the entire sketch generation process.

**Portrait Generation Module:** Processes the captured image to enhance it and prepare it for sketch generation. This includes face detection, alignment, and any necessary pre-processing to ensure the image is suitable for the next steps.

**Sketch Generation Module:** Utilizes AI models to convert the processed image into a sketch. The model identifies key facial features such as the eyes, nose, mouth, and general face outline, creating a simplified, artistic representation.

**Drawing Motion Generation Module:** Transforms the digital sketch into a series of waypoints that the robotic arm can follow. These waypoints guide the robotic arm in replicating the sketch on a physical medium using a calligraphy pen.

**Robotic Arm and Calligraphy Pen:** Executes the drawing by following the waypoints generated in the previous step. The robotic arm precisely moves the calligraphy pen to create the final physical sketch, mirroring the AI-generated digital sketch.

## Key Features
**AI-Powered Sketch Generation:** Utilizes deep learning models like pix2pix to convert digital images into sketches, capturing essential details while removing unnecessary noise and background information.

**Real-Time Processing:** Capable of processing images and generating sketches in real time, enabling quick feedback and adjustments.

**Robotic Arm Drawing:** Uses a robotic arm to replicate digital sketches on physical media, providing a tangible output of the AI-generated art.

**Customizable Sketch Styles:** The AI model can be fine-tuned to generate different sketch styles, from simple line drawings to more detailed and shaded sketches.

## Getting Started
### Prerequisites
Project is still on going and yet to be fully released.
## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## Acknoledgements
- Hoping to implement AI

- Inspiration for this project came from various AI-powered art projects and robotic drawing machines.

- Difference in this project compared to others is that this robotic arm uses Axial Motors (2)

