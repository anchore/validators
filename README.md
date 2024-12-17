# Validators

## NTIA
```
cd ntia
docker build -t ntia-checker-image .
cat <SOME_SBOM.json> | docker run -i --rm ntia-checker-image --extension json
```

## Cyclone-DX
`cat <SOME_SBOM.json> | docker run -i --rm cyclonedx/cyclonedx-cli validate --input-format json`
