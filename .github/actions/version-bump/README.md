# Version Bump GitHub Action

This GitHub Action automates the process of version bumping (major, minor, or patch), creating a new tag, and pushing it to the repository.

---

## Features

- **Automated Versioning**: Supports semantic versioning (`major`, `minor`, `patch`).
- **Custom Git Configuration**: Allows setting the Git username and email for tag creation.
- **Tag Management**: Fetches the latest tags, calculates the new version, and pushes the updated tag.

---

## Inputs

| Argument         | Description                                           | Required | Default |
| ---------------- | ----------------------------------------------------- | -------- | ------- |
| `version_type`   | The type of version bump (`major`, `minor`, `patch`). | Yes      | `patch` |
| `git_user_name`  | The Git username for tag creation.                    | Yes      | None    |
| `git_user_email` | The Git email for tag creation.                       | Yes      | None    |

---

## Usage

### Example Workflow
```yaml
name: Version Bump

on:
  push:
    branches:
      - main

jobs:
  bump-version:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Version Bump
        uses: ./
        with:
          version_type: 'minor'
          git_user_name: 'Your GitHub Username'
          git_user_email: 'your-email@example.com'

      - name: Push Changes
        run: |
          echo "Version bump completed and new tag pushed."
```

---

## Example Use Cases

1. **Increment Patch Version**:
   ```yaml
   with:
     version_type: 'patch'
     git_user_name: 'example-user'
     git_user_email: 'user@example.com'
   ```

2. **Increment Minor Version**:
   ```yaml
   with:
     version_type: 'minor'
     git_user_name: 'example-user'
     git_user_email: 'user@example.com'
   ```

3. **Increment Major Version**:
   ```yaml
   with:
     version_type: 'major'
     git_user_name: 'example-user'
     git_user_email: 'user@example.com'
   ```

---

## Error Handling

- Ensures Git is installed and configured with the specified username and email.
- Fetches the latest tags; if no tags exist, defaults to `v0.0.0`.
- Handles empty or improperly formatted tags by initializing the version to `0.0.0`.
- Pushes the new tag to the repository; ensure a GitHub personal access token (PAT) is available in the environment as `GIT_PAT`.

---

## Notes

- The action requires a valid GitHub PAT stored as a secret (`GIT_PAT`) in your repository to push tags.
- Semantic versioning is used for calculating the next version.
- Ensure the action has permission to push tags to the repository.
