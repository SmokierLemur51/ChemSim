import pygame

pygame.init()

print(f"w: {width}\nh: {height}")

def get():
	information = pygame.display.Info()

	w = information.current_w
	h = information.current_h

	return (w, h)

t = get()

print(f"\n\nw: {t[0]}\nh: {t[1]}")