def is_click_in_circle(mouse_x, mouse_y, circle_center, r):
    return (circle_center[0] - mouse_x) ** 2 + (circle_center[1] - mouse_y) ** 2 <= r ** 2
