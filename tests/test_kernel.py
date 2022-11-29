import ape


def test_ape_kernel_user_ns(kernel):
    # check namespace contains ape console ns
    ape_ns = {component: getattr(ape, component) for component in ape.__all__}
    ape_ns["ape"] = ape
    assert ape_ns.items() <= kernel.user_ns.items()
