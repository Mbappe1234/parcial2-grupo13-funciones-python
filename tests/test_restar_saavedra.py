from funciones.restar_saavedra import restar_saavedra

def test_restar_saavedra():
    # Caso 1: resta normal
    assert restar_saavedra(10, 4) == 6

    # Caso 2: resultado negativo
    assert restar_saavedra(5, 10) == -5

    # Caso 3: resta con cero
    assert restar_saavedra(7, 0) == 7
