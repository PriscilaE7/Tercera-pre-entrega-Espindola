#Agenda de comidas.

## Descripción
Este proyecto es una agenda de comidas desarrollado con Django. Permite a los usuarios ver y agregar sus propias recetas,
como tambien enlistarlas para organizar su propia agenda de alimentación.

## Instalación
-En primera instancia es necesario clonar el repositorio https://github.com/PriscilaE7/Tercera-pre-entrega-Espindola
-Se requerirá la instalación de Django en la terminal: pip3 install Django
-Aplicamos las migraciones de la base de datos: python manage.py migrate
-Iniciamos el servidor local: python manage.py runserver
Abrimos el navegador y accedemos a http://127.0.0.1:8000/

## Uso
Una vez que la página esté en funcionamiento, los usuarios pueden navegar por las diferentes opciones.
En la pantalla de inicio tenemos un mensaje de bienvenida con el nombre de la página.
En la parte superior derecha se encuentran botones de <Nueva Receta>, <Todas las Recetas>, <Comentario> y <Contacto> por los cuales se podrá navegar haciendo click.

## Nueva Receta
En esta sección se encuentra un formulario en el cual el usuario puede crear una nueva receta llenando los campos requeridos de <Nombre> e <Ingredientes>.
Para probar su uso puede agregar el nombre <Omelette> y la cantidad de ingredientes <3>. Haga click en <Agregar> y de esa manera se guardará en la base de datos.

## Todas las Recetas
En esta sección encontraremos el listado de las comidas que fueron agregadas. Si realizó el paso anterior también encontrará el nombre <Omelette> entre ellas.

## Comentario
En esta sección el usuario encontrará un formulario donde le estará pidiendo que llene los campos <Nombre>, <Apellido> y <Comentario>.
Dentro del campo Comentario el usuario sera libre de dejar el mensaje que desee.
(El cual debería quedar en la página pero al hacer click en <Enviar> me arroja un error que desconozco, si puede explicarme cómo solucionar ese error estaría agradecida).

## Contacto
Sobre esta sección el usuario puede llenar con sus datos y un mensaje el formulario siempre que tenga alguna duda para que el admin pueda contactarse con él y solucionar el inconveniente.

## Inicio
Siempre que se haga click sobre el botón <Inicio> el usuario volverá a la pantalla principal con el mensaje de Bienvenida.

## Admin
El admin podrá acceder a la base de datos ingresando en el navegador http://127.0.0.1:8000/admin/
usuario: Priscila
password: 1234

## Créditos
Este proyecto fue creado por Espindola Priscila Vanesa.

## Agradecimientos
Quiero expresar mi agradecimiento al tutor Ariel Souto por brindarme su apoyo y orientación durante mi desarrollo como estudiante de programación.
