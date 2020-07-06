from datetime import date


class Date(date):
    year_month_day = "%Y %m %d"
    month_day_year = "%m %d %Y"

    def __init__(self, *args, **kwargs):
        self.string_format = self.year_month_day
        super(Date, self).__init__(*args, **kwargs)

    @classmethod
    def __repr__(cls):
        return cls.strftime(cls.string_format)


    def __str__(self):
        return self.strftime(self.string_format)
