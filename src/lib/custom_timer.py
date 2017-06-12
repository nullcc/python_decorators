# -*- coding: utf-8 -*-

from threading import _Timer


class CustomTimer(_Timer):
    def __init__(self, interval, function, *args, **kwargs):
        self._original_function = function
        super(CustomTimer, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *args, **kwargs):
        self.result = self._original_function(*args, **kwargs)

    def c_join(self):
        super(CustomTimer, self).join()
        return self.result
