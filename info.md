## App configuration

```yaml
hacs:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`endpoint` | True | string | `healthcheck`| The endpoint URL which will be registered.
