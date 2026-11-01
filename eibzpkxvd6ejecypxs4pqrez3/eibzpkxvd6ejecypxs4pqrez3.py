import xtqz1bv8mlviwo7a892eslt6x as Dependency


class eibzpkxvd6ejecypxs4pqrez3[Type](Dependency._[Type]):
    data_type: type[Type]

    @Dependency._.value.setter
    def value(self, new_value: Type) -> None:
        if self._value != new_value:
            self._value = new_value
            self.value_changed.emit(self._value)
            self.valueChanged.emit(self._value)
