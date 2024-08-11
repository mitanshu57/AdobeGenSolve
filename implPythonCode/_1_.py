import os
from utils import read_csv, plot, polylines2svg
from regularization import fit_line, fit_circle
from symmetry_detection import detect_symmetry
from curve_completion import complete_curve

def handle_file(input_filepath, output_svg_filepath):
    # TSS Gensolve Round 2 Solution
    # Load data from CSV
    paths_points = read_csv(input_filepath)
    
    # Process each path of points
    for path in paths_points:
        for points in path:
            # TSS Gensolve Round 2 Solution
            # Perform line fitting
            slope, intercept = fit_line(points)
            print(f'Line equation: y = {slope}x + {intercept}')
            
            # Perform circle fitting
            center_x, center_y, radius = fit_circle(points)
            print(f'Circle parameters: center=({center_x}, {center_y}), radius={radius}')
            
            # TSS Gensolve Round 2 Solution
            # Symmetry analysis
            symmetry_result = detect_symmetry(points)
            print(f'Symmetry status: {symmetry_result}')
            
            # Curve completion task
            completed_path = complete_curve(points, occlusion_type='connected')
            print(f'Completed curve points: {completed_path}')
    
    # TSS Gensolve Round 2 Solution
    # Generate a plot of the results
    plot(paths_points)
    
    # Export the results to an SVG file
    polylines2svg(paths_points, output_svg_filepath)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'problems')
    output_dir = os.path.join(base_dir, 'problems', 'output')
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # TSS Gensolve Round 2 Solution
    # List of CSV files to be processed
    csv_files = [
        'isolated.csv',
        'frag0.csv',
        'frag1.csv',
        'frag2.csv',
        'occlusion1.csv',
        # Add more filenames as necessary
    ]
    
    # Process each CSV file and generate corresponding SVG output
    for csv_file in csv_files:
        input_filepath = os.path.join(input_dir, csv_file)
        output_svg_filepath = os.path.join(output_dir, csv_file.replace('.csv', '.svg'))
        print(f'Processing file: {csv_file}...')
        handle_file(input_filepath, output_svg_filepath)
        print(f'SVG output saved at: {output_svg_filepath}')
