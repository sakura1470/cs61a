test = {
  'name': 'filter-lst',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4))
          18ed436675247bac3aee01a3103ea649
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(1 3 5))
          4cc9884dfb545fbb2d98f3843fec6a4a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(2 4 6 1))
          e7b3891c5a7d2f503188f1818ec702da
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst even? '(3))
          d17487605f66346bf68b6fb7c92f6257
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? nil)
          d17487605f66346bf68b6fb7c92f6257
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4)) ; checks you dont use builtin filter
          (2 4)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define filter nil) 
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
