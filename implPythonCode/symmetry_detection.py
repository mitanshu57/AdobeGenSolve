# TSS Gensolve Round 2 Solution
# symmetry_detection.py
import numpy as np
# TSS Gensolve Round 2 Solution
def detect_symmetry(points):
    # TSS Gensolve Round 2 Solution
    # Reflect points over their centroid
    centroid = np.mean(points, axis=0)
    reflected_points = 2 * centroid - points
    # TSS Gensolve Round 2 Solution
    # Check for symmetry by comparing original and reflected points
    differences = np.linalg.norm(points - reflected_points, axis=1)
    symmetry = np.all(differences < 1e-6) 
    # TSS Gensolve Round 2 Solution
    # Tolerance for floating point comparison
    
    return symmetry
