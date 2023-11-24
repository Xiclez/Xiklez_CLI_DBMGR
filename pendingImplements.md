<h1>+++EZ1s:+++</h1>


```

            	  _)_
               .-'(/ '-.
              /    `    \
             /  -     -  \
            (`  a     a  `)
             \     ^     /
              '. '---' .'
              .-`'---'`-.
             /           \
            /  / '   ' \  \
          _/  /|       |\  \_
         `/|\` |+++++++|`/|\`
              /\       /\
              | `-._.-` |
              \   / \   /
              |_ |   | _|
       jgs    | _|   |_ |
              (ooO   Ooo)

```
<ul>
<li>Si quieren usar mi base de datos, pedir las credenciales para loguearse</li>
<li>Agregar opcion en menu para crear nueva base de datos</li>
<li>Agregar opcion en menu para limpiar output</li>
<li>Agregar Empty State</li>
<li>Mejorar esteticamente el programa(Nuevos menus, colores, animaciones etc)</li>
</ul>

```
--Pseudocodigo:
des = "usar xiklesdb? y/n"

if des = y:
user= "ingrese usuario:"
pw= "ingrese contraseña:"

cadena de conexion = db_url = "mongodb+srv://<user>:<pw>@ulsa.cpqqpie.mongodb.net/"

[integrar funcion connect to mongo db]:

	try:
        client = pymongo.MongoClient(db_url)
        db = client[database]
        collection = db[collection_name]
        return client, collection
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error al conectar la base de datos: {e}")
        des=(Intentar de nuevo y/n)
        if des == Y:
        return get_con_data
        else
        des=(deseas usar tu propia base de datos o salir del programa)?
	if des == 1:
	contunuar flujo linea 48;
	else
	end;
```

```
+++BadBoyz:+++

                  .--""""--.
nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
              : J J___/\___L L :#####################
nnnnnnnnnnnnnn{ [{ `.    ,' }] }## ### ### ### ### ##
NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
               \ L,`*n,,n*',J /
nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
```
<ul>
<li>Manejar correctamente valores nulos</li>
<li>Dar esquema de datos adecuado</li>
<li>Testeo general en busca de errores</li>
<li>Refinar busqueda(implemetar islike etc)</li>
<li>Deployment</li>
</ul>
```
+++Devil Shit:+++

          (                      )
          |\    _,--------._    / |
          | `.,'            `. /  |
          `  '              ,-'   '
           \/_         _   (     /
          (,-.`.    ,',-.`. `__,'
           |/#\ ),-','#\`= ,'.` |
           `._/)  -'.\_,'   ) ))|
           /  (_.)\     .   -'//
          (  /\____/\    ) )`'\
           \ |V----V||  ' ,    \
            |`- -- -'   ,'   \  \      _____
     ___    |         .'    \ \  `._,-'     `-
        `.__,`---^---'       \ ` -'
           -.______  \ . /  ______,-
                   `.     ,'            
```

Permitir ver y gestionar bases de datos creadas con este programa(Atlas API)
Implementar custom_schema y editar schemas predefinidos 

