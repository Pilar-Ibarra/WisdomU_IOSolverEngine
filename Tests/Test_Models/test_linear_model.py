import pytest
from Models.linear_model import LinearModel
def test_model_initialization():
    #arrange,  es preparar lo que se usara o sea crear un objeto
    my_model=LinearModel(name="optiproyect")
    #act, actuar, aqui se ejecutaria la accion que se quiere probar+

    #Assert: verificar, compruebas que coincide con el resultado que esperas, ejemplo:
    assert my_model.name=="optiproyect"
    assert my_model.type=="linear"