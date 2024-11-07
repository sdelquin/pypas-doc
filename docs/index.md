# pypas

Si damos por buena aquella frase de «A programar se aprende programando», sería muy útil disponer de «problemas» a los que encontrar una solución mediante código. Pues este proyecto viene a dar respuesta a este escenario.

`pypas` te ofrece **cientos de ejercicios** con los que podrás practicar tu lenguaje de programación favorito **Python**.

NOTE: **¡Recuerda!**
[Aprende Python](https://aprendepython.es) ... **comiendo pipas!**

Este paquete proporciona una **herramienta en línea de comandos** llamada `pypas` mediante la cual podrás interactuar con los ejercicios.

## Instalación

Hay varias formas de instalar el paquete `pypas-cli`:

### uv

>?NOTE: **Requisitos**
>
> Necesitas [instalar uv](https://docs.astral.sh/uv/getting-started/installation/) que es un gestor (rápido y eficiente) de paquetería para Python.

Una vez que tengas `uv` instalado, abre una terminal y ejecuta el siguiente comando:

```console
uv tool install -n -p 3.13 pypas-cli
```

>? WARNING: **PATH**
> Para que puedas usar correctamente el ejecutable `pypas` debes añadir a tu `PATH` la ruta `$HOME/.local/bin` (en [Linux/MacOS](https://www.youtube.com/watch?v=xeXEEp-tqgY)) o `%HOMEPATH%\.local\bin` (en [Windows](https://www.youtube.com/watch?v=JND4SsPQ3HU)).

### pip

>?NOTE: **Requisitos**
>
> Necesitas [instalar Python >= 3.10](https://www.python.org/downloads/).

Una vez que tengas `python` instalado, abre una terminal y ejecuta el siguiente comando:

```console
python -m pip install pypas-cli
```

### pipx

>?NOTE: **Requisitos**
>
> Necesitas [instalar pipx](https://pipx.pypa.io/stable/installation/) que es una herramienta para instalar aplicaciones Python en entornos aislados.

Una vez que tengas `pipx` instalado, abre una terminal y ejecuta el siguiente comando:

```console
pipx install pypas-cli
```

## Actualización

Es **fundamental** que tengas instalada la **última versión disponible** de `pypas-cli`, para evitar fallos y disponer de las mejoras implementadas.

Para actualizar a la última versión de `pypas-cli` puedes usar la propia herramienta (_self-upgrading_):

```console
pypas upgrade
```

>? WARNING: **Actualización «manual»**
> Si tienes algún problema con el comando de actualización `pypas upgrade`, también puedes actualizar manualmente el paquete `pypas-cli`. Este proceso dependerá del gestor de paquetes que hayas utilizado:
>
> - **uv** → `uv tool upgrade --no-cache pypas-cli`
> - **pip** → `python -m pip install --no-cache -U pypas-cli`
> - **pipx** → `pipx upgrade pypas-cli`

> NOTE: **ÚLTIMA VERSIÓN**
> La última versión disponible de <a href="https://pypi.org/project/pypas-cli/">pypas-cli</a> es la **{{pypas_cli_version}}**

## Listar los ejercicios

Para listar todos los ejercicios «públicos» basta con ejecutar el siguiente comando:

```console
pypas list
```

### Filtros

Es posible aplicar distintos filtros para refinar el listado de ejercicios:

- Filtrar por **tema principal** (_primary topic_):

    ```console
    pip list -p <topic>
    ```

- Filtrar por **tema secundario** (_secondary topic_):

    ```console
    pip list -s <topic>
    ```

- Filtrar por **frame** (_secondary topic_):

    ```console
    pip list -f <topic>
    ```

>? INFO: **Combinando filtros**
> Es posible combinar los filtros anteriores para obtener un mejor resultado.

## Obtener un ejercicio

Cada ejercicio dispone de un **slug** que lo identifica (_nombre único_).

Supongamos que queremos trabajar en el ejercicio `add`. Para obtenerlo escribimos el siguiente comando:

```console
pypas get add
```

El comando anterior creará una carpeta `add` con los siguientes directorios y ficheros:

```console
.
├── docs
│   └── README.pdf
├── main.py
├── tests
│   ├── __init__.py
│   └── test_main.py
└── vendor.py
```

Es posible que esta estructura cambie ligeramente, en función de las características del ejercicio.

## Enunciado de un ejercicio

Una vez dentro de la carpeta del ejercicio, podemos visualizar el **enunciado del ejercicio** mediante el siguiente comando:

```console
pypas doc
```

Previsiblemente se abrirá un documento `.pdf` con la explicación del ejercicio.

>? WARNING: **Dentro de la carpeta**
> Este ejercicio requiere estar dentro de la carpeta del ejercicio → `cd <ejercicio>`

## Probar un ejercicio

El punto de entrada de la mayoría de los ejercicios es `main.py`. Será el fichero que debes cumplimentar buscando la etiqueta `# TODO`.

Para probar (_testear_) un ejercicio puedes usar:

```console
pypas test
```

>? INFO: **pytest**
>En realidad `pypas test` es un simple «wrapper» para [pytest](https://docs.pytest.org/en/stable/). Aprovecha todo el potencial de `pytest` usando las [opciones en línea de comandos](https://docs.pytest.org/en/6.2.x/usage.html) que ofrece.
>
> Los tests que se ejecutan son aquellos que viven en la carpeta `tests` de cada ejercicio. Por lo tanto también puedes probar el ejercicio con:
> ```console
> pytest
> ```

>? WARNING: **Dentro de la carpeta**
> Este ejercicio requiere estar dentro de la carpeta del ejercicio → `cd <ejercicio>`

## Ejecutar un ejercicio

Eventualmente podrías querer **ejecutar tu código** en vez de lanzar las pruebas.

Para explicar cómo, vamos a partir del ejercicio `add`. Este sería su `main.py` una vez terminado:

```python
def run(a: int, b: int) -> int:
      result = x + y
      return result

# DO NOT TOUCH THE CODE BELOW
# ...
```

Tendrás que crear un fichero `args.py` dentro de la carpeta del ejercicio con los valores que quieras dar a los **parámetros de la función principal**:

```python
a = 3
b = 7
```

Ahora podrás ejecutar tu programa con:

```console
pypas run
```

Puedes utilizar esta estrategia para depurar los errores o mejorar tu código.

>? INFO: **python**
>En realidad `pypas run` es un simple «wrapper» para `python main.py`. Por tanto puedes usar este comando directamente o las variaciones que creas correspondiente.

>? WARNING: **Dentro de la carpeta**
> Este ejercicio requiere estar dentro de la carpeta del ejercicio → `cd <ejercicio>`

## Actualizar un ejercicio

Es posible que, debido a la corrección de errores o mejoras introducidas, haya actualizaciones de los ejercicios.

En ese caso, puedes **actualizar el ejercicio** con:

```console
pypas update
```

Se hará automáticamente una copia de seguridad (local) de aquellos ficheros (propios) que puedan ser sobreescritos.

>? WARNING: **Dentro de la carpeta**
> Este ejercicio requiere estar dentro de la carpeta del ejercicio → `cd <ejercicio>`

## Comprimir un ejercicio

Si quisieras comprimir todo el contenido del ejercicio para enviarlo o almacenarlo, lo puedes hacer con:

```console
pypas zip
```

El comando anterior genera un fichero `<ejercicio>.zip` dentro de la propia carpeta del ejercicio con todos los ficheros (exluyendo ciertos ficheros «temporales» o «auxiliares»).

>? WARNING: **Dentro de la carpeta**
> Este ejercicio requiere estar dentro de la carpeta del ejercicio → `cd <ejercicio>`

## Autenticarse como usuario

Para poder autenticarte como usuario debes recibir un **token** por parte del administrador. Una vez que dispongas de este «token» debes ejecutar el siguiente comando:

```console
$ pypas auth <pon-aqui-tu-token-quitando-los-angulitos>
```

Si la autenticación ha sido satisfactoria, se creará un fichero `.pypas.toml` en el `HOME` del usuario con la configuración correspondiente.

### Desautenticarse

Es posible eliminar el «token» de autenticación ejecutando el comando:

```console
pypas unauth
```

## Entregar un ejercicio

Para entregar (_subir_) un ejercicio a [pypas.es](https://pypas.es) debes ejecutar el siguiente comando:

```console
pypas put
```

>? INFO: **Requiere autenticación** 
> Este comando necesita estar previamente [autenticado/a](#autenticarse-como-usuario).

>? WARNING: **Dentro de la carpeta**
> Este ejercicio requiere estar dentro de la carpeta del ejercicio → `cd <ejercicio>`

El comando anterior [comprime todos los archivos](#comprimir-un-ejercicio) de tu ejercicio y los sube a [pypas.es](https://pypas.es).

## Seguir tu actividad

Para seguir tu actividad puedes lanzar el siguiente comando:

```console
pypas log
```

Con el comando anterior podrás obtener la **información de tus entregas**, separadas por **frames**. Un frame es un "bloque de ejercicios" que suele tener asociada una fecha de comienzo y una fecha de finalización.

Dentro de cada «frame» verás la siguiente información:

- **Uploaded**: número de ejercicios entregados sobre el total de ejercicios del frame.
- **Passed**: número de ejercicios que han pasado todos los tests.
- **Failed**: número de ejercicios que no han pasado todos los tests.
- **Waiting**: número de ejercicios que están pendientes de testearse.
- **Score**: nota (puntuación). Ejercicios satisfactorios («passed») entre el total disponible.

Puedes obtener **información más detallada sobre cada ejercicio** entregado utilizando lo siguiente:

```console
pypas log -v
```

Puedes obtener **información de un determinado «frame»** utilizando lo siguiente:

```console
pypas log -f <frame>
```

>? INFO: **Requiere autenticación** 
> Este comando necesita estar previamente [autenticado/a](#autenticarse-como-usuario).

## Miscelánea

- `pypas --version` te proporciona la **versión actual instalada** del paquete `pypas-cli`.
- `pypas --help` te proporciona **ayuda** sobre el modo de uso del programa. Puedes aplicar `--help` sobre cualquier comando.

Si quieres informar de cualquier **error** o **propuesta de mejora**, lo puedes hacer en [GitHub](https://github.com/sdelquin/pypas-cli/issues) o escribiendo un correo (ver «footer»).
