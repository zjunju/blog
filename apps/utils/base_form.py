class FormsMixin(object):
    def get_json_error(self):
        if getattr(self, 'errors'):
            data = self.errors.get_json_data()
            errors = {}
            for key, values in data.items():
                errors[key] = []
                for message in values:
                    errors[key].append(message.get('message'))
            return errors
        else:
            return {}
