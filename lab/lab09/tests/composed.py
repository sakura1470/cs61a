test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add-then-mul 2)
          aae76aca9259a704209b44193fad5f6a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed add-one add-one) 2)
          a1e11865670a42d05e20b9a3455dc457
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two multiply-by-two) 2)
          2bfcd627609c82ebd017c2edfad00c89
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed add-one multiply-by-two) 2)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) add-one) 2)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) multiply-by-two) 2)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two (composed add-one add-one)) 2)
          8
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define (add-one a) (+ a 1))
      scm> (define (multiply-by-two a) (* a 2))
      scm> (define add-then-mul (composed multiply-by-two add-one))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
