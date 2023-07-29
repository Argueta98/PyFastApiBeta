## PyFastApiBeta


crear el ambito de la interfaz para trabajar python

```
conda create --name PyFastApiBeta python=3
```

Activar la interfaz

```
conda activate fastapi-crud-restapi --activar un ambito
```

Instalar complementos

```
pip install fastapi
pip install uvicorn
pip install motor
```

Generar un archivo con requerimientos del ambito

```
pip freeze > requeriments.txt
```

## EJECUTAR EL PROYECTO


```
uvicorn app:app
```

se agregar '--reload' para cargar cambios

```
uvicorn app:app --reload   
```
