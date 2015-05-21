import melange
import sys

@melange.app(client='pyglet')
def draw(canvas):
    print('hello melange')
    canvas.image(64, 64, "helloworld.png")


if __name__=='__main__':
    sys.exit(draw())