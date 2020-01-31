#!/usr/bin/python3
import os, sys, webbrowser, getopt
from pathlib import Path
import html
import css
import quotes

font_dir = "/home"
html_dir = os.path.dirname(os.path.realpath(__file__)) + "/FontViewer"
index_html = html_dir + "/index.html"
css_file = html_dir + "/fonts.css"
font_ext = [".otf", ".ttf", ".wot"]

def get_all_fonts(dir):
    all_fonts = []
    for root,d_names,f_names in os.walk(dir):
        for f in f_names:
            f_path = os.path.join(root, f)
            file_ext = str(os.path.splitext(f_path)[1])
            if file_ext.lower() in font_ext:
                all_fonts.append(f_path)
    return all_fonts

def create_files_and_folder():
    if not os.path.exists(html_dir):
        os.mkdir(html_dir)
    
    try:
        f_index = open(index_html, "w")
        f_index.write(html.generate_html(fonts = get_all_fonts(font_dir)))
        f_index.close()

        f_css = open(css_file, "w")
        f_css.write(css.generate_css(get_all_fonts(font_dir)))
        f_css.close()
    except:
        print("Access denied!")
        return False

    return True

def main():
    global font_dir
    if len(sys.argv)>1:
        font_dir = sys.argv[1]

    if not os.path.exists(font_dir):
        print("The path {} is not exist!".format(font_dir))
        return

    print("Searching for fonts...")
    if create_files_and_folder():
        print("Done!")
        webbrowser.open(index_html)
    else:
        print("Faield!")

if __name__ == "__main__":
    main()
