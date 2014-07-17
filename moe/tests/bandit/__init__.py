# -*- coding: utf-8 -*-
r"""Testing code for the (Python) bandit library.

Testing is done via the Testify package:
https://github.com/Yelp/Testify

This package includes:

* Test cases/test setup files
* Tests for bandit/epsilon

**Files in this package**

* bandit_test_case.py: test case with different sampled arm historical info inputs

**Files in this package**

* optimal_learning_test_case.py: base test case for bandit tests with some extra asserts; meant to provide
  a well-behaved source of random arm to unit tests.

"""