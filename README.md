# Ejercicios de perfilamiento:

- [Backend](https://github.com/hackademymx/frontend-level/blob/master/README-backend.md)
  - Resuelvelos con python o nodejs dependiendo de la tecnología que prefieras, los 8 mejores serán los que ocupen los lugares de backend: 4 python y 4 Nodejs
- [Frontend](https://github.com/hackademymx/frontend-level/blob/master/README-frontend.md)
  - Resuelvelos con Angular o ReactJS dependiendo de la tecnología que prefieras, los 8 mejores serán los que ocupen los lugares de backend: 4 reactjs y 4 angular
- [Móvil](https://github.com/hackademymx/frontend-level/blob/master/README-movil.md)
  - Resuelvelos usando React Native, los 4 mejores serán los que ocupen los 4 lugares disponibles.
  
# Para ejecutar el servidor:
pip install virtualenv
cd ruta_del_repositorio_clonado/ejercicios-level
virtualenv -p python3 caminantesENV
source caminantesENV/bin/activate
pip install -r requirements.txt
cd registro_caminantes
./manage.py runserver

Endpoint GET:
http://localhost:8000/caminantes/
El mismo enlace le permite hacer POST

O si prefiere la terminal:
pip install httpie
El anterior paquete para hacer GET o POST como en los siguientes ejemplos:
http POST http://localhost:8000/caminantes/ nombre="Fulanito" correo="Fulanito@fulano_server.com" Km_semanales=4
http GET http://localhost:8000/caminantes/

Es posible que httpie se instale en el home de usuario, en tal caso las rutas son:
~/.local/bin/http POST http://localhost:8000/caminantes/ nombre="Fulanito" correo="Fulanito@fulano_server.com" Km_semanales=4
~/.local/bin/http GET http://localhost:8000/caminantes/
