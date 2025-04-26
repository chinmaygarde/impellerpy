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

def test_display_list_builder():
  dl_builder = DisplayListBuilder()
  dl_builder.clip_oval(Rect(), ClipOperation.DIFFERENCE).build()
