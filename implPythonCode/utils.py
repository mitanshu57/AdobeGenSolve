import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from svgpathtools import parse_path

def load_csv_data(csv_path):
    # TSS Gensolve Round 2 Solution
    # Load the CSV data into a numpy array
    data_array = np.genfromtxt(csv_path, delimiter=',')
    grouped_paths = []
    
    # Group data by unique paths
    for path_id in np.unique(data_array[:, 0]):
        path_data = data_array[data_array[:, 0] == path_id][:, 1:]
        points_groups = []
        for subpath_id in np.unique(path_data[:, 0]):
            points = path_data[path_data[:, 0] == subpath_id][:, 1:]
            points_groups.append(points)
        grouped_paths.append(points_groups)
    
    return grouped_paths

def load_svg_data(svg_path):
    # TSS Gensolve Round 2 Solution
    # Parse the SVG file and extract paths
    tree = ET.parse(svg_path)
    root = tree.getroot()
    namespaces = {'svg': 'file path'}
    
    parsed_paths = []
    for path_element in root.findall('.//svg:path', namespaces):
        path_data = path_element.attrib.get('d', '')
        points = extract_points_from_svg_path(path_data)
        if points.size > 0:
            parsed_paths.append([points])
    return parsed_paths

def extract_points_from_svg_path(path_string):
    # TSS Gensolve Round 2 Solution
    # Convert the SVG path string to a series of points
    path = parse_path(path_string)
    points = []
    for segment in path:
        for point in segment:
            points.append([point.real, point.imag])
    return np.array(points)

def plot_paths(paths_XYs, output_svg_path, output_png_path):
    # TSS Gensolve Round 2 Solution
    # Plot paths and save as both SVG and PNG
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    for path_group in paths_XYs:
        for path_points in path_group:
            ax.plot(path_points[:, 0], path_points[:, 1], linewidth=2)
    ax.set_aspect('equal')
    
    # Save the plot as an SVG
    plt.savefig(output_svg_path, format='svg')
    # Save the plot as a PNG
    plt.savefig(output_png_path, format='png')
    plt.close()  # Close the figure to release memory

def convert_paths_to_svg(paths_XYs, svg_path):
    import svgwrite
    import cairosvg
    
    # TSS Gensolve Round 2 Solution
    # Determine the width and height for the SVG canvas
    max_width, max_height = 0, 0
    for path_group in paths_XYs:
        for path_points in path_group:
            max_width = max(max_width, np.max(path_points[:, 0]))
            max_height = max(max_height, np.max(path_points[:, 1]))
    
    padding_factor = 0.1
    max_width, max_height = int(max_width * (1 + padding_factor)), int(max_height * (1 + padding_factor))
    
    # Create SVG drawing
    drawing = svgwrite.Drawing(svg_path, profile='tiny', shape_rendering='crispEdges')
    path_group = drawing.g()
    
    for path_group_index, path_group in enumerate(paths_XYs):
        path_instructions = []
        for path_points in path_group:
            path_instructions.append(("M", (path_points[0, 0], path_points[0, 1])))
            for point_index in range(1, len(path_points)):
                path_instructions.append(("L", (path_points[point_index, 0], path_points[point_index, 1])))
            if not np.allclose(path_points[0], path_points[-1]):
                path_instructions.append(("Z", None))
        path_group.add(drawing.path(d=path_instructions, fill='none', stroke='black', stroke_width=2))
    
    drawing.add(path_group)
    drawing.save()
    
    # Convert the SVG to PNG with appropriate scaling
    png_output_path = svg_path.replace('.svg', '.png')
    scaling_factor = max(1, 1024 // min(max_height, max_width))
    cairosvg.svg2png(url=svg_path, write_to=png_output_path, parent_width=max_width, parent_height=max_height,
                     output_width=scaling_factor * max_width, output_height=scaling_factor * max_height,
                     background_color='white')
