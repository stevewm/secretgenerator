# Secret Generator

Warning: Under active development and probably broken in some way I haven't noticed.

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

Will create an endpoint at `/sabnzbd` that returns a JSON object with the generated secrets:

```json
{
  "api_key": "TAUIT8t06W3fwDX0VoymjmQ0i74vEHKS",
  "nzb_key": "XY17X7FKo3BSfURw2v2dTdwf6oq1wQQc"
}
```

Each invocation of the endpoint will generate new secrets.

## Generators

At the moment the following generators are implemented:

- `AlphaNumeric`: Generates a random alphanumeric string.
- `Base64`: Generates a random base64 string.
- `BasicAuth`: Generates a random username and password in the form of `username:password`.
- `PBKDF2`: Generates a random PBKDF2 hash digest, intended for use with Authelia.

Each generator takes a set of parameters specific to it. For generators where setting the length is possible the default is 32 characters.

## Examples

See the [examples](./examples) directory.

## TODO

- Better tests
- Better CI
- More generators
- Proper releases
- Configuration schema
