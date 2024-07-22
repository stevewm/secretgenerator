# Webhook Secret Generator

This is a rough proof-of-concept tool designed to generate secrets, in conjunction with [External Secrets](https://external-secrets.io), for applications running in a Kubernetes cluster. I created this to alleviate the hassle of generating secrets and storing them in an external store.

## Usage

SecretGenerator will look in the path specified in the `CONFIG_PATH` environment variable for configuration files (`*.yaml`) to load. These configuration files specify the application name and the secrets that should be generated for that application. For example, the following configuration file:

```yaml
---
name: sabnzbd
secrets:
  - name: api_key
    type: AlphaNumeric
    parameters:
      length: 32
  - name: nzb_key
    type: AlphaNumeric
    parameters:
      length: 32
```

Will create an endpoint at `/sabnzbd` that will return a JSON object with the generated secrets:

```json
{
  "api_key": "TAUIT8t06W3fwDX0VoymjmQ0i74vEHKS",
  "nzb_key": "XY17X7FKo3BSfURw2v2dTdwf6oq1wQQc"
}
```

## Examples

See the [examples](./examples) directory for more examples.

## TODO

- Tests
- CI
- More generators
- Proper releases
