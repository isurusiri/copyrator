import kubernetes
from contextlib import suppress
from kubernetes.client.rest import ApiException

CRD_GROUP = 'isurusiri.com'
CRD_VERSION = 'v1'
CRD_PLURAL = 'copyrators'


# load_crd queries the api server and loads all rules / crds.
# for the rule created in workloads/examples/copyrator-rule.yaml
# this will output something similar to below,
# {'ruleType': 'configmap', 'selector': {'copyrator': 'true'}, 'namespace': ['default']}
def load_crd(namespace, name):
    client = kubernetes.client.ApiClient()
    custom_api = kubernetes.client.CustomObjectsApi(client)

    with suppress(ApiException):
        crd = custom_api.get_namespaced_custom_object(
            CRD_GROUP,
            CRD_VERSION,
            namespace,
            CRD_PLURAL,
            name,
        )

    return {x: crd[x] for x in ('ruleType', 'selector', 'namespace')}
