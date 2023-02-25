@app.route('/test/unit/render_msg')
def test_render_msg():
  msg = {'msg': 'AWAKEN a bit ago, RECAP PLAY GAME vampire survivors',
         'Date': 'Tue Feb 14 11:13:50 PST 2023'}
  for i in range(1000):
    DISCUSSION_RENDER.msg(msg)
  return 'DONE'

@app.route('/test/unit/date_cmd')
def test_date_cmd():
  for i in range(10000):
    util.date_cmd("-d", 'Tue Feb 14 11:13:50 PST 2023', "+%T")
  return 'DONE'


@app.route('/test/unit/render_every_note')
def test_render_every_note():
  for note in FLAT.list():
    DISCUSSION_RENDER.MAIN(note)
  return 'DONE'

@app.route('/test/unit/pagesize_every_note')
def test_pagesize_every_note():
  size = 0
  for note in FLAT.list():
    size += len(DISCUSSION_RENDER.MAIN(note))
  return 'rendered size: ' + str(size)
