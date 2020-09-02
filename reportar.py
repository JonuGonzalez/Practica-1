import webbrowser


def reportar(nombre):
    import json
    htmFile = open("reporte.html", "w")
    htmFile.write("""<!DOCTYPE HTML PUBLIC"

    <html>

    <head>
        <title>REPORTE</title>
     <meta charset="utf-5">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    
    <style type="text/css">
            body{
                background-color: #474D5A;
            }
            div#reporte {
                width: 60%;
                height: 98%;
                border:solid black;	
                background-color: #B1B7C4;
                margin: 20%;
                margin-top: 0;
                border-radius: 50px;
            }
            div#titulo{
                background-color: black;
                border:solid black;
                border-radius: 50px;
                height:10%;
            }
            h1{
                font-family: arial,helvetica;
                color: white;
            }
            h4{
                font-family: arial,helvetica;
                color: black;
            }
            h5{
                font-family: arial,helvetica;
                color: black;
            }
        </style>
    </head>
    <body>
        <div id="reporte">
            <div id="titulo">
                <center>
                    <h1>Reporte  Jonathan González</h1>
                </center>
            </div>
            <center>
                <h4>
                    Registros Seleccionados	
                </h4>            
  <table class="table">
    <thead>
      <tr>
       <th>nombre</th>
        <th>edad</th>
        <th>activo</th>
        <th>saldo</th>
      </tr>
    </thead>

    """)

    with open(nombre) as contenido:
        p = json.load(contenido)
        contenido = ""
        for i in p:
            contenido += (" <tbody>"
                          "<td>" + i['nombre'] + "</td>"
                                                 "<td>" + str(i['edad']) + "</td>"
                                                                           "<td>" + str(i['activo']) + "</td>"
                                                                                                       "<td>" + str(
                i['saldo']) + "</td>"
                              "</tbody>")

    htmFile.write(contenido)

    htmFile.write("""






  </table>
</div>
    </body>
    </html>""")

    htmFile.close


archivo = 'archivo1.json'
reportar(archivo)
webbrowser.open_new_tab('reporte.html')
