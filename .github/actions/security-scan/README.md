# Trivy Security Scan

This GitHub Action performs a security scan using Trivy, capable of scanning repositories or container images. The results can be uploaded as an artifact for further inspection.

---

## Features

- **Flexible Scanning**: Supports scanning of both repositories and container images.
- **Severity Filtering**: Configure the scan to alert on specific severity levels.
- **Customizable Output**: Choose the format of the scan results and optionally upload them as artifacts.
- **Optional Steps**: Skip the installation of Trivy or Git checkout if these steps have already been completed.

---

## Inputs

| Argument                  | Description                                                        | Required | Default         |
| ------------------------- | ------------------------------------------------------------------ | -------- | --------------- |
| `trivy_artifact_name`     | The name of the Trivy report artifact.                             | No       | `trivy_report`  |
| `scan_type`               | Type of scan to perform (`repository` or `image`).                 | Yes      | `repository`    |
| `image_to_scan`           | The image to scan (required if scan_type is `image`).              | Yes      | (empty)         |
| `severities`              | Severity levels to alert on.                                       | No       | `HIGH,CRITICAL` |
| `trivy_fail_on_detection` | Fail the action if any detection is found.                         | No       | `false`         |
| `trivy_output_format`     | The output format of the Trivy scan (`table`, `json`, `template`). | No       | `table`         |
| `create_artifact`         | Upload the scan results as an artifact.                            | No       | `true`          |
| `repo_path`               | The repository working directory.                                  | No       | `.`             |
| `skip_trivy_installation` | Skip Trivy installation if done in previous steps.                 | No       | `false`         |
| `skip_checkout`           | Skip Git repository checkout.                                      | No       | `true`          |

---

## Usage

### Example Workflow
```yaml
name: Trivy Security Scan

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Trivy Security Scan
        uses: ./
        with:
          scan_type: 'repository'
          severities: 'HIGH,CRITICAL'
          create_artifact: 'true'

## Example Use Cases

	1.	Scan a Repository for High and Critical Vulnerabilities:
  ```yaml
  with:
    scan_type: 'repository'
    severities: 'HIGH,CRITICAL'
  ```

	2.	Scan a Docker Image:
  ```yaml
  with:
    scan_type: 'image'
    image_to_scan: 'my-docker-image:latest'
  ```

	3.	Skip Trivy Installation (if already installed):
  ```yaml
  with:
    skip_trivy_installation: 'true'
  ```

	4.	Upload Scan Results as an Artifact:
  ```yaml
  with:
    create_artifact: 'true'
  ```

## Error Handling

	•	The action ensures that Trivy is installed unless explicitly skipped.
	•	The scan results are output in the chosen format and can be uploaded as artifacts for later use.
	•	The action allows filtering based on vulnerability severity and can fail the workflow if any issues are detected.
