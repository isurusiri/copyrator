# Copyrator

Copyrator is a Kubernetes operator to copy configmaps when a new namespace is created or when a configmap or secret is change it's state. This covers following aspects with the Kubernetes operator development in this project.

- Custom Resource Definitions (CRDs) to interact with the operator.
- Operator is configurable via command line flags and environment variables.
- Docker image and Helm chart for installing the operator.


