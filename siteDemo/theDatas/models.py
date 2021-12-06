from django.db import models

import mongoengine
# 表名
class TestModel(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    age = mongoengine.IntField(default=0)

class Test(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    enName = mongoengine.StringField(max_length=16)
    provinceName = mongoengine.StringField(max_length=16)
    lastUpdate = mongoengine.StringField (max_length=16)# "2020-03-30T05:34:43.000Z"
    confirmedCount = mongoengine.IntField(default=0)
    suspectedCount = mongoengine.IntField(default=0)
    curedCount = mongoengine.IntField(default=0)
    deadCount = mongoengine.IntField(default=0)
    seriousCount = mongoengine.IntField(default=0)
    suspectedIncreased = mongoengine.IntField(default=0)
    confirmedIncreased = mongoengine.IntField(default=0)
    curedIncreased = mongoengine.IntField(default=0)
    deadIncreased = mongoengine.IntField(default=0)
    seriousIncreased = mongoengine.IntField(default=0)
    updateTime = mongoengine.StringField(max_length=16)
    insickCount = mongoengine.IntField(default=0)
    updateDate = mongoengine.StringField(max_length=16)
    seriousRate = mongoengine.StringField(max_length=16)
    seriousDayRate = mongoengine.StringField(max_length=16)
    suspectedAccum = mongoengine.IntField(default=0)
    curedRate = mongoengine.StringField(max_length=16)
    deadRate = mongoengine.StringField(max_length=16)
    seriousDeadRate = mongoengine.StringField(max_length=16)
    # Null
    cities = mongoengine.BinaryField(max_bytes=None)

    countryEnglishName = mongoengine.StringField(max_length=16)
    countryName = mongoengine.StringField(max_length=16)
    locationId = mongoengine.IntField(default=0)
    continentName = mongoengine.StringField(max_length=16)
    timestamp = mongoengine.IntField(default=0)
    provinceEnglishName = mongoengine.StringField(max_length=16)
    comment = mongoengine.StringField(max_length=16)
    maxZeroIncrDays = mongoengine.IntField(default=0)
    currentConfirmedCount = mongoengine.IntField(default=0)
    provinceShortName = mongoengine.StringField(max_length=16)
    continentEnglishName = mongoengine.StringField(max_length=16)

class ByCountry(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    enName = mongoengine.StringField(max_length=16)
    provinceName = mongoengine.StringField(max_length=16)
    lastUpdate = mongoengine.StringField (max_length=16)# "2020-03-30T05:34:43.000Z"
    confirmedCount = mongoengine.IntField(default=0)
    suspectedCount = mongoengine.IntField(default=0)
    curedCount = mongoengine.IntField(default=0)
    deadCount = mongoengine.IntField(default=0)
    seriousCount = mongoengine.IntField(default=0)
    suspectedIncreased = mongoengine.IntField(default=0)
    confirmedIncreased = mongoengine.IntField(default=0)
    curedIncreased = mongoengine.IntField(default=0)
    deadIncreased = mongoengine.IntField(default=0)
    seriousIncreased = mongoengine.IntField(default=0)
    updateTime = mongoengine.StringField(max_length=16)
    insickCount = mongoengine.IntField(default=0)
    updateDate = mongoengine.StringField(max_length=16)
    seriousRate = mongoengine.StringField(max_length=16)
    seriousDayRate = mongoengine.StringField(max_length=16)
    suspectedAccum = mongoengine.IntField(default=0)
    curedRate = mongoengine.StringField(max_length=16)
    deadRate = mongoengine.StringField(max_length=16)
    seriousDeadRate = mongoengine.StringField(max_length=16)
    # Null
    cities = mongoengine.BinaryField(max_bytes=None)

    countryEnglishName = mongoengine.StringField(max_length=16)
    countryName = mongoengine.StringField(max_length=16)
    locationId = mongoengine.IntField(default=0)
    continentName = mongoengine.StringField(max_length=16)
    timestamp = mongoengine.IntField(default=0)
    provinceEnglishName = mongoengine.StringField(max_length=16)
    comment = mongoengine.StringField(max_length=16)
    maxZeroIncrDays = mongoengine.IntField(default=0)
    currentConfirmedCount = mongoengine.IntField(default=0)
    provinceShortName = mongoengine.StringField(max_length=16)
    continentEnglishName = mongoengine.StringField(max_length=16)

class ByDate(mongoengine.Document):
    day = mongoengine.StringField(max_length=16)
    records = mongoengine.fields
    confirmedIncreased = mongoengine.IntField(default=0)
    curedIncreased = mongoengine.IntField(default=0)
    deadIncreased = mongoengine.IntField(default=0)
    maxZeroIncrDays = mongoengine.IntField(default=0)

class ByArea(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    enName = mongoengine.StringField(max_length=16)
    provinceName = mongoengine.StringField(max_length=16)
    records = mongoengine.fields
    lastUpdate = mongoengine.StringField(max_length=16)
    updateTime = mongoengine.StringField(max_length=16)
    zipCode = mongoengine.StringField(max_length=16)
    confirmedCount = mongoengine.IntField(default=0)
    suspectedCount = mongoengine.IntField(default=0)
    curedCount = mongoengine.IntField(default=0)
    deadCount = mongoengine.IntField(default=0)
    insickCount = mongoengine.IntField(default=0)
    confirmedIncreased = mongoengine.IntField(default=0)
    curedIncreased = mongoengine.IntField(default=0)
    deadIncreased = mongoengine.IntField(default=0)
    maxZeroIncrDays = mongoengine.IntField(default=0)

class ByIncrease(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    lastUpdate = mongoengine.StringField(max_length=16)
    records = mongoengine.fields

class ByOverall(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    enName = mongoengine.StringField(max_length=16)
    provinceName = mongoengine.StringField(max_length=16)
    records = mongoengine.fields
    lastUpdate = mongoengine.StringField(max_length=16)
    updateTime = mongoengine.StringField(max_length=16)
    zipCode = mongoengine.StringField(max_length=16)
    confirmedCount = mongoengine.IntField(default=0)
    suspectedCount = mongoengine.IntField(default=0)
    curedCount = mongoengine.IntField(default=0)
    deadCount = mongoengine.IntField(default=0)
    insickCount = mongoengine.IntField(default=0)
    confirmedIncreased = mongoengine.IntField(default=0)
    curedIncreased = mongoengine.IntField(default=0)
    deadIncreased = mongoengine.IntField(default=0)
    maxZeroIncrDays = mongoengine.IntField(default=0)

class BySearchterm(mongoengine.Document):
    url = mongoengine.StringField(max_length=16)
    keywords = mongoengine.fields

class ByWorld(mongoengine.Document):
    records = mongoengine.fields
    locationId = mongoengine.IntField(default=0)
    continentName = mongoengine.StringField(max_length=16)
    continentEnglishName = mongoengine.StringField(max_length=16)
    countryName = mongoengine.StringField(max_length=16)
    countryEnglishName = mongoengine.StringField(max_length=16)
    provinceName = mongoengine.StringField(max_length=16)
    provinceShortName = mongoengine.StringField(max_length=16)
    provinceEnglishName = mongoengine.StringField(max_length=16)
    currentConfirmedCount = mongoengine.IntField(default=0)
    confirmedCount = mongoengine.IntField(default=0)
    suspectedCount = mongoengine.IntField(default=0)
    curedCount = mongoengine.IntField(default=0)
    deadCount = mongoengine.IntField(default=0)
    cities = mongoengine.StringField(max_length=16)
    comment = mongoengine.StringField(max_length=16)
    updateTime = mongoengine.StringField(max_length=16)
    timestamp = mongoengine.LongField(default=0)
    lastUpdate = mongoengine.StringField(max_length=16)
    name = mongoengine.StringField(max_length=16)
    enName = mongoengine.StringField(max_length=16)
    confirmedIncreased = mongoengine.IntField(default=0)
    curedIncreased = mongoengine.IntField(default=0)
    deadIncreased = mongoengine.IntField(default=0)

