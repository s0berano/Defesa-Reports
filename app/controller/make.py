from app.controller.data import temperature
from app.controller.parser import html
import imgkit

__OUT_HTML_FILE = 'out/out.html'
__OUT_HTML_JPG = 'out/out-*.jpg'
__OPTIONS_JPG = {
    'width': '1080',
    'height': '1920',
}

def report(citie_group=[['cuiaba', 'juina', 'alta_floresta', 'vila_rica', 'barra_do_garcas', 'rondonopolis'], ['caceres', 'tangara_da_serra', 'diamantino', 'sorriso', 'juara', 'sinop']]):

    model = open('app/view/model.html', 'r').read()

    position = 0
    for group in citie_group:

        data = html(temperature(group))

        try:
            with open(__OUT_HTML_FILE, 'w+') as file:
                file.write(model.replace(
                    '{%DISPLAY%}', 
                    data['display']).replace(
                        '{%TITLE%}', data['tittle']
                    )
                )

            position += 1
        except:
            return False
        else:
            imgkit.from_file(
                __OUT_HTML_FILE, 
                __OUT_HTML_JPG.replace('*', str(position)),
                options=__OPTIONS_JPG
            )

    return True
