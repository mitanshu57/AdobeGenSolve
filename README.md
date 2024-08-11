ShapeSense
ShapeSense is a powerful and flexible toolkit designed for the analysis and processing of 2D shapes. It includes a wide array of features such as shape detection, symmetry analysis, curve completion, and advanced shape recognition using machine learning techniques.

Overview
ShapeSense is specialized in processing 2D shapes represented as polylines, with key functionalities that include:

Shape Regularization: Accurately identifies and categorizes geometric shapes like circles, ellipses, rectangles, polygons, and star shapes.
Symmetry Detection: Capable of detecting both reflective and rotational symmetries within shapes.
Curve Completion: Efficiently fills in missing segments of shapes through interpolation methods.
Shape Recognition: Implements a deep learning model to recognize and classify shapes from images of their polylines.
Usage
1. Shape Regularization
Script: regularization.py
Functionality: This module classifies geometric shapes from a given set of points.
Usage Example:
Load your shape data, use the identify_shapes function, and retrieve the recognized shapes.
2. Symmetry Detection
Script: symmetry_detection.py
Functionality: This module detects and reports reflective and rotational symmetries in shapes.
Usage Example:
Load your shape data, invoke detect_symmetry, and receive detailed symmetry information.
3. Curve Completion
Script: curve_completion.py
Functionality: This module completes incomplete shapes by applying interpolation techniques.
Usage Example:
Load your shape data, apply complete_curve, and then visualize or save the completed shapes.
4. Shape Recognition Model Training
Script: utils.py
Functionality: Trains a deep learning model, such as ResNet-18, to recognize and classify different shapes.
Usage Example:
Point to your dataset, execute the script to start model training, and save the trained model for future use.
5. Shape Prediction from New Data
Script: _1_.py
Functionality: This script uses the trained model to predict shapes based on new input data.
Usage Example:
Load new shape data, run the script, and save the resulting predictions as images.
Running the Project
Dataset Preparation: Ensure your shape data is in CSV format, where each row corresponds to a point on the shape (with X, Y coordinates).
Script Execution: Follow the sequence of scripts mentioned above, beginning with data processing, proceeding to model training, and concluding with shape prediction.
Conclusion
ShapeSense offers a comprehensive set of tools for analyzing 2D shapes, from basic shape detection and symmetry analysis to more advanced tasks such as curve completion and shape recognition via deep learning. It’s an excellent choice for research, computer vision projects, or any task requiring detailed shape analysis.