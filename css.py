import os
def generate_css(fonts):
    font_face = ""
    for font in fonts:
        f_with_ext = os.path.basename(font)
        f_without_ext = os.path.splitext(f_with_ext)[0]
        font_face = font_face + '''
        @font-face {{
            font-family:"{}";
            src: url({});
        }}
        '''.format(str(f_without_ext), font)

    style = '''
    [contenteditable]:focus {
        outline: 0px solid transparent;
    }
    ::selection {
        color: rgba(250, 0, 149, 0.87);
        background: transparent;
    }
    ::-moz-selection {
        color: rgba(250, 0, 149, 0.87);
        background: transparent;
    }
    html{
        --scrollbarBG: rgb(24, 26, 27);
        --thumbBG: rgba(250, 0, 149, 0.87);
        scrollbar-color : rgba(250, 0, 149, 0.87) rgb(24, 26, 27);
    }
    *{
        margin : 0;
        padding : 0;
    }
    body{
        background-color : rgb(24, 26, 27);
        font-family: sans-serif;
        scrollbar-width: thin;
        scrollbar-color: var(--thumbBG) var(--scrollbarBG);
    }
    body::-webkit-scrollbar {
        width: 11px;
    }
    body::-webkit-scrollbar-track {
        background: var(--scrollbarBG);
    }
    body::-webkit-scrollbar-thumb {
        background-color: var(--thumbBG) ;
        border-radius: 6px;
        border: 3px solid var(--scrollbarBG);
    }
    .header{
        width : 90%;
        text-align : center;
        border : 1px solid rgba(250, 0, 149, 0.87);
        padding : 10px;
        margin-bottom : 50px;
    }
    .header h1{
        color : rgba(232, 230, 227, 0.87);
        font-size : 50px;
    }
    .header p{
        color : rgb(150, 150, 150);
        font-size: 20px;
    }
    ul{
        list-style : none;
        padding-left : 50px;
    }
    li{
        display: inline-grid;
        padding : 20px 0 50px 0;
        border-top : 1px solid rgba(102, 102, 102, 0.4);
        margin-left : 25px;
        margin-right : 25px;
        width: -webkit-calc(27% - 100px + 0px);
        width: calc(27% - 100px + 0px);
        overflow : hidden;
    }
    .container {
        width: 90%;
        height: auto;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin : auto;
        max-width : 1920px;
    }
    .font-preview{
        font-size : 40px;
        color : rgba(232, 230, 227, 0.87);
        padding-top : 20px;
    }
    .font-title{
        color : rgba(250, 0, 149, 0.87);
        font-size : 17px;
    }

    .footer{
        font-size : 17px;
        width : 90%;
        text-align : left;
        color : rgba(102, 102, 102, 0.4);
        padding-bottom : 50px;
    }

    @media only screen and (max-width: 1900px) {
        li{
            width: -webkit-calc(35% - 100px + 0px);
            width: calc(35% - 100px + 0px);
        }
    }

    @media only screen and (max-width: 1200px) {
        li{
            width: -webkit-calc(50% - 60px + 0px);
            width: calc(50% - 60px + 0px);
        }
    }
    @media only screen and (max-width: 950px) {
        ul{
            padding-left : 0;
        }
        li{
            width: -webkit-calc(100% - 20px + 0px);
            width: calc(100% - 20px + 0px);
        }
    }
    '''
    return font_face + style