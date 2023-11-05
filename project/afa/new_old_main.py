import curses
from typing import List
from panel import Panel

def main(screen):
    # Disable cursor blinking
    curses.curs_set(False)

    session = create_session()

    # Create parent panel
    parent = Panel(screen, 0, 0, curses.COLS, curses.LINES)
    main = parent.create_child(0,0,1000,1000)
    main.add_border(curses.COLOR_YELLOW)

    # Create child panels
    child1 = main.create_child(2, 2, 20, 10)
    child2 = main.create_child(25, 2, 20, 10)
    child3 = main.create_child(2, 14, 43, 15)

    # Add content to child panels
    child1.add_content(["This is child panel 1"])
    child2.add_content(["This is child panel 2"])
    child3.add_content(["This is child panel 3"])

    # Add borders to child panels
    child1.add_border(curses.COLOR_RED)
    child2.add_border(curses.COLOR_GREEN)
    child3.add_border(curses.COLOR_BLUE)

    # Redraw all panels
    parent.redraw()

    # Wait for user input
    screen.getch()

    # Clean up
    curses.curs_set(True)
    curses.endwin()

curses.wrapper(main)
