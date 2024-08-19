from ursina import window

def percentage_to_x_coordinate(percentage):
    """
    Transform a percentage into an x coordinate within the window.
    
    :param percentage: Input percentage (0-100)
    :return: Transformed x coordinate
    """
    return percentage_to_coordinate(percentage, window.aspect_ratio * -.5, window.aspect_ratio * .5)

def percentage_to_y_coordinate(percentage):
    """
    Transform a percentage into a y coordinate within the window.
    
    :param percentage: Input percentage (0-100)
    :return: Transformed y coordinate
    """
    return percentage_to_coordinate(percentage, .5, -.5)

def percentage_to_coordinate(percentage, min_coord, max_coord):
    """
    Transform a percentage into a coordinate within a given range.
    
    :param percentage: Input percentage (0-100)
    :param min_coord: Minimum coordinate value
    :param max_coord: Maximum coordinate value
    :return: Transformed coordinate
    """
    # Ensure percentage is between 0 and 100
    percentage = max(0, min(percentage, 100))
    
    # Transform percentage to a value between 0 and 1
    normalized = percentage / 100
    
    # Calculate the coordinate
    coordinate = min_coord + (max_coord - min_coord) * normalized
    
    return coordinate
