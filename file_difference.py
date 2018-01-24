import webbrowser,lcs
from yattag import Doc,indent

def get_file_content(path):
    with open(path) as file_content:
        return list(file_content)
def generate_html_code(input1,input2,operations):
    doc,tag,text,line = Doc().ttl()
    with tag('html'):
        with tag('head'):
            doc._append('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">')
            doc._append('<script src="https://use.fontawesome.com/35ac922f38.js"></script>')
        with tag('body',klass = 'container bg-light'):
            line('h2','file difference',klass = 'text-center')
            with tag('div',klass = 'card'): ########3
                line('h4', 'File A content = ' + input1)
                doc._append('<br>')
                line('h4', 'File B content = ' + input2)

            line('h6', 'You Can Convert A To B with these operations', klass='text-center display-4')

            with tag('div',klass = 'container'):
                for i in operations:
                    if i[0:3] == 'ADD':
                        with tag('div',klass = "bg-success"):
                            line('i','',klass = 'fa fa-plus pull-right')
                            line('h4',i[3:])
                    elif i[0:3] == 'REM':
                        with tag('div',klass = "bg-danger"):
                            line('i','',klass = 'fa fa-remove pull-right')
                            line('h4',i[3:])
                    if i[0:3] == 'LCS':
                        with tag('div',klass = "bg-info"):
                            line('i','',klass = 'fa fa-star pull-right')
                            line('h4',i[3:])



    return indent(doc.getvalue())

def saveMarkedUpContentToFile(content):
        with open('output.html', 'w') as f:
            f.write(content)




if __name__ == "__main__" :
    input1 = get_file_content('input1.txt')
    input2 = get_file_content('input2.txt')

    operations = lcs.lcs(input1[0],input2[0])
    input1 = ''.join(input1[0])
    input2 = ''.join(input2[0])
    print operations
    content = generate_html_code(input1,input2,operations)
    saveMarkedUpContentToFile(content)

