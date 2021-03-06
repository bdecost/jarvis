from jarvis.core.specie import Specie


def test_sp():
    el = Specie("Al")
    assert (
        el.Z,
        round(el.atomic_mass, 2),
        el.symbol,
        round(el.get_chgdescrp_arr[1], 2),
        round(el.get_descrp_arr[1], 2),
    ) == (13, 26.98, "Al", 12.17, 2792.11)
