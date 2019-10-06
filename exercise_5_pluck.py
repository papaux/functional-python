#! /bin/python

from functools import reduce


def non_functional():

  def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

  def call(fn, key):
    def apply_fn(record):
      return assoc(record, key, fn(record.get(key)))
    return apply_fn

  def extract_name_and_country(band):
    plucked_band = {}
    plucked_band['name'] = band['name']
    plucked_band['country'] = band['country']
    return plucked_band

  def pipeline_each(bands, transforms):
    return list(reduce(lambda b, f: map(f, b),
            transforms,
            bands))

  bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
          {'name': 'women', 'country': 'Germany', 'active': False},
          {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

  print(pipeline_each(bands, [call(lambda x: 'Canada', 'country'),
                              call(lambda x: x.replace('.', ''), 'name'),
                              call(str.title, 'name'),
                              extract_name_and_country]))



def functional():

  def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

  def call(fn, key):
    def apply_fn(record):
      return assoc(record, key, fn(record.get(key)))
    return apply_fn

  def pluck(keys):
    def apply_pluck(record):
      return reduce(lambda a, key: assoc(a, key, record[key]), keys, {})
    return apply_pluck

  def pipeline_each(bands, transforms):
    return list(reduce(lambda b, f: map(f, b),
            transforms,
            bands))

  bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
          {'name': 'women', 'country': 'Germany', 'active': False},
          {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

  print(pipeline_each(bands, [call(lambda x: 'Canada', 'country'),
                              call(lambda x: x.replace('.', ''), 'name'),
                              call(str.title, 'name'),
                              pluck(['name', 'country'])]))


if __name__== "__main__":

  print("Non functional version")
  print("======================")
  non_functional()

  print()
  print("Functional version")
  print("======================")
  functional()

