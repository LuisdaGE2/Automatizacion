from Areatriangulo import area_triangulo
import pytest

def test_area_correcto():
    assert area_triangulo(5, 7) == pytest.approx(17.5)
    
def test_area_negativo():
    with pytest.raises(ValueError):
        area_triangulo(-5, 7)
    with pytest.raises(ValueError):
        area_triangulo(5, -7)
    with pytest.raises(ValueError):
        area_triangulo(-5, -7)
        
def test_area_base_cero():
    with pytest.raises(ValueError):
        area_triangulo(0, 7)
 

