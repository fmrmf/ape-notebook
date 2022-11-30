from ipykernel.kernelapp import IPythonKernel


class ApeKernel(IPythonKernel):
    implementation = "ape"
    implementation_version = "0.1"

    def __init__(self, **kwargs):
        """
        Applies same namespace logic from ape_console to IPythonKernel.

        SEE: https://github.com/ApeWorX/ape/blob/main/src/ape_console/_cli.py
        SEE: https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html
        """
        import ape

        # update user ns to ape prior to calling super
        ns = {component: getattr(ape, component) for component in ape.__all__}
        ns["ape"] = ape
        self.user_ns = ns

        super().__init__(**kwargs)
