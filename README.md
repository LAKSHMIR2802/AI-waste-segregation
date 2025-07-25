# AI-Powered Waste Segregation System

This project implements a smart waste sorting system that uses computer vision to classify trash and automatically sorts it into different bins. I built this to explore how AI can help solve real-world sustainability challenges.

## How It Works

The system has three main components:

1. **Computer Vision Model** - A fine-tuned MobileNetV2 model that classifies waste into:
   - Organic
   - Recyclable 
   - Non-recyclable

2. **Real-Time Classification** - Processes live webcam feed to identify waste items

3. **Physical Sorting Mechanism** - Uses servo motors to open the correct bin flap based on the AI's classification

## Key Features

- Custom-trained deep learning model with ~90% accuracy
- Real-time processing using webcam feed
- Physical sorting via servo-controlled flaps
- Modular design allows easy improvements
- Includes training notebooks and demo videos

## Technical Details

### Model Training
- Used MobileNetV2 pretrained on ImageNet
- Fine-tuned on custom waste dataset
- Implemented data augmentation to improve generalization
- Achieved 90% validation accuracy

### Hardware Integration
- Raspberry Pi 4 as the control unit
- Standard servo motors for flap control
- Webcam for live classification
- 3D-printed bin dividers (optional)

## Getting Started

### Requirements
- Python 3.7+
- TensorFlow/Keras
- OpenCV
- RPi.GPIO (for hardware control)

### Setup
1. Clone the repo:
```bash
git clone https://github.com/yourusername/AI-waste-sorter.git
cd AI-waste-sorter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For hardware setup:
- Connect servos to GPIO pins 17, 27, 22
- Position webcam above sorting area

## Usage

1. **Training the model**:
```bash
jupyter notebook Fine Tuning MobileNetV2.ipynb
```

2. **Running live classification**:
```bash
jupyter notebook Webcam_integration.ipynb
```

3. **Testing sorting mechanism**:
```bash
python servo_motor_control.py
```

## Demo Videos

Check out these included demos:
- `Simulation of Waste Segregator.mp4` - Full system in action
- `Demonstration of running waste classifier AI.mp4` - Close-up of the classification

## Why I Built This

I wanted to create a practical application of AI that could:
- Help reduce improper waste disposal
- Demonstrate how computer vision can solve real problems
- Provide a foundation for more advanced recycling systems

The project shows how relatively simple AI and hardware can be combined to create useful automation systems.

## Limitations

- Requires good lighting for accurate classification
- Physical mechanism needs precise calibration
- Model could benefit from more diverse training data

## Future Improvements

Some ideas I'm considering:
- Adding a compaction mechanism
- Implementing weight sensors
- Creating a mobile app interface
- Expanding to more waste categories

