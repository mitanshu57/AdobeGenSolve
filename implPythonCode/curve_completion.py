import numpy as np
from scipy.interpolate import interp1d
from sklearn.linear_model import LinearRegression

def complete_curve(points, occlusion_type='connected'):
    # TSS Gensolve Round 2 Solution
    if occlusion_type == 'connected':
        # Use linear interpolation to reconstruct the curve
        x_coords = points[:, 0]
        y_coords = points[:, 1]
        interpolator = interp1d(x_coords, y_coords, kind='linear')
        
        # Generate new points along the curve
        interpolated_x = np.linspace(x_coords[0], x_coords[-1], num=500)
        interpolated_y = interpolator(interpolated_x)
        
        # Combine x and y into completed points
        completed_curve = np.column_stack((interpolated_x, interpolated_y))
        return completed_curve
    
    elif occlusion_type == 'disconnected':
        # TSS Gensolve Round 2 Solution
        # Address disconnected occlusions by bridging the endpoints
        completed_curve = bridge_disconnected_segments(points)
        return completed_curve

def bridge_disconnected_segments(points):
    """
    Bridge disconnected occlusions by connecting fragment endpoints.
    """
    # TSS Gensolve Round 2 Solution
    if len(points) < 2:
        return points
    
    # Determine the start and end points of the fragment
    start_point = points[0]
    end_point = points[-1]
    
    # Fit a line between the start and end points
    linear_model = LinearRegression()
    linear_model.fit(points[:, 0].reshape(-1, 1), points[:, 1])
    
    # Generate new points along the fitted line
    line_x = np.linspace(start_point[0], end_point[0], num=500)
    line_y = linear_model.predict(line_x.reshape(-1, 1))
    
    # Combine original points with the newly created points
    completed_curve = np.vstack((points, np.column_stack((line_x, line_y))))
    return completed_curve

# Example usage in the __1.py script
if __name__ == "__main__":
    import sys
    from utils import read_csv, plot, polylines2svg
    from regularization import fit_line, fit_circle
    from symmetry_detection import detect_symmetry
    from curve_completion import complete_curve

    input_filepath = 'problems/problems/isolated.csv'
    output_svg_filepath = 'problems/problems/output.svg'
    
    # Load the paths from the CSV file
    paths = read_csv(input_filepath)
    
    for path in paths:
        for points in path:
            # TSS Gensolve Round 2 Solution
            # Fit a line to the points
            slope, intercept = fit_line(points)
            print(f'Line fit: y = {slope}x + {intercept}')
            
            # Fit a circle to the points
            x_center, y_center, radius = fit_circle(points)
            print(f'Circle fit: center=({x_center}, {y_center}), radius={radius}')
            
            # Detect any symmetry in the points
            symmetry = detect_symmetry(points)
            print(f'Symmetry detected: {symmetry}')
            
            # Complete the curve based on the given occlusion type
            completed_points = complete_curve(points, occlusion_type='connected')
            print(f'Completed curve points: {completed_points}')
            
            # Plot the results and save them as an SVG file
            plot(paths)
            polylines2svg(paths, output_svg_filepath)
