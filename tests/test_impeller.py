from impeller import *

def test_version():
  assert(get_version() != 0)

def test_structs():
  r = Rect()
  r.width = 13
  r.height = 14
  assert(r.x == 0)
  assert(r.y == 0)
  assert(r.width == 13)
  assert(r.height == 14)
  r2 = Rect()
  assert(r2.width == 0)

def test_display_list_builder():
  dl_builder = DisplayListBuilder()
  dl_builder.clip_oval(Rect(), ClipOperation.DIFFERENCE).build()

def test_can_create_window():
  context = Context(ContextBackend.METAL)
  window = get_main_window()
  while not window.should_close():
    window.poll_events()
    surface = window.create_render_surface(context)
    paint = Paint()

    color = Color()
    color.red = 1.0
    color.green = 1.0
    color.blue = 1.0
    color.alpha = 1.0
    paint.set_color(color)

    paint = Paint()
    paint.set_color(color)

    rect = Rect()
    rect.x = 100
    rect.y = 200
    rect.width = 200
    rect.height = 300

    dl_builder = DisplayListBuilder()
    dl_builder.draw_rect(rect, paint)
    dl = dl_builder.build()

    surface.draw(dl)

    surface.present()
