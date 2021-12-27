class EDIT_RENDER:
  @classmethod
  def EDIT(R, note):
    content = util.read_file(FLAT.to_path(note))

    bar = FLAT_RENDER._bar(note,
                 f'<a href="/note/{note}">note</a>'
                 f'<a href="/disc/{note}">disc</a>'
                 )

    line_height = 23;

    textarea_resize_script = """
    function textarea_resize(el) {

      // https://stackoverflow.com/questions/15195209/how-to-get-font-size-in-html
      // https://stackoverflow.com/a/15195345
      linecount = el.innerHTML.split(/\\n/).length;
      el.style.height = (""" + str(line_height * 1.065) + """ * linecount)+"px";
    }
    // window.onload = () => { textarea_resize(document.getElementsByTagName("textarea")[0]); };
    """

    # compose html
    title = FLAT.title(note)
    result = "".join([f"<!DOCTYPE hmtl><html><head>{RENDER.STYLE()}<title>{title}</title></head>",
                      f"<body>{bar}<div class=\"content\">",
                      f'<h1 class="title">{title}</h1>',
                      f'<script>{textarea_resize_script}</script>'
                      f'<form method="post">'
                      #f'<textarea name="text" oninput="textarea_resize(this)" style="line-height: 23px; resize:none; overflow: auto; width: -webkit-fill-available" rows="100">{content}</textarea><br/><br/>',
                      f'<textarea name="text" class="editor_textarea" rows="100">{content}</textarea><br/><br/>',
                      f'<input type="submit" value="Submit"/></form>',
                      f"</div></body></html>"])
    return Response(result, mimetype="text/html")


@app.route("/edit/<note>", methods=['GET', 'POST'])
def route_edit(note):
  if request.method == 'POST':
    FLAT.handle_edit(note, request.form)
    return redirect(f"/edit/{note}", code=302)

  return EDIT_RENDER.EDIT(note)
