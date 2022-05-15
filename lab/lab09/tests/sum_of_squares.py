test = {
  'name': 'sum_of_squares',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sum-of-squares 3 4)
          cc2eb9e12f87b26594c445f7d87461f0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sum-of-squares -1 0)
          7cd20da6435c318b417f99ab831ac85e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sum-of-squares 1 -100)
          03bfbf96a7d00c7f2619b7795bd7eea4
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
