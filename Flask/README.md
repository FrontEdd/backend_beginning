## Crear un entorno virtual

```
nombre_entorno -> puede cambiar
python -m venv nombre_entorno
```

## Activar un entorno virtual

```
- Gitbash
Windows
source nombre_entorno/Scripts/activate
No Windows
source nombre_entorno/bin/activate
```

## Desactivar entorno virtual

```
deactivate
```

## Instalar modulos de python

```
pip install nombre_modulo
```

## Crear nuestro archivo requirements

```
pip freeze > requirements.txt
```

## Instalación desde el requirements

```
pip install -r requirements.txt
```

## Desinstalar un modulo

```
pip uninstall nombre_modulo
```

## Desinstalar masiva desde el requirements

```
pip uninstall -r requirements.txt
```

## Actualizar una dependencia hasta su versión actual

```
pip install nombre_modulo --upgrade
pip install nombre_modulo -U
```

## Instalar una versión definida por ti

```
pip install nombre_modulo=0.1
```

## Crear un entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
- Windows: source venv/Scripts/activate
- Mac / Linux: source venv/bin/activate
```

## Desactivar entorno virtual

```
deactivate
```

### Endpoints

## Put - Patch

```
Put -> Actualización completas
Patch -> Actualización parcial
Usuario
- nombres
- apellidos
- fecha_nacimiento
- genero
PUT
----------------
http://dominio.com/users/:id
{
 "nombres": "Nuevo Nombre",
 "apellidos": "",
 "fecha_nacimiento": "",
 "genero": ""
}
PATCH
-----------------
http://dominio.com/users/:id
{
 "nombres": "Nuevo Nombre",
 "apellidos": "Nuevo Apellido"
}
```