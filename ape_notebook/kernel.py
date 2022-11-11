from ipykernel.kernelbase import Kernel


class ApeKernel(Kernel):
    implementation = "Ape"
    implementation_version = "0.1"
    language = "python"
    language_version = ">=3.8,<4"
    language_info = {"name": "ape", "mimetype": "text/plain", "extension": ".py"}
    banner = "Kernel for Ape"

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        # TODO:
        return super().do_execute(self, code, silent, store_history, user_expressions, allow_stdin)
