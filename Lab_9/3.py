import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_1:
                    mode = 'rectangle'
                elif event.key == pygame.K_2:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_s:
                    mode = 'square'
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'
                elif event.key == pygame.K_u:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_d:
                    mode = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if mode != 'rectangle' and mode != 'circle':
                        radius = min(200, radius + 1)
                    else:
                        points = [event.pos]
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if mode == 'rectangle' or mode == 'circle':
                    points[1] = position
                else:
                    points = points + [position]
                    points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            if mode == 'rectangle':
                drawRectangle(screen, points[0], points[1])
            elif mode == 'circle':
                drawCircle(screen, points[0], points[1])
            elif mode == 'eraser':
                drawEraser(screen, i, points[i], points[i + 1], radius)
            elif mode == 'square':
                drawSquare(screen, points[0], points[1])
            elif mode == 'right_triangle':
                drawRightTriangle(screen, points[0], points[1])
            elif mode == 'equilateral_triangle':
                drawEquilateralTriangle(screen, points[0], points[1])
            elif mode == 'rhombus':
                drawRhombus(screen, points[0], points[1])
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end):
    pygame.draw.rect(screen, (255, 255, 255), (start[0], start[1], end[0] - start[0], end[1] - start[1]))

def drawCircle(screen, start, end):
    radius = ((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5
    pygame.draw.circle(screen, (255, 255, 255), start, int(radius))

def drawEraser(screen, index, start, end, width):
    pygame.draw.line(screen, (0, 0, 0), start, end, width)

def drawSquare(screen, start, end):
    size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, (255, 255, 255), (start[0], start[1], size, size))

def drawRightTriangle(screen, start, end):
    pygame.draw.polygon(screen, (255, 255, 255), [(start[0], start[1]), (end[0], start[1]), (start[0], end[1])])

def drawEquilateralTriangle(screen, start, end):
    distance = ((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5
    height = distance * 3**0.5 / 2
    pygame.draw.polygon(screen, (255, 255, 255), [(start[0], end[1]), ((start[0] + end[0]) / 2, start[1]), (end[0], end[1])])

def drawRhombus(screen, start, end):
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    pygame.draw.polygon(screen, (255, 255, 255), [(mid_x, start[1]), (end[0], mid_y), (mid_x, end[1]), (start[0], mid_y)])

main()