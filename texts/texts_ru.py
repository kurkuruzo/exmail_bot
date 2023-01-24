from dataclasses import dataclass


@dataclass(slots=True)
class TEXTS_CLASS:
    manage_shop_btn: str
    cancel_btn: str
    start_message: str
    help_message: str
    request_shop_number_message: str
    manage_shop_message: str
    open_btn: str
    close_btn: str
    other_answer: str
    user_not_found_message: str
    shop_not_found_message: str
    shop_opened_message: str
    address_confirmation_message: str
    yes_btn: str
    no_btn: str
    geolocation_request_message: str
    geolocation_request_btn: str


TEXTS_RU = TEXTS_CLASS(
    manage_shop_btn="Управлять ПВЗ",
    cancel_btn="Отмена",
    start_message="Здравствуйте! Вас приветствует бот для управления ПВЗ. \nПожалуйста, выберите, что вы хотите сделать с помощью клавиатуры.",
    help_message='Чтобы управлять ПВЗ запустите бота командой /start, затем выберите "Управлять ПВЗ" на клавиатуре',
    request_shop_number_message="Пожалуйста, пришлите номер ПВЗ",
    manage_shop_message="Пожалуйста, выберите, что вы хотите сделать",
    open_btn="Открыть ПВЗ",
    close_btn="Закрыть ПВЗ",
    other_answer="Я не понял, что вы хотели сделать...",
    user_not_found_message="Пользователь с id = {user_id} не найден.",
    shop_not_found_message="ПВЗ с id = {shop_id} не найден.",
    shop_opened_message="ПВЗ по адресу {address} открыт в {datetime}",
    address_confirmation_message="Вы хотите {operation} ПВЗ по адресу {address}?",
    yes_btn="Да",
    no_btn="Нет",
    geolocation_request_message="Пожалуйста, отправьте ваше местоположение с помощью кнопки",
    geolocation_request_btn="Отправить местоположение",
)
