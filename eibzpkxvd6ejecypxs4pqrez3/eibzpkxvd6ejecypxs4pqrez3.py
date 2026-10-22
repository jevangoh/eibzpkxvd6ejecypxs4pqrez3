import xtqz1bv8mlviwo7a892eslt6x as Dependency


class eibzpkxvd6ejecypxs4pqrez3[Type](Dependency._[Type]):
    data_type: type[Type]
    value: Type

    def set_value(self, new_value: Type):
        if self._value != new_value:
            self._value = new_value
            self.value_changed.emit(self._value)
            self.valueChanged.emit(self._value)
