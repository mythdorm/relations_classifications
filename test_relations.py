
from unittest import TestCase
import relations

class TestRelationsReflexive(TestCase):
    def test_irreflexive_check(self):
        matrix = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]

        expected = False
        actual = relations.check_reflexive(matrix)

        self.assertEqual(expected, actual)

    def test_irreflexive_fix(self):
        matrix = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        expected = [[1,0,0],
                   [0,1,0],
                   [0,0,1]]

        actual = relations.make_reflexive(matrix)
        self.assertEqual(expected, actual)

    def test_single_pair_check(self):
        matrix = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]

        expected = False
        actual = relations.check_reflexive(matrix)

        self.assertEqual(expected, actual)

    def test_single_pair_fix(self):
        matrix = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
        expected = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]

        actual = relations.make_reflexive(matrix)
        self.assertEqual(expected, actual)

    def test_two_pair_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]

        expected = False
        actual = relations.check_reflexive(matrix)

        self.assertEqual(expected, actual)

    def test_two_pair_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
        expected = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]

        actual = relations.make_reflexive(matrix)
        self.assertEqual(expected, actual)

    def test_reflexive_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]

        expected = True
        actual = relations.check_reflexive(matrix)

        self.assertEqual(expected, actual)

    def test_reflexive_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]

        actual = relations.make_reflexive(matrix)
        self.assertEqual(expected, actual)

class TestRelationsIrreflexive(TestCase):
    def test_irreflexive_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = False
        actual = relations.check_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_irreflexive_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],]
        actual = relations.make_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_single_irreflexive_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]

        expected = False
        actual = relations.check_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_single_irreflexive_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        actual = relations.make_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_two_irreflexive_check(self):
        matrix = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]

        expected = False
        actual = relations.check_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_two_irreflexive_fix(self):
        matrix = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        actual = relations.make_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_already_irreflexive_check(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        expected = True
        actual = relations.check_irreflexive(matrix)
        self.assertEqual(expected, actual)

    def test_already_irreflexive_fix(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        actual = relations.make_irreflexive(matrix)
        self.assertEqual(expected, actual)

class TestRelationsSymmetric(TestCase):
    def test_antisymmetric_matrix_check(self):
        matrix = [[0, 0, 1],
                  [1, 0, 0],
                  [0, 1, 0]]

        expected = False
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_antisymmetric_matrix_fix(self):
        matrix = [[0, 0, 1],
                  [1, 0, 0],
                  [0, 1, 0]]
        expected = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_check(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]]
        expected = True
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_fix(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]]
        expected = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_one_symmetric_check(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 0, 0]]
        expected = False
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_one_symmetric_fix(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 0, 0]]
        expected = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_two_symmetric_check(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [1, 0, 0]]
        expected = False
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_two_symmetric_fix(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [1, 0, 0]]
        expected = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_right_check(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [0, 0, 0]]
        expected = False
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_right_fix(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [0, 0, 0]]
        expected = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_left_check(self):
        matrix = [[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0]]
        expected = False
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_left_fix(self):
        matrix = [[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0]]
        expected = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_symmetrix_with_reflexive_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = True
        actual = relations.check_symmetric(matrix)
        self.assertEqual(expected, actual)

    def test_symmetrix_with_reflexive_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        actual = relations.make_symmetric(matrix)
        self.assertEqual(expected, actual)

class TestRelationsAntisymmetric(TestCase):
    def test_symmetric_matrix_check(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]]

        expected = False
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_matrix_fix(self):
        expected = [[0, 1, 1],
                  [0, 0, 1],
                  [0, 0, 0]]
        matrix = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_antisymmetric_check(self):
        matrix = [[0, 0, 1],
                  [1, 0, 0],
                  [0, 1, 0]]
        expected = True
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_antisymmetric_fix(self):
        matrix = [[0, 0, 1],
                  [1, 0, 0],
                  [0, 1, 0]]
        expected = [[0, 0, 1],
                  [1, 0, 0],
                  [0, 1, 0]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_one_symmetric_check(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 0, 0]]
        expected = False
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_one_symmetric_fix(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [1, 0, 0]]
        expected = [[0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_two_symmetric_check(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [1, 0, 0]]
        expected = False
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_all_but_two_symmetric_fix(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [1, 0, 0]]
        expected = [[0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_right_check(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [0, 0, 0]]
        expected = True
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_right_fix(self):
        matrix = [[0, 1, 1],
                  [0, 0, 1],
                  [0, 0, 0]]
        expected = [[0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_left_check(self):
        matrix = [[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0]]
        expected = True
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_symmetry_heavy_left_fix(self):
        matrix = [[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0]]
        expected = [[0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_with_reflexive_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = True
        actual = relations.check_antisymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_with_reflexive_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]
        actual = relations.make_antisymmetric(matrix)
        self.assertEqual(expected, actual)

class TestRelationsAsymmetric(TestCase):
    def test_antisymmetric_only(self):
        matrix = [[0,1,0],
                  [0,1,0],
                  [0,1,0]]
        expected = False
        actual = relations.check_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_antisymmetric_only_fix(self):
        matrix = [[0,1,0],
                  [0,1,0],
                  [0,1,0]]
        expected = [[0,1,0],
                  [0,0,0],
                  [0,1,0]]
        actual = relations.make_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_irreflexive_only(self):
        matrix = [[0, 1, 0],
                  [1, 0, 0],
                  [0, 1, 0]]
        expected = False
        actual = relations.check_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_irreflexive_only_fix(self):
        matrix = [[0, 1, 0],
                  [1, 0, 0],
                  [0, 1, 0]]
        expected = [[0, 1, 0],
                    [0, 0, 0],
                    [0, 1, 0]]
        actual = relations.make_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_asymmetry(self):
        matrix = [[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]]
        expected = False
        actual = relations.check_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_no_asymmetry_fix(self):
        matrix = [[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]]
        expected = [[0, 1, 0],
                    [0, 0, 1],
                    [0, 0, 0]]
        actual = relations.make_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_partial_asymmetry(self):
        matrix = [[0, 1, 0],
                  [0, 0, 1],
                  [0, 1, 0]]
        expected = False
        actual = relations.check_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_partial_asymmetry_fix(self):
        matrix = [[0, 1, 0],
                  [0, 0, 1],
                  [0, 1, 0]]
        expected = [[0, 1, 0],
                    [0, 0, 1],
                    [0, 0, 0]]
        actual = relations.make_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_full_asymmetry(self):
        matrix = [[0, 1, 0],
                  [0, 0, 0],
                  [0, 1, 0]]
        expected = True
        actual = relations.check_asymmetric(matrix)
        self.assertEqual(expected, actual)

    def test_full_asymmetry_fix(self):
        matrix = [[0, 1, 0],
                  [0, 0, 0],
                  [0, 1, 0]]
        expected = [[0, 1, 0],
                  [0, 0, 0],
                  [0, 1, 0]]
        actual = relations.make_asymmetric(matrix)
        self.assertEqual(expected, actual)

class TestRelationsTransitive(TestCase):
    def test_reflexive_matrix(self):
        matrix = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
        expected = True
        actual = relations.check_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_reflexive_matrix_fix(self):
        matrix = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
        expected = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
        actual = relations.make_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_irreflexive_matrix(self):
        matrix = [[0,0,0],
                  [0,0,1],
                  [0,0,0]]
        expected = True
        actual = relations.check_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_irreflexive_matrix_fix(self):
        matrix = [[0,0,0],
                  [0,0,1],
                  [0,0,0]]
        expected = [[0,0,0],
                  [0,0,1],
                  [0,0,0]]
        actual = relations.make_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_matrix(self):
        matrix = [[0,1,0],
                  [1,0,1],
                  [0,1,0]]
        expected = False
        actual = relations.check_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_matrix_fix(self):
        matrix = [[0,1,0],
                  [1,0,1],
                  [0,1,0]]
        expected = [[1,1,1],
                  [1,1,1],
                  [1,1,1]]
        actual = relations.make_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_antisymmetric_matrix(self):
        matrix = [[0,1,0],
                  [0,0,0],
                  [1,0,1]]
        expected = False
        actual = relations.check_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_antisymmetric_matrix_fix(self):
        matrix = [[0,1,0],
                  [0,0,0],
                  [1,0,1]]
        expected = [[0,1,0],
                  [0,0,0],
                  [1,1,1]]
        actual = relations.make_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_asymmetric_matrix(self):
        matrix = [[0,1,0],
                  [0,0,0],
                  [0,1,0]]
        expected = True
        actual = relations.check_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_asymmetric_matrix_fix(self):
        matrix = [[0,1,0],
                  [0,0,0],
                  [0,1,0]]
        expected = [[0,1,0],
                  [0,0,0],
                  [0,1,0]]
        actual = relations.make_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_matrix(self):
        matrix = [[1,1,1],
                  [0,0,0],
                  [1,1,1]]
        expected = True
        actual = relations.check_transitive(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_matrix_fix(self):
        matrix = [[1,1,1],
                  [0,0,0],
                  [1,1,1]]
        expected = [[1,1,1],
                  [0,0,0],
                  [1,1,1]]
        actual = relations.make_transitive(matrix)
        self.assertEqual(expected, actual)

class TestRelationsEquivalence(TestCase):
    def test_transitive_check(self):
        matrix = [[1,1,1],
                  [0,0,0],
                  [1,1,1]]
        expected = False
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_fix(self):
        matrix = [[1,1,1],
                  [0,0,0],
                  [1,1,1]]
        expected = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_check(self):
        matrix = [[0, 1, 1],
                  [1, 0, 0],
                  [1, 0, 0]]
        expected = False
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_fix(self):
        matrix = [[0, 1, 1],
                  [1, 0, 0],
                  [1, 0, 0]]
        expected = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_reflexive_check(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = True
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_reflexive_fix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        expected = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_symmetric_check(self):
        matrix = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 0]]
        expected = False
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_symmetric_fix(self):
        matrix = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 0]]
        expected = [[1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_reflexive_check(self):
        matrix = [[1, 1, 1],
                  [0, 1, 0],
                  [1, 1, 1]]
        expected = False
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_transitive_reflexive_fix(self):
        matrix = [[1, 1, 1],
                  [0, 1, 0],
                  [1, 1, 1]]
        expected = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_reflexive_check(self):
        matrix = [[1, 1, 0],
                  [1, 1, 1],
                  [0, 1, 1]]
        expected = False
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_symmetric_reflexive_fix(self):
        matrix = [[1, 1, 0],
                  [1, 1, 1],
                  [0, 1, 1]]
        expected = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_equivalence_check(self):
        matrix = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        expected = True
        actual = relations.check_equivalence(matrix)
        self.assertEqual(expected, actual)

    def test_equivalence_fix(self):
        matrix = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        expected = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        actual = relations.make_equivalence(matrix)
        self.assertEqual(expected, actual)

class TestRelationsDifferences(TestCase):
    def test_check_difference_none(self):
        first_matrix = [[0,1,0],
                        [1,0,1],
                        [0,1,1]]
        second_matrix = [[0,1,0],
                        [1,0,1],
                        [0,1,1]]
        expected = []
        actual = relations.check_differences(first_matrix, second_matrix)
        self.assertEqual(expected, actual)

    def test_check_difference_single(self):
        first_matrix = [[1, 1, 0],
                        [1, 0, 1],
                        [0, 1, 1]]
        second_matrix = [[0, 1, 0],
                         [1, 0, 1],
                         [0, 1, 1]]
        expected = [[(0,0),"1 --> 0"]]
        actual = relations.check_differences(first_matrix, second_matrix)
        self.assertEqual(expected, actual)

    def test_check_difference_multiple(self):
        first_matrix = [[1, 1, 0],
                        [1, 0, 1],
                        [0, 1, 0]]
        second_matrix = [[0, 1, 0],
                         [1, 1, 1],
                         [0, 1, 1]]
        expected = [[(0, 0), "1 --> 0"],[(1, 1), "0 --> 1"],[(2, 2), "0 --> 1"]]
        actual = relations.check_differences(first_matrix, second_matrix)
        self.assertEqual(expected, actual)