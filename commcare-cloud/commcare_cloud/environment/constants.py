import jsonobject


class _Constants(jsonobject.JsonObject):
    commcarehq_main_db_name = jsonobject.StringProperty(default='commcarehq')
    formplayer_db_name = jsonobject.StringProperty(default='formplayer')
    ucr_db_name = jsonobject.StringProperty(default='commcarehq_ucr')


constants = _Constants()
