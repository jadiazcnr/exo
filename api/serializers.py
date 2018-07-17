from rest_framework import serializers
from datetime import datetime
from rates.common import CURRENCY


class RatesSerializer(serializers.ModelSerializer):

    def validate(self, data):
        errors = {}
        date_form = data.get('date-from')
        date_to = data.get('date-to')

        if not date_form:
            errors['1'] = u'date-from is required'
        else:
            try:
                datetime.strptime(date_form, '%Y-%m-%d')
            except ValueError:
                errors['3'] = u'date-from has incorrect data format, should be YYYY-MM-DD'
        if not date_to:
            errors['2'] = u'date-to is required'
        else:
            try:
                datetime.strptime(date_to, '%Y-%m-%d')
            except ValueError:
                errors['4'] = u'date-to has incorrect data format, should be YYYY-MM-DD'

        if errors:
            raise serializers.ValidationError(errors)
        return data


class ConvertSerializer(serializers.ModelSerializer):

    def validate(self, data):
        errors = {}
        origin = data.get('origin')
        target = data.get('target')
        amount = data.get('amount')

        if not origin:
            errors['5'] = u'origin is required'
        else:
            if origin not in CURRENCY:
                errors['6'] = u'origin has to be one of ' + CURRENCY
        if not target:
            errors['7'] = u'target is required'
        else:
            if target not in CURRENCY:
                errors['8'] = u'target has to be one of ' + CURRENCY
        if not amount:
            errors['9'] = u'amount is required'
        else:
            try:
                float(amount)
            except ValueError:
                errors['10'] = u'amount has to be a decimal number'

        if errors:
            raise serializers.ValidationError(errors)
        return data


class TimeWeightedSerializer(serializers.ModelSerializer):
    def validate(self, data):
        errors = {}
        origin = data.get("origin")
        target = data.get("target")
        amount = data.get("amount")
        date_invested = data.get("date-invested")

        if not origin:
            errors['5'] = u'origin is required'
        else:
            if origin not in CURRENCY:
                errors['6'] = u'origin has to be one of ' + CURRENCY
        if not target:
            errors['7'] = u'target is required'
        else:
            if target not in CURRENCY:
                errors['8'] = u'target has to be one of ' + CURRENCY
        if not amount:
            errors['9'] = u'amount is required'
        else:
            try:
                float(amount)
            except ValueError:
                errors['10'] = u'amount has to be a decimal number'

        if not date_invested:
            errors['2'] = u'date-invested is required'
        else:
            try:
                datetime.strptime(date_invested, '%Y-%m-%d')
            except ValueError:
                errors['4'] = u'date-to has incorrect data format, should be YYYY-MM-DD'

        if errors:
            raise serializers.ValidationError(errors)
        return data
