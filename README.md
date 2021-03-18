# Toph-OSINT
Herramienta OSINT. WIP.

## Desarrollo

Se utilizó `python` versión `3.9`

## ¿Cómo utilizar TOPH-OSINT?

`***Se recomienda un sistema operativo basado en UNIX como: distribuciones linux o macOS`

### Pre-requisitos:
* Instalar python 3
    - En linux (Guía de ejemplo): https://python-guide-es.readthedocs.io/es/latest/starting/install3/linux.html
    - En macOS (Guía de ejemplo): https://python-guide-es.readthedocs.io/es/latest/starting/install3/osx.html
* Instalar pip 
    - En linux y macOs (Guía de ejemplo): https://pip.pypa.io/en/stable/installing/

1. Instalación de dependencias:

```
make install-assets
```

2. El proyecto se inicia con: 
```
make run
```

## Pruebas unitarias
Las pruebas se inician con:
```
make test
```