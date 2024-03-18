# Real-Time Object Detection with Voice Notification

## Table of Contents
- [Real-Time Object Detection with Voice Notification](#real-time-object-detection-with-voice-notification)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Technologies Used](#technologies-used)
  - [System Overview](#system-overview)
  - [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Running the Detection](#running-the-detection)
    - [Voice Notification](#voice-notification)
  - [Metrics and Tools](#metrics-and-tools)
  - [Benchmark Results](#benchmark-results)
  - [Project Milestones Schedule](#project-milestones-schedule)
  - [Challenges and Solutions](#challenges-and-solutions)
  - [Future Work](#future-work)
  - [Contributors](#contributors)

---

## Introduction
This project aims to develop a real-time object detection system on smartphones that provides voice notifications for detected objects. This is particularly designed to assist visually impaired users by informing them about their surroundings.

---

## Technologies Used
- **YOLOv8n:** For real-time object detection.
- **Google Text-to-Speech (gTTS):** For generating voice notifications.
- **Python:** Primary programming language.
- **Android/iOS:** Target platforms for the application.
- **C++:** Utilized for working with C++ files and components within the project.

---

## System Overview
- TODO
<!-- The system captures live video from the smartphone's camera, identifies objects in real-time using the YOLOv8n model, and communicates detected objects and their positions via voice notifications. -->

---

## Setup Instructions

### Prerequisites
- TODO
<!-- - Python 3.8 or higher
- Access to a smartphone camera or webcam -->

### Installation
- TODO
<!-- 1. Clone the repository: `git clone [repository URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Download and place YOLOv8n model weights in the project directory. -->

---

## Usage

### Running the Detection
- TODO

<!-- To execute the detection script, run the following command in your terminal:
`python your_script.py --image your_image_path.jpg --model your_model_path.pt`

Make sure to replace `your_script.py`, `your_image_path.jpg`, and `your_model_path.pt` with the appropriate file names and paths. -->


### Voice Notification
- TODO

<!-- Detected objects along with their confidence levels and positions are automatically converted to voice notifications and played back to the user. -->

---

## Metrics and Tools
To assess the effectiveness of our real-time object detection and voice notification system, we utilize the following tools and metrics:

- **Tools**:
  - YOLO (You Only Look Once) for object detection.
  - Google's Text-to-Speech (gTTS) for generating voice notifications.

- **Metrics**:
  - **Object Detection Performance**:
    - TODO
    <!-- - Detection Accuracy: Precision and recall rates.
    - Detection Speed: Time taken from image capture to object detection. -->
  - **Voice Notification Performance**:
    - TODO
    <!-- - Notification Speed: Time taken from object detection to voice notification delivery.
    - Notification Clarity: Understandability of voice notifications. -->

---

## Benchmark Results
- TODO
<!-- *Note: This section will be updated with the actual performance metrics and comparisons once the testing phase is completed.* -->

---

## Project Milestones Schedule
| Nr. | Milestones | Completion Date |
|-----|------------|-----------------|
| **1**   | **Theory (Literature Review)** | **TBD** |
| 1.1 | OD: Evaluation of Object Detection Software | **TBD** |
| 1.2 | OD: Define Metrics for YOLO | **TBD** |
| 1.3 | OD: Compare YOLO with Other Software | **TBD** |
| 1.4 | TTS: Evaluation of Text-to-Speech Software| **TBD** |
| 1.5 | TTS: Define Metrics for Text-to-Speech Software | **TBD** |
| **2**  | **Practical (Implementation)** | **TBD** |
| 2.1 | YOLO Installation and Runtime Metrics Measurement | **TBD** |
| 2.2 | TTS Installation and Runtime Metrics Measurement | **TBD** |
| 2.3 | Prototype Development of OD Program with Vocal Feedback (*Integration of YOLO and TTS*) | **TBD** |
| 2.4 | Measurement of Detection Rate and Response Time | **TBD** |
| **3**  | **Conclusions and Suggestions** | **TBD** |
| 3.1 | Prepare Project Documentation and Appendices | **TBD** |

*Note: Completion dates are to be determined (TBD) and will be updated as the project progresses.*

---

## Challenges and Solutions
- TODO
<!-- - **Real-Time Processing:** Optimization techniques were employed to enhance the speed of detection.
- **Voice Clarity:** Selected a voice modulation that is clear and easy to understand. -->

---

## Future Work
- TODO
<!-- - Integration with AR for enhanced spatial understanding.
- Adding support for more languages. -->

---

## Contributors
- Adel Ahmadi
- Prof. Dr. B. Rhein
<!-- - [Adel Ahmadi](your-profile-link)
- [Prof. Dr. B. Rhein](profile-link) -->

For more information or to contribute to the project, please visit our [GitHub repository](https://github.com/AdelAhmadi-GH/realtime_objdetect_with_voicenotify).