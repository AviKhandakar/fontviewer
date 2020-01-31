import os
import quotes
def main_content(fonts):
    f_list = ""
    for font in fonts:
        f_with_ext = os.path.basename(font)
        f_without_ext = os.path.splitext(f_with_ext)[0]
        f_list = f_list + '''
        <li>
            <p class = "font-title">{}</p>
            <p class = "font-preview" contenteditable = "true" spellcheck="false" style = "font-family : {};">{}</p>
        </li>
        '''.format(str(f_without_ext[0:35]), str(f_without_ext), quotes.get_quote())
    return f_list

def generate_html(fonts = [], title = "Font Viewer", css = "style.css"):
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="fonts.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{}</title>
</head>
<body>
    <div class = "container">
        <section class="header">
            <h1>Font Viewer</h1>
            <p>Total <span style = "color : rgba(250, 0, 149, 0.87)">{}</span> fonts found!</p>
        </section>
        <ul>
            {}
        </ul>
        <p class = "footer">&copy;2020, Avi Khandakar</p>
    </div>
    
    <script>
    var all_prev = document.getElementsByClassName("font-preview");
    var d_html = "";
    for(prev of all_prev){{
        prev.onfocus = function(){{
            d_html = this.innerHTML;
            this.innerHTML = "";
        }}
        prev.onblur = function(){{
            if (this.innerHTML == "") {{
                this.innerHTML = d_html;
            }}
        }}
    }}
    </script>
</body>
</html>'''.format(title, len(fonts), main_content(fonts))

    return html