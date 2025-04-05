from graphics import GraphWin, Rectangle, Point, GraphicsError
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser, cells):
    """Erase objects in contact with the eraser"""
    eraser_x1 = eraser.getP1().getX()
    eraser_y1 = eraser.getP1().getY()
    eraser_x2 = eraser.getP2().getX()
    eraser_y2 = eraser.getP2().getY()
    
    # Check each cell to see if it overlaps with the eraser
    for cell in cells:
        cell_x1 = cell.getP1().getX()
        cell_y1 = cell.getP1().getY()
        cell_x2 = cell.getP2().getX()
        cell_y2 = cell.getP2().getY()

        # If the eraser overlaps with the cell, "erase" it (make it white)
        if not (eraser_x2 < cell_x1 or eraser_x1 > cell_x2 or 
                eraser_y2 < cell_y1 or eraser_y1 > cell_y2):
            cell.setFill("white")

def main():
    canvas = GraphWin("Eraser", CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.setBackground("white")

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    cells = []  # Store all cell rectangles

    # Create the grid
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            cell.setFill("blue")
            cell.draw(canvas)
            cells.append(cell)  # Store cell in list

    # Wait for the user to click before creating the eraser
    canvas.getMouse()

    last_click_x, last_click_y = canvas.getMouse().getX(), canvas.getMouse().getY()

    # Create the eraser
    eraser = Rectangle(Point(last_click_x, last_click_y), 
                       Point(last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE))
    eraser.setFill("pink")
    eraser.draw(canvas)

    # Move the eraser with the mouse and erase touching objects
    while True:
        try:
            mouse_x, mouse_y = canvas.getMouse().getX(), canvas.getMouse().getY()
            dx = mouse_x - eraser.getP1().getX()
            dy = mouse_y - eraser.getP1().getY()

            # Move eraser
            eraser.move(dx, dy)

            # Erase overlapping objects
            erase_objects(canvas, eraser, cells)

            time.sleep(0.05)
        except GraphicsError:
            break  # Exit loop if window is closed

    canvas.close()

if __name__ == "__main__":
    main()
