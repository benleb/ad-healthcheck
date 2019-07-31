# healthcheck

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

*Simple [AppDaemon](https://github.com/home-assistant/appdaemon) healthcheck app. Can be used as a docker-compose healthcheck.*

## Installation

Download the `healthcheck` directory from inside the `apps` directory here to your local `apps` directory, then add the configuration to enable the `healthcheck` module.

## App configuration

```yaml
healthcheck:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`endpoint` | True | string | `healthcheck`| The endpoint URL which will be registered.

## docker-compose configuration

```yaml
healthcheck:
  test: ["CMD", "curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", "{}", "https://<appdaemon URL>:5050/api/appdaemon/<endpoint>"]
  interval: 45s
  timeout: 3s
  retries: 5
```
