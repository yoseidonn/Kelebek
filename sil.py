css = '<style>\n'
css += 'table {\n'
css += '    width: 100%;\n'
css += '    border-collapse: collapse;\n'
css += '    page-break-after: always;\n'
css += '}\n'
css += '@media print {\n'
css += '    @page {\n'
css += '        size: A4 portrait;\n'
css += '        margin: 2cm;\n'
css += '    }\n'
css += '}\n'
css += 'th, td {\n'
css += '    border: 1px solid black;\n'
css += '    padding: 8px;\n'
css += '    text-align: left;\n'
css += '}\n'
css += 'th {\n'
css += '    background-color: #f2f2f2;\n'
css += '}\n'
css += '</style>\n'

print(css)