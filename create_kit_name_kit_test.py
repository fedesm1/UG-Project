import data
import sender_stand_request

# La funcion get_kit_body cambia el contenido del cuerpo solicitud para la creacion del kit
def get_kit_body (name):
    body_name = data.kit.copy()
    body_name["name"] = name
    return body_name

# La funcion get_new_user_token guarda el codigo token del usuario registrado
def get_new_user_token():
    token=data.headers["Authorization"]
    return token

# La funcion positive_assert aplica los datos de prueba positivos en el cuerpo de la solicitud
def positive_assert(kit_body):
    kit1_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit1_response.status_code == 201
    return kit1_response

# La funcion negative_assert_code_400 aplica los datos de prueba negativos en el cuerpo de la solicitud
def negative_assert_code_400(kit_body):
    kit1_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit1_response.status_code == 400
    return kit1_response


# test 1
def test_1_characters():
    kit1 = get_kit_body("a")
    positive_assert(kit1)

# test 2
def test_511_caracters():
    kit1 = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit1)

# test 3
def test_zero_characters():
    kit1 = get_kit_body("")
    negative_assert_code_400(kit1)

# test 4
def test_512_caracters():
    kit1 = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit1)

# test 5
def test_special_caracters():
    kit1 = get_kit_body('"№%@",')
    positive_assert(kit1)

# test 6
def test_spaces():
    kit1 = get_kit_body("A Aaa")
    positive_assert(kit1)

# test 7
def test_numbers():
    kit1 = get_kit_body("123")
    positive_assert(kit1)

# test 8
def test_no_parameters():
    kit1 = get_kit_body(0)
    negative_assert_code_400(kit1)

# test 9
def test_parameter_dif_number():
    kit1 = get_kit_body(123)
    negative_assert_code_400(kit1)
