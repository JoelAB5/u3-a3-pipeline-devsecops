# U3 A3 Construcción de un Pipeline DevSecOps

Laboratorio de integración continua con Bandit (SAST) y Safety (SCA).
Repositorio: https://github.com/JoelAB5/u3-a3-pipeline-devsecops

## Secuencia de la actividad

1. Publicar la versión vulnerable en `main`.
2. Crear `feature/nueva-funcionalidad`, realizar un cambio menor y abrir un Pull Request hacia `main`.
3. Esperar la ejecución fallida y conservar los logs de Bandit y Safety.
4. Eliminar la credencial del código, leerla de una variable de entorno, añadir timeout y actualizar Requests a una versión corregida.
5. Subir la corrección a la misma rama y conservar la ejecución exitosa y el estado final del Pull Request.

## Configuración necesaria de Safety

Safety necesita una cuenta y una API key válida para CI. No guardes esa clave en archivos ni en el chat.
En GitHub abre Settings → Secrets and variables → Actions → New repository secret.
Nombre: `SAFETY_API_KEY`. Valor: tu clave de Safety.
La ausencia de la clave falla explícitamente; no se interpreta como ausencia de vulnerabilidades.

## Ajustes justificados respecto de la guía

- Se corrige la indentación del paso de instalación del YAML.
- `api_key` se denomina `api_token` para que la regla B105 identifique la credencial ficticia.
- Se conserva el control de severidad alta `-lll`. Las credenciales B105/B106/B107 se revisan además con `-l`, porque Bandit las clasifica como LOW.
- Los analizadores usan un entorno separado; Requests 2.20.0 no debe degradar las dependencias del propio Safety.
- Los análisis se ejecutan antes de la decisión final para obtener ambos logs. `Build Breaker` devuelve un código de error si cualquiera falla o no se ejecuta; `continue-on-error` no permite aprobar el job.
- Se usan versiones de Actions compatibles con runners actuales.
- Se escanea `app.py` para no analizar entornos virtuales ni material de evidencia.
- `safety check` se conserva por correspondencia con la guía, aunque Safety lo marca como obsoleto. Su funcionamiento se verificará con una API key válida.
- Un check rojo por sí solo no impide al propietario hacer merge: para bloquear la integración hay que exigir el check `security-scans` en una regla de protección de `main`.

## Entregables requeridos

- Captura del fallo de Bandit con el hallazgo B105 visible.
- Captura del fallo de Safety con las vulnerabilidades de Requests visibles.
- Captura final del Pull Request con los checks exitosos tras la remediación.
- Informe con los pasos realizados y las capturas insertadas.

Una aprobación humana de revisión y un check de CI exitoso son estados distintos. El autor no puede aprobar su propio Pull Request; si el docente exige revisión aprobada, debe participar otra persona autorizada.

## Fuentes técnicas

- Bandit B105: https://bandit.readthedocs.io/en/latest/plugins/b105_hardcoded_password_string.html
- Safety CLI: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/available-commands-and-inputs
- Safety API key: https://docs.safetycli.com/safety-docs/support/invalid-api-key-error
- Releases de Requests: https://github.com/psf/requests/releases
