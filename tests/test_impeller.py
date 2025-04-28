from impeller import *
from impeller import impeller
from PIL import Image
import os
import pytest


def test_version():
    assert get_version() != 0


def test_structs():
    r = impeller.Rect()
    r.width = 13
    r.height = 14
    assert r.x == 0
    assert r.y == 0
    assert r.width == 13
    assert r.height == 14
    r2 = Rect_()
    assert r2.width == 0


def test_display_list_builder():
    dl_builder = DisplayListBuilder_()
    dl_builder.clip_oval(impeller.Rect(), ClipOperation_.DIFFERENCE).build()


def test_can_create_window():
    context = Context_(ContextBackend_.METAL)
    window = get_main_window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        paint = Paint_()

        color = impeller.Color(a=1, b=1)
        paint.set_color(color)

        paint = Paint_()
        paint.set_color(color)

        rect = impeller.Rect(100, 200, 200, 300)

        dl_builder = DisplayListBuilder_()
        dl_builder.draw_rect(rect, paint)
        dl = dl_builder.build()

        surface.draw(dl)

        surface.present()


def test_can_draw_image(pytestconfig):
    image = Image.open(
        os.path.join(pytestconfig.rootpath, "assets/airplane.jpg")
    )
    assert image.size[0] > 0
    assert image.size[1] > 0
    image.tobytes()
