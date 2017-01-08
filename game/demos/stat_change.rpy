init python:
    class CustomFieldValue(FieldValue):
        def changed(self, value):
            super(CustomFieldValue, self).changed(value)
            update_sounds()

screen stats:
    frame:
        xsize 200
        has vbox
        text "craziness"
        bar value CustomFieldValue(stats, 'crazy', 1.0)
        text "light"
        bar value CustomFieldValue(stats, 'light', 1.0)
        text "bear"
        bar value CustomFieldValue(stats, 'bear', 1.0)
