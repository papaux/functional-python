#! /bin/python

from functools import reduce

def non_functional():
  bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
          {'name': 'women', 'country': 'Germany', 'active': False},
          {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

  def format_bands(bands):
    for band in bands:
      band['country'] = 'Canada'
      band['name'] = band['name'].replace('.', '')
      band['name'] = band['name'].title()

  format_bands(bands)

  print(bands)
  # => [{'name': 'Sunset Rubdown', 'active': False, 'country': 'Canada'},
  #     {'name': 'Women', 'active': False, 'country': 'Canada' },
  #     {'name': 'A Silver Mt Zion', 'active': True, 'country': 'Canada'}]


def functional():

  def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

  def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")

  def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))

  def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())

  def pipeline_each_mine(bands, transforms):
    if(not transforms): return list(bands)

    return pipeline_each_mine(map(lambda b: transforms[0](b), bands), transforms[1:])

  def pipeline_each_solution(bands, transforms):
    return list(reduce(lambda b, f: map(f, b),
            transforms,
            bands))


  bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
          {'name': 'women', 'country': 'Germany', 'active': False},
          {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

  print(pipeline_each_mine(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names]))

  print(pipeline_each_solution(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names]))


def more_functional():
  """
  Ultimate and cleanest solution
  """

  def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

  def call(fn, key):
    def apply_fn(record):
      return assoc(record, key, fn(record.get(key)))
    return apply_fn

  def pipeline_each(bands, transforms):
    return list(reduce(lambda b, f: map(f, b),
            transforms,
            bands))

  bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
          {'name': 'women', 'country': 'Germany', 'active': False},
          {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

  print(pipeline_each(bands, [call(lambda x: 'Canada', 'country'),
                              call(lambda x: x.replace('.', ''), 'name'),
                              call(str.title, 'name')]))



if __name__== "__main__":

  print("Non functional version")
  print("======================")
  non_functional()

  print()
  print("Functional version")
  print("======================")
  functional()

  print()
  print("More Functional version")
  print("======================")
  more_functional()
